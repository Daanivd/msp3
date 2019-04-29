import os
from flask import Flask, render_template, redirect, request, url_for
from flask-pymongo import PyMongo
from bson.objectid import ObjectId 
import datetime

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipeDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/recipes')    
def recipes():
      return render_template("recipes.html", recipes=mongo.db.recipes.find())


@app.route('/recipes/<recipe_id>')
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
    keywords = keywords.split(',')
    
    recipes.insert_one({'recipeName': recipeName, 'dateEntered': dateEntered, 'servings': servings, 'prepTime': prepTime, 'diet': diet, 'ingredients': ingredients, 'directions': directions, 'allergens': allergens, 'keywords': keywords, 'views': 0})
    
    return redirect(url_for('recipes'))
         
     
@app.route('/edit/<recipe_id>')
def edit(recipe_id):
     the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
     recipes = mongo.db.recipes
     return render_template('edit.html', recipe=the_recipe, types=mongo.db.type.find(), allergens=mongo.db.allergens.find()) 
    
@app.route('/submit_edit/<recipe_id>', methods=['POST'])
def submit_edit(recipe_id):
    #recipe_id = request.form['_id']
    
    directions = request.form['directions']
    recipeName = request.form['recipe_name']
    ingredients =  request.form.getlist('ingredients')
    allergens = request.form.getlist('allergens')
    keywordString = request.form('keywords')
    keywords = keywordString.split(",")
    mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {'$set': {'recipeName': recipeName, 'ingredients': ingredients, 'directions': directions, 'allergens': allergens, 'keywords': keywords}})
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    views = the_recipe['views']
    views = views + 1
    return redirect(url_for('recipes', ))
    
     
@app.route('/delete/<recipe_id>')
def delete(recipe_id):
     #recipe_id = request.form['_id']
     mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
     return redirect(url_for('recipes'))   
    

@app.route('/search_recipe', methods=['POST'])
def search_recipe():
    searchKey = request.form.get("searchKey")
    searchResults = mongo.db.recipes.find({"recipeKeywords": searchKey})
    return redirect(url_for('recipes', recipes=searchResults))    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
