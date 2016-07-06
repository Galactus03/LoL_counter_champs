"""This scipt intends to provide you an easy way to know the counter of a champion, the site used will be http://www.lolcounter.com"""

from bs4 import BeautifulSoup as bs
import requests
import sys

class champion_counter():
    def __init__(self,x):
        self.champion_name=x
        champion_url="http://www.lolcounter.com/champions/"+self.champion_name.strip()
        url_content=requests.get(champion_url)
        if url_content.status_code==200:
            print "champion found"
            self.soup=bs(url_content.content,"lxml")
        elif url_content.status_code==404:
            print "champion not found or site down"
            print "tried "+champion_url+" url"
        else:
            print "some internal error occured, status code :"+str(url_content.statuscode)

    def get_hints(self):
        tips_data=self.soup.find_all("div",class_="tip-block")
        tips=[]
        for i in tips_data:
            parsed_data=str(i.find(class_="_tip")).get_text()
            print parsed_data

#will do stats data later
    def weak_against(self):
        weak_data=self.soup.find("div",class_="weak-block").find_all("div",class_="champ-block")
        for i in weak_data:
            print self.champion_name+" is weaker then these champions :"
            temp_data=filter(None,(str(i.get_text().strip()).split("\n")))
            print "Champion: "+temp_data[0]+", postion : "+temp_data[1]+", upvotes: "+temp_data[2]+", Downvotes: "+temp_data[3]

    def strong_against(self):
        strong_data=self.soup.find("div",class_="strong-block").find_all("div",class_="champ-block")
        print self.champion_name+" is stronger then these champions :"
        for i in strong_data:
            temp_data=filter(None,(str(i.get_text().strip()).split("\n")))
            print "Champion: "+temp_data[0]+", postion : "+temp_data[1]+", upvotes: "+temp_data[2]+", Downvotes: "+temp_data[3]

champion_name=raw_input("Enter the name of champion: ")
champion=champion_counter(champion_name)
data_type=int(raw_input("press 0 for hints,1 for the champion that are stronger,2 for champion that are weaker"))
if data_type==0:
    champion.get_hints()
elif data_type==1:
    champion.weak_against()
elif data_type==2:
    champion.strong_against()
else:
    print "Invalid choice, exiting."
