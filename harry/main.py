#step0:ImportingData
import requests
from bs4 import BeautifulSoup

#InputTheURL
url = "https://www.codewithharry.com"

#Step1:GetTheHTMLWithRequest
content = requests.get(url)
htmlcontent = content.content
#print(htmlcontent)

#step2:ParseTheHTML
soup = BeautifulSoup(htmlcontent, "html.parser")
#print(soup.prettify()) #prettifyingHTMLTag

#Step3:HTMLTreeTraversal
#GetTheTitleOfTheHTMLPage
title = soup.title
#print([title]) #ArrayOfString
#print(type(title)) #TypeofString
#print(title.string) #NavigableString


#GetAllTheParagraphTag
#print(soup.find_all("p"))

#GetFirstOneParagraphTag
#print(soup.find("p"))

#GetClassesOfAnyElementInTheHTMLPage
#print(soup.find("p"), ["class"])

#FindAllTheElementsWithClassLead
#print(soup.find_all("p", class_= "lead"))

#GetTheTextFromTheTags/Soup
#print(soup.find("p").get_text())

#GetAllTheAnchorTagsFromThePage
anchors = soup.find_all('a')
#print(set(anchors)) #setMean{}
all_links = set()

#AnchorTagLinks
#for link in anchors:
#    if(link != "#"):
#        linkText = url +link.get('href')
#        all_links.add(link)
#        print(linkText)

#https://www.codewithharry.com/videos/python-web-scraping-tutorial-in-hindi