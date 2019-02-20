#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This program will randomly produce a recipe from db.json
"""
__author__ = "tgentry300"


from flask import Flask
from flask import render_template
from tinydb import TinyDB
import random

recipe_database = TinyDB('db.json')
app = Flask(__name__)


def get_a_recipe():
    """gets a random recipe from db.json"""
    return random.choice(list(recipe_database))


@app.route('/')
def show_a_recipe():
    """renders recipe template"""
    random_recipe = get_a_recipe()
    return render_template('recipe.html', name=random_recipe)
