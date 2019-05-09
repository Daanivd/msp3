# Online Cookbook/Recipe Database

## Overview
 
### What is this website for?
 
This is a website for people to look up cooking recipes, and for people to add, edit or delete recipes to the online database. It provides filtering based on allergens and 
diet (vegan, vegetarian, fish, meat) and you can look up most popular recipes (based on views) or most recently added recipes (base on date recipe was entered into the database).
 
### What does it do?
 
This website is connected to an online database (MongoDB) where it stores recipes. Through an interactive website one can view, search, create, edit and delete these recipes. 
 
### How does it work
 
The backend uses **Python** to connect to the online database and perform the CRUD operations. The website is styled using **CSS** using **Materialize**. Additional logic was added
using **JQuery** and **Javascript**. A contact email was linked through EmailJS

## User Eperience Design

The website facilitates easy exploration of recipes present in the online database. The home page shows all recipes based on most popular (most views) and most recent
(most recently added). To not clutter the website, the recipes page is paginated. By simply clicking on a recipe of interest, the user is directed to that specific 
recipe page. This page holds all the information such as ingredients, Directions Allergens, and Keywords. Anyone looking for an easy place to store their recipes or to search 
for recipes can use this website. 

## Features
 
### Existing Features
- Multiple page layout:
    - Home page with all recipes (paginated) and filter functions based on diet/allergens.
    - Single Recipe page with ingredients, directions, etc for a specific recipe (with links to 'Edit Page' or 'Delete function')
    - Edit page to edit a specific recipe through a form
    - Add page to add a recipe through a form
- Contact link in footer of page



### Features Left to Implement
- Search function based on keywords/recipe title/ingredients


## Tech Used

### Some the tech used includes:
- **HTML**, **CSS** and **Javascript**
  - Base languages used to create website
- **Python**
    - for server side processing 
    - Dependencies installed are 
        - flask
        - flask-pymongo
        - dnspython
        - datetime
- [MongoDB](mongodb.com)
    - Online database   
- [Materialize](http://archives.materializecss.com/0.100.2/)
    - We use **Materialize** to give our project a simple, responsive layout
- [JQuery](https://jquery.com)
    - Use **JQuery** for Materialize, logic behind the website and in support of EmailJS
- [EmailJS](email.js.com)
    - We use EmailJS to link up the modal contact form to an actual e-mail address


## Testing
- All code used on the site has been tested to ensure everything is working as expected
    - App.routes were checked on going to the correct destinations  
    - Filtering functionality for recipes was checked with allergens and diet.
    - Delete functionality was checked for specific recipes.
    - Edit functionality was checked for specific recipes.
    - 10 recipes were added through the form on the website to confirm proper adding of recipes.
- Site viewed and tested in the following browsers:
  - Google Chrome
  - Safari
  - Firefox
  - Opera

## Deployment

### Deployment through Cloud9
1. Create a blank workspace in your Cloud9 dashboard.
2. Get all files from github using 'git clone https://github.com/Daanivd/msp3' command in the C9 CLI
3. install Python dependies through !!!!!
3. Open up msp3/app.py and click 'Run'. Click on the link for the running app, click 'open app' to view the website.

### Deployment through Heroku
!!!!

### Deployment through Github.io

## Contributing
[recipes](https://sallysbakingaddiction.com/best-banana-cake/)
[Materialize](https://materializecss.com/)
[MongoDB](https://docs.mongodb.com/manual/tutorial/insert-documents/)

## Credits
Recipes belong to [recipes](https://sallysbakingaddiction.com/best-banana-cake/)

### Media
[meat symbol](https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwj2nZ-HvoviAhWJbFAKHUajABwQjRx6BAgBEAU&url=https%3A%2F%2Fwww.designspiration.net%2Fsave%2F27356255783901%2F&psig=AOvVaw3Wgow-xMzgzeyuj9Bnfrzx&ust=1557389464529574)
[fish symbol](https://pngtree.com/freepng/flat-fish-symbol-icon_664870.html)
[vegetarian symbol](https://www.kisspng.com/png-vegetarian-cuisine-desktop-wallpaper-veggie-burger-5332147/)
[vegan symbol](https://image.shutterstock.com/image-vector/icon-vegan-food-260nw-778394854.jpg)
[allergy icons](http://chittagongit.com/icon/allergy-icon-27.html)

### Information/Data
Recipes belong to [recipes](https://sallysbakingaddiction.com/best-banana-cake/)

### Additional sources
[Query an Array Pymongo](https://docs.mongodb.com/manual/tutorial/query-arrays/)
[Updating Form](https://stackoverflow.com/questions/38355463/flask-pymongo-forms-loading-pymongo-data-into-a-form-for-editing)
[Allergens](https://www.fsai.ie/legislation/food_legislation/food_information/14_allergens.html)
[Pagination](https://scalegrid.io/blog/fast-paging-with-mongodb/)
[Stop submit on Enter](https://www.tjvantoll.com/2013/01/01/enter-should-submit-forms-stop-messing-with-that/)







