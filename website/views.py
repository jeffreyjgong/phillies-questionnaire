from flask import Blueprint, render_template
import os

views = Blueprint('views', __name__)

PICTURE_FOLDER = os.path.join('static', 'images')

@views.route('/')
def home():
   full_filename = os.path.join(PICTURE_FOLDER, 'test.png')
   return render_template("home.html", image = full_filename)