import requests 
import lxml.html as lxml
import re

# First, get url of the data
url='https://questionnaire-148920.appspot.com/swe/data.html'

# Perform GET request to get html
page_html = requests.get(url)

# Convert into a doc using lxml
contents = lxml.fromstring(page_html.content)

# Parse for table row elements
table_rows = contents.xpath('//tr')
print('Total rows of salary data: ', len(table_rows))

# Write correct and malformed outputs to separate text files
count = 0

with open('test_outputs\malformed_outputs.txt', 'w') as f_1, open('test_outputs\correct_outputs.txt', 'w') as f_2:
   for t in table_rows:
      #https://regexlib.com/REDetails.aspx?regexp_id=130
      x = re.search(r"^\$?([0-9]{1,3},([0-9]{3},)*[0-9]{3}|[0-9]+)(\.[0-9][0-9])?$", t[1].text_content())
      if not x:
         f_1.write(t[1].text_content() + '\n')
         count+=1
      else: 
         f_2.write(x.group() + '\n')

print('Total malformed: ', count)