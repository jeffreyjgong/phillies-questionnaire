# Phillies Questionnaire (part b) by Jeffrey Gong

This is a web-app deployed with Flask, which dynamically populates 2 histograms and the average salary of the top 125 highest MLB salaries of the given year using Python, lxml.html, regex, requests, and matplotlib. [Steps to clone and host locally](#steps-to-run-locally), [example of the site](#example-of-the-site), [a quick explanation of some of the code](#quick-explanation-of-some-of-the-code), and [references](#references) can be found below. 

## Steps to Run Locally
1. Make sure you have **Python** and **pip** installed on your machine. 
2. Clone the repo ```git clone https://github.com/jeffreyjgong/phillies-questionnaire.git```
3. cd into the repo ```cd phillies-questionnaire```
4. Install requirements ```pip install -r requirements.txt```
5. Run ```app.py``` with either, ```flask run```, ```python3 -m flask run```, ```python3 app.py```, or some related version of that
6. Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) (zoom out if images aren't side by side correctly)
## Example of the Site
![site_example](https://user-images.githubusercontent.com/82338138/152037604-42b3cb6b-ebb5-440f-a0b7-9d26db5a8bc4.PNG)

## Quick Explanation of Some of the Code
#### Testing the data for malformed outputs ([test.py](https://github.com/jeffreyjgong/phillies-questionnaire/blob/main/tests/test.py))
First, I used a GET request to get the html content of the site and parsed for ```tr``` elements using lxml.html. Then, I used a regex expression that accepted all valid currency values (e.g - $900,000 or 900000 or 900,000) to write all the non-matches to a [text file](https://github.com/jeffreyjgong/phillies-questionnaire/blob/main/test_outputs/malformed_outputs.txt) for inspection. 
The main errors were
1. Too many $ signs
2. 'no salary data' or blank value

I then adapted the regex expression to accept strings that had any number of $ signs at the beginning using a ```*``` wildcard. 

Now that I had a way of parsing through the salary data, I wrote a function to do so ([get_salaries.py](https://github.com/jeffreyjgong/phillies-questionnaire/blob/main/get_salaries.py) and returned the relevant information as a tuple (year, average salary, and salaries array).

#### Creating the Flask web app
Then, I used a Flask web app structure to create 2 histograms and display the average salary of the top 125 highest MLB salaries in a given year ([views,py](https://github.com/jeffreyjgong/phillies-questionnaire/blob/main/website/views.py). 

This site dynamically updates on refresh. 

## References
1. Adapted the regex expression from [https://regexlib.com/REDetails.aspx?regexp_id=130](https://regexlib.com/REDetails.aspx?regexp_id=130)
2. Showing histograms in Flask, [https://stackoverflow.com/questions/50728328/python-how-to-show-matplotlib-in-flask](https://stackoverflow.com/questions/50728328/python-how-to-show-matplotlib-in-flask)
3. render_template with multiple variables, [https://stackoverflow.com/questions/12096522/render-template-with-multiple-variables](https://stackoverflow.com/questions/12096522/render-template-with-multiple-variables)
4. How to format currency in python, [https://www.kite.com/python/answers/how-to-format-currency-in-python](https://www.kite.com/python/answers/how-to-format-currency-in-python)
