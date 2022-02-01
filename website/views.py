from flask import Blueprint, render_template
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from get_salaries import get_salaries

views = Blueprint('views', __name__)

PICTURE_FOLDER = os.path.join('static', 'images')
PICTURE_FOLDER_GLOBAL = os.path.join('website', 'static', 'images')

URL = 'https://questionnaire-148920.appspot.com/swe/data.html'

@views.route('/')
def home():
   data = get_salaries(URL)
   create_hists(data[2], data[0], len(data[2]))
   full_filename1 = os.path.join(PICTURE_FOLDER, 'hist1.png')
   full_filename2 = os.path.join(PICTURE_FOLDER, 'hist2.png')
   return render_template("home.html", year = data[0], average_salary = data[1], image_all = full_filename1, image_top = full_filename2)

def create_hists(salaries, year, total_num):
   plt.hist(salaries, bins=20, rwidth=0.9, color="blue", ec = "blue")
   plt.suptitle("Histogram showing " + str(total_num) + " MLB Players' salaries")
   plt.xlabel('Dollar amount in ten millions')
   plt.ylabel('Number of players')
   plt.savefig(os.path.join(PICTURE_FOLDER_GLOBAL, 'hist1.png'))
   plt.clf()
   plt.hist(salaries[0:125], rwidth=0.9, color = "orange", ec = "orange")
   plt.suptitle("Histogram showing the top 125 MLB Players' salaries")
   plt.xlabel('Dollar amount in ten millions')
   plt.ylabel('Number of players')
   plt.savefig(os.path.join(PICTURE_FOLDER_GLOBAL, 'hist2.png'))
   plt.clf()
