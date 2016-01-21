__author__ = 'Akhil'
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
import MySQLdb

while True:
    url="http://aqicn.org/city/chennai//us-consulate/"
    render=webdriver.Firefox()
    render.get(url)
    page_soup=BeautifulSoup(render.page_source,'html.parser')


    str1=page_soup.find('div',style='font-size:16px;font-weight:light;;').string

    print "Time/Date/Part of Day:"+str1[11::]
    day=""
    for i in range(11,len(str1)):
        if str1[i]!=" ":
            day+=str1[i]
        else:
            index=i
            break

    time=str1[index+1::]

    print "curr, max, min pmi2.5 aqi : ",
    print page_soup.find('td',id='cur_pm25').string,"  ",page_soup.find('td',id='max_pm25').string,"  ",page_soup.find('td',id='min_pm25').string
    pmi=int(page_soup.find('td',id='cur_pm25').string)

    print "curr, max, min temp : ",
    print page_soup.find('td',id='cur_t').span.string,"  ",page_soup.find('td',id='max_t').span.string,"  ",page_soup.find('td',id='min_t').span.string
    temp=int(page_soup.find('td',id='cur_t').span.string)

    print "curr, max, min pressure : ",
    print page_soup.find('td',id='cur_p').string,"  ",page_soup.find('td',id='max_p').string,"  ",page_soup.find('td',id='min_p').string
    pres=int(page_soup.find('td',id='cur_p').string)

    print "curr, max, min humidity : ",
    print page_soup.find('td',id='cur_h').string,"  ",page_soup.find('td',id='max_h').string,"  ",page_soup.find('td',id='min_h').string
    humi=int(page_soup.find('td',id='cur_h').string)

    print "Initiating upload to database."




    db=MySQLdb.connect("localhost","root","","pollutionlive")
    cursor=db.cursor()
    sql="INSERT INTO chennai(pm,temp,pres,humi,time,day) VALUES('%d','%d','%d','%d','%s','%s')"%(pmi,temp,pres,humi,time,day)
    cursor.execute(sql)
    db.commit()
    db.close()
    print "Database entry successful. Connection closed."
    sleep(3600)


