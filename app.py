import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import datetime
from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipeDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


#@app.route('/')
@app.route('/recipes/<page>')    
def recipes(page):
      
      recipes = mongo.db.recipes.find().sort('dateEntered',-1)
      recipesV = mongo.db.recipes.find().sort('views', -1)
      total = recipes.count()
      nPerPage = 2
      pages = list(range(1,-(-total//nPerPage)+1))
      skip = (int(page)-1)*nPerPage
      recipes=recipes.skip(skip).limit(nPerPage)
      recipesV=recipesV.skip(skip).limit(nPerPage)
      return render_template("recipes.html", recipes = recipes, recipesV = recipesV, pages=pages)


@app.route('/recipe/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    views = the_recipe['views']
    views = views + 1
    mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$set": {"views": views}})
    return render_template('recipe.html', recipe=the_recipe, views=views)
 
 
@app.route('/create')
def create():
     return render_template('create.html', types=mongo.db.type.find(), allergens=mongo.db.allergens.find())
     
@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    dateEntered = datetime.datetime.now().strftime("%d-%m-%y")
    recipes = mongo.db.recipes
    servings = request.form['servings']
    prepTime = request.form['prepTime']
    directions = request.form['directions']
    recipeName = request.form['recipe_name']
    ingredients =  request.form.getlist('ingredients')
    allergens = request.form.getlist('allergens')
    diet = request.form.getlist('diet')
    keywords = request.form['keywords']
    keywords = keywords.strip().split(',')
    
    recipes.insert_one({'recipeName': recipeName.lower(), 
                        'dateEntered': dateEntered,
                        'servings': servings.lower(), 
                        'prepTime': prepTime.lower(), 
                        'diet': diet.lower(), 
                        'ingredients': ingredients.lower(), 
                        'directions': directions.lower(),
                        'allergens': allergens.lower(), 
                        'keywords': keywords.lower(), 
                        'views': 0})
    
    return redirect(url_for('recipes'))
         
     
@app.route('/edit/<recipe_id>')
def edit(recipe_id):
     the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
     recipes = mongo.db.recipes
     return render_template('edit.html', recipe=the_recipe, types=mongo.db.type.find(), allergens=mongo.db.allergens.find()) 
    
@app.route('/submit_edit/<recipe_id>', methods=['POST'])
def submit_edit(recipe_id):
    directions = request.form['directions']
    recipeName = request.form['recipe_name']
    ingredients =  request.form.getlist('ingredients')
    allergens = request.form.getlist('allergens')
    diet = request.form.getlist('diet')
    keywordString = request.form['keywords']
    keywords = keywordString.strip().split(',')
    mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {'$set': {'recipeName': recipeName,
                                                                        'ingredients': ingredients,
                                                                        'directions': directions,
                                                                        'diet': diet,
                                                                        'allergens': allergens, 
                                                                        'keywords': keywords}})
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    views = the_recipe['views']
    views = views + 1
    return redirect(url_for('recipes'))
    
     
@app.route('/delete/<recipe_id>')
def delete(recipe_id):
     mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
     return redirect(url_for('recipes'))   
    

@app.route('/search_recipes', methods=['POST'])
def search_recipes():
    searchKey = request.form["searchKey"]
    searchResults = mongo.db.recipes.find({'keywords': searchKey})
    return render_template('recipes.html', recipes=searchResults)
  


     
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
