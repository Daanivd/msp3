import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import datetime
from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'recipeDB'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo = PyMongo(app)



#@app.route('/')
@app.route('/recipes/<page>', methods=['GET'])    
def recipes(page):
      allergensF = request.args.getlist('allergensF')
      dietF = request.args.getlist('dietF')
      if dietF == []:
        dietF = ['Vegetarian', 'Vegan', 'Meat', 'Fish']
      recipes = mongo.db.recipes.find({'$and':[{'diet': {'$in': dietF}}, {'allergens': {'$nin': allergensF}}]}).sort('dateEntered',-1)
      recipesV = mongo.db.recipes.find({'$and':[{'diet': {'$in': dietF}}, {'allergens': {'$nin': allergensF}}]}).sort('views', -1)
      total = recipes.count()
      nPerPage = 4
      pages = list(range(1,-(-total//nPerPage)+1))
      skip = (int(page)-1)*nPerPage
      recipes=recipes.skip(skip).limit(nPerPage)
      recipesV=recipesV.skip(skip).limit(nPerPage)
      return render_template('recipes.html', dietF=dietF, allergensF=allergensF, page=page, recipes = recipes, recipesV = recipesV, pages=pages, types=mongo.db.type.find(), allergens=mongo.db.allergens.find())

@app.route('/filter_recipes', methods=['POST'])
def filter_recipe():
    
    allergensF = request.form.getlist('allergens')
    dietF = request.form.getlist('diet')
    #mongo.db.filters.update_one({},{'$set': {'dietF': dietF,
       #                                  'allergensF': allergensF}})
    
#filteredRecipes = mongo.db.recipes.find({'diet': {'all': diet}, 'allergens': {'nin': allergens}})
                                            
    return redirect(url_for('recipes', page=1, dietF = dietF, allergensF = allergensF))

@app.route('/recipe/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    views = the_recipe['views']
    views = views + 1
    mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)}, {'$set': {'views': views}})
    return render_template('recipe.html', recipe=the_recipe, views=views)
 
@app.route('/create')
def create():
     return render_template('create.html', types=mongo.db.type.find(), allergens=mongo.db.allergens.find())
     
@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    dateEntered = datetime.datetime.now().strftime('%d-%m-%y')
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
     the_recipe =  mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
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
    mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)}, {'$set': {'recipeName': recipeName,
                                                                        'ingredients': ingredients,
                                                                        'directions': directions,
                                                                        'diet': diet,
                                                                        'allergens': allergens, 
                                                                        'keywords': keywords}})
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    views = the_recipe['views']
    views = views + 1
    return redirect(url_for('recipes', page=1))
    
     
@app.route('/delete/<recipe_id>')
def delete(recipe_id):
     mongo.db.recipes.delete_one({'_id': ObjectId(recipe_id)})
     return redirect(url_for('recipes', page=1))   
    

@app.route('/search_recipes', methods=['POST'])
def search_recipes():
    searchKey = request.form['searchKey']
    searchResults = mongo.db.recipes.find({'keywords': searchKey})
    return render_template('recipes.html', page=1, recipes=searchResults)
     
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
