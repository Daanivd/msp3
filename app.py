import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import datetime

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipeDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/search')    
def recipes():
      return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route('/recipes/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=the_recipe,
    )
 
@app.route('/create')
def create():
     return render_template('create.html', types=mongo.db.type.find())
     
@app.route('/alter/<recipe_id>')
def alter(recipe_id):
     the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
     recipes = mongo.db.recipes
     return render_template('alter.html', recipe=the_recipe) 
    
#@app.route('/change_recipe/<recipe_id>', methods=['POST'])
#def change_recipe(recipe_id):
#     the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
#     directions = request.form['directions']
#     recipeName = request.form['recipe_name']
#     ingredients =  request.form.getlist('ingredients')
#     allergens = request.form.getlist('allergens')
#     keywords = request.form.getlist('keywords')
#     the_recipe.update_one({'name': recipeName, 'ingredients': ingredients, 'allergens': allergens, 'keywords': keywords})
#     

     
@app.route('/delete')
def delete():
     return render_template('delete.html')    
    
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
    keywords = request.form.getlist('keywords')
    recipes.insert_one({'recipeName': recipeName, 'dateEntered': dateEntered, 'servings': servings, 'prepTime': prepTime, 'ingredients': ingredients, 'allergens': allergens, 'keywords': keywords, 'views': 0})
    return redirect(url_for('recipes'))
    
@app.route('/search_recipe', methods=['POST'])
def search_recipe():
    searchKey = request.form.get("searchKey")
    print(searchKey)
    searchResults = mongo.db.recipes.find({"recipeKeywords": searchKey})
    return redirect(url_for('recipes'))    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
