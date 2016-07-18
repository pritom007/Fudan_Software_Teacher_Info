#This is a simple program to get th information
#of the Software school teachers' of Fudan University
#information inculdes

#
#website:
#name:
#degicnation:
#email:
#address:
#educational background:

import requests
from bs4 import BeautifulSoup

#takes the url as input
#this url contains the names of the teachers
#here from the href attribute we get the indivudial webite adress

def fudan_software_teacher(url):
    source_code = requests.get(url)
    #plain_text = source_code.text
    soup = BeautifulSoup(source_code.text)
    for link in soup.findAll('a', {'target': '_blank'}):
        href = link.get('href')
        #title = link.string
        #print(href)
        try:
            information_parser(href)
        except:
            print("problem")


#this module takes input of the website url of the teacher
#and gives informations of the teacher as output

def information_parser(url):
    try:
        source_code = requests.get(url)
    except:
        print("error")
    #plain_text = source_code.text
    beautiful_soup = BeautifulSoup(source_code.text)
    name_of_teacher=beautiful_soup.find('div', {'class': 't-n ui-btmline'}).string
    print('Name:',name_of_teacher)
    print('Website:',url)
    try:
        for info in beautiful_soup.find_all('div',{'class': 't-inf ui-btmline'}):
            print(info.string)
    except:
        print("error")

    print("\n")

#calling the module
fudan_software_teacher('http://www.mse.fudan.edu.cn/content/article/RevealItselfByCategoryArticle/0000000010j/bdghkqugu0n.html')
