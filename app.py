import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import datetime


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'recipeDB'
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost')
mongo = PyMongo(app)

##### APP.ROUTES #####

# Redirect to Recipes Page
@app.route('/')
def landing_page():
     return redirect(url_for('recipes', page=1))
  
  
# Recipes Page    
@app.route('/recipes/<page>', methods=['GET'])    
def recipes(page):
      allergensF = request.args.getlist('allergensF')
      dietF = request.args.getlist('dietF')
     
      if dietF == []:
        recipes = mongo.db.recipes.find({'allergens': {'$nin': allergensF}}).sort('dateEntered',-1)
        recipesV = mongo.db.recipes.find({'allergens': {'$nin': allergensF}}).sort('views',-1)
      else:
        recipes = mongo.db.recipes.find({'$and':[{'diet': {'$in': dietF}}, 
                                        {'allergens': {'$nin': allergensF}}]}).sort('dateEntered',-1)
        recipesV = mongo.db.recipes.find({'$and':[{'diet': {'$in': dietF}}, 
                                        {'allergens': {'$nin': allergensF}}]}).sort('views',-1)
      total = recipes.count()
      nPerPage = 4
      pages = list(range(1,-(-total//nPerPage)+1))
      if int(page) > 1:
          prevPage = int(page) - 1
      else:
          prevPage = 1
      if int(page) < len(pages): 
          nextPage = int(page) + 1
      else:
          nextPage = len(pages)
          
      skip = (int(page)-1)*nPerPage
      recipes=recipes.skip(skip).limit(nPerPage)
      recipesV=recipesV.skip(skip).limit(nPerPage)
      return render_template('recipes.html', dietF=dietF, allergensF=allergensF, page=int(page), 
                             prevPage=prevPage, nextPage=nextPage, recipes = recipes, recipesV = recipesV, 
                             pages=pages, types=mongo.db.type.find(), allergens=mongo.db.allergens.find())


# Filter Recipes Function based on Allergens and Diet
@app.route('/filter_recipes', methods=['POST'])
def filter_recipe():
    allergensF = request.form.getlist('allergens')
    dietF = request.form.getlist('diet')
    return redirect(url_for('recipes', page=1, dietF = dietF, allergensF = allergensF))


# Single Recipe Page
@app.route('/recipe/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    views = the_recipe['views']
    views = views + 1
    mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)}, 
                                {'$set': {'views': views}})
    return render_template('recipe.html', recipe=the_recipe, views=views)
 
 
# Add Recipe Page 
@app.route('/create')
def create():
     return render_template('create.html', types=mongo.db.type.find(), allergens=mongo.db.allergens.find())
    
    
# Add Recipe to MongoDB Database Function     
@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    dateEntered = datetime.datetime.now().strftime('%d-%m-%y')
    recipes = mongo.db.recipes
    servings = request.form['servings']
    prepTime = request.form['prepTime']
    directions = request.form.getlist('directions')
    recipeName = request.form['recipe_name']
    ingredients =  request.form.getlist('ingredients')
    allergens = request.form.getlist('allergens')
    diet = request.form.getlist('diet')
    keywords = request.form['keywords']
    keywords = keywords.replace(" ", "").split(',')
    image = request.form['image']
    recipes.insert_one({'recipeName': recipeName, 
                        'dateEntered': dateEntered,
                        'servings': servings, 
                        'prepTime': prepTime, 
                        'diet': diet, 
                        'ingredients': ingredients, 
                        'directions': directions,
                        'allergens': allergens, 
                        'keywords': keywords, 
                        'image': image,
                        'views': 0})
    return redirect(url_for('recipes', page=1))
         

# Edit Recipe Page     
@app.route('/edit/<recipe_id>')
def edit(recipe_id):
     the_recipe =  mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
     recipes = mongo.db.recipes
     return render_template('edit.html', recipe=the_recipe, types=mongo.db.type.find(), allergens=mongo.db.allergens.find()) 
    
    
# Submit Edits to Recipe to MongoDB Function    
@app.route('/submit_edit/<recipe_id>', methods=['POST'])
def submit_edit(recipe_id):
    servings = request.form['servings']
    prepTime = request.form['prepTime']
    directions = request.form.getlist('directions')
    recipeName = request.form['recipe_name']
    ingredients =  request.form.getlist('ingredients')
    allergens = request.form.getlist('allergens')
    diet = request.form.getlist('diet')
    keywords = request.form['keywords']
    keywords = keywords.replace(" ", "").split(',')
    image = request.form['image']
    mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)}, {'$set': {'recipeName': recipeName,
                                                                        'ingredients': ingredients,
                                                                        'directions': directions,
                                                                        'diet': diet,
                                                                        'allergens': allergens, 
                                                                        'keywords': keywords,
                                                                        'image': image}})
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    views = the_recipe['views']
    views = views + 1
    return redirect(url_for('recipes', page=1))
    
 
# Delete Recipe from MongoDB Function     
@app.route('/delete/<recipe_id>')
def delete(recipe_id):
     mongo.db.recipes.delete_one({'_id': ObjectId(recipe_id)})
     return redirect(url_for('recipes', page=1))   
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
            
