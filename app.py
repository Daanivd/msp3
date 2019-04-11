import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipeDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/recipes')    
def recipes():
      return render_template("recipes.html", recipes=mongo.db.recipes.find())
      
@app.route('/create')
def create():
     return render_template('create.html')
     
@app.route('/alter')
def alter():
     return render_template('alter.html') 
     
@app.route('/delete')
def delete():
     return render_template('delete.html')    
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
