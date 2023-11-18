from flask import Flask, render_template, request, url_for, redirect, g, flash, session
from FoodProduct import FoodProduct, Unit

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('recipe'))

@app.route('/recipe')
def recipe():
    return "Recipe page"


@app.route('/grocerylist')
def groceryList():
    return "Grocery list page"


if __name__ == "__main__":
    app.run()