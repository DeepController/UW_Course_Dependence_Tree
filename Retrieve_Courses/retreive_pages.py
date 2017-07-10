import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.washington.edu/students/crscat/cse.html'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html5lib')
courses = soup.find_all('a', string=re.compile("CSE"))
for course in courses:
    info = course.previous_sibling
    description = info.text
    prereq = re.search('Prerequisite:(.*?\.[0-9])*.*?\.(?!\b)', description)
    if (prereq):
        print(prereq.group(0))

