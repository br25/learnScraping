from bs4 import BeautifulSoup
import requests
import time

print("which type of data do you find?")
type = input('>')
print("searching data")

def find_jobs():
    url_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35").text
    soup = BeautifulSoup(url_text, "lxml")

    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate (jobs):
        post_date= job.find("span", class_="sim-posted").span.text
        if 'few' in post_date:
            
            company_name = job.find('h3', class_= 'joblist-comp-name').text.replace(' ','')
            skills = job.find("span", class_='srp-skills').text.replace(' ','')
            link_info = job.header.h2.a['href']
            if type not in skills:
                with open(f'C:/Users/S4G59GWS/Desktop/python/posts/{index}.txt', 'w') as f:
                    f.write(f"company Name: {company_name.strip()}")
                    f.write(f"Require Skills: {skills.strip()}")
                    f.write(f"Info: {link_info.strip()}")
                print(f'file saved: {index}')
        
find_jobs()