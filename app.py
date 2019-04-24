import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

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
    
    the_ingredients = mongo.db.recipes.distinct('ingredients')
    the_allergens =  mongo.db.recipes.distinct('allergens')
    return render_template('recipe.html', recipe=the_recipe, ingredients=the_ingredients, allergens=the_allergens
    )
 
@app.route('/create')
def create():
     return render_template('create.html', types=mongo.db.type.find())
     
@app.route('/alter')
def alter():
     return render_template('alter.html') 

     
@app.route('/delete')
def delete():
     return render_template('delete.html')    
    
@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
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
