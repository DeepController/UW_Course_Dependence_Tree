#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

URL = 'https://www.washington.edu/students/crscat/'

HEADERS = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
}

# Return the content of the response from the given URL
def getHtml(url, header = HEADERS):
    page = requests.get(url, headers = header)
    return page.text
	
def main():
	raw_content = getHtml(URL)
	soup = BeautifulSoup(raw_content, "lxml")
	course_link_dict = {}
	for tag in soup.find_all("a", href=re.compile("^[A-Za-z0-9]+\.html")):
		data = tag.string
		acronym = data[data.rfind("(") + 1:data.rfind(")")]
		if not re.match('^[A-Z\s&]+$', acronym):
			continue
		acronym = acronym.replace(u'\xa0', ' ')
		value = "https://www.washington.edu/students/crscat/" + tag['href']
		course_link_dict[acronym] = value
	for link in course_link_dict:
		print(link + " : " + course_link_dict[link])



#### Test for missing item ####################################################################### 
	# l = []
	# for tag in soup.find_all("a", href=re.compile("^[A-Za-z0-9]+\.html")):
	# 	data = tag.string
	# 	acronym = data[data.rfind("(") + 1:data.rfind(")")]
	# 	if not re.match('^[A-Z\s&]+$', acronym):
	# 		continue
	#	value = tag['href']
	#	l.append(value)
	#	course_link_dict[acronym] = value
	# for link in course_link_dict:
	# 	print(link + " : " + course_link_dict[link])
	# print(len(course_link_dict.values()))

	# for tag in soup.find_all("a", href=re.compile("^[A-Za-z0-9]+\.html")):
	# 	s = tag['href']
	# 	if s not in l:
	# 		print(tag['href'])


if __name__ == '__main__':
	main()


