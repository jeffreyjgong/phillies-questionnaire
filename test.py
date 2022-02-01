import requests 
import lxml.html as lxml
import pandas as pd
import re

url='https://questionnaire-148920.appspot.com/swe/data.html'

page_html = requests.get(url)

contents = lxml.fromstring(page_html.content)

table_rows = contents.xpath('//tr')

#print([len(T) for T in table_rows[:50]])
#print([x[1].text_content() for x in table_rows])
count = 0
print('total count is: ', len(table_rows))

with open('malformed_outputs.txt', 'w') as f_1, open('correct_outputs.txt', 'w') as f_2:
   for t in table_rows:
      #https://regexlib.com/REDetails.aspx?regexp_id=130
      x = re.search(r"^\$?([0-9]{1,3},([0-9]{3},)*[0-9]{3}|[0-9]+)(\.[0-9][0-9])?$", t[1].text_content())
      if not x:
         f_1.write(t[1].text_content() + '\n')
         count+=1
      else: 
         f_2.write(x.group() + '\n')

print('total weird ones: ', count)


# errors
# 1. $ errors (no $, too many $)
