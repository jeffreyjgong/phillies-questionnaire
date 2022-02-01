import requests
import lxml.html as lxml
import re

def get_salaries(url):
   page_html = requests.get(url)
   contents = lxml.fromstring(page_html.content)
   table_rows = contents.xpath('//tr')
   
   # Now, we have the table rows of the salary data

   year = str(table_rows[0][2].text_content())
   salaries = []

   for t in table_rows:
      correct_output = re.search(r"^\$*?([0-9]{1,3},([0-9]{3},)*[0-9]{3}|[0-9]+)(\.[0-9][0-9])?$", t[1].text_content())

      if correct_output:
         salaries.append(int(correct_output.group().replace('$', '').replace(',', '')))
   
   salaries.sort(reverse=True)
   
   sum = 0
   num = min(125, len(salaries))
   for i in range(0, num):
      sum += salaries[i]

   # https://www.kite.com/python/answers/how-to-format-currency-in-python
   average = round(sum/num, 2)
   average_salary = "${:,.2f}".format(average)

   return (year, average_salary, salaries)