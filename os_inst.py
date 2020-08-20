'''The project its a selenium based script that ains to find all photos from someone trough the internet using google'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException)
from urllib.request import urlopen, Request, urlretrieve
import sys
import warnings
from bs4 import BeautifulSoup
import shutil
import wget
import requests
import  time
import urllib.parse
#import driver

print(" ___                ___     ___ ")
print("  |  ._   _ _|_  _.  |  |\ | |  ")
print(" _|_ | | _>  |_ (_| _|_ | \| | ")



driver = webdriver.Firefox(executable_path ="C:\\Users\\E3\\Desktop\\cd\\geckodriver.exe")
slist = list()
class itim():
    fol_dict = dict

    def __init__(self):
        pass




    def get_start(self): # simple get the driver to instagram page
        driver.get("https://www.instagram.com/")
        driver.implicitly_wait(30)
        driver.maximize_window()

    def get_login(self):
        login_by_fb = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[5]/button/span[2]')
        login_by_fb.click()
        driver.implicitly_wait(5)
        #username and password fb
        us_in = input("email:")
        usr_fb = us_in
        psw_in = input("password:")
        psw_fb = psw_in
        # get your crendetials and use it to log in fb and trough that log in instagram
        usrfb = driver.find_element_by_xpath('//*[@id="email"]')
        usrfb.send_keys(usr_fb)
        pswfb = driver.find_element_by_xpath('//*[@id="pass"]')
        pswfb.send_keys(psw_fb)
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

    def check_banner(self): # get over the pop up when u log in
        driver.implicitly_wait(10)

        try:  # Try both ways to get over the pop up
            f1form = driver.find_element_by_xpath("/html/body/div[3]/div").is_displayed()
            if f1form is True:
                driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]").click()
            else:
                driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()

      #  / html / body / div[4] / div / div / div / div[3] / button[2]
        except:
            f2form = driver.find_element_by_xpath("/html/body/div[4]/div").is_displayed()
            if f2form is True:
                driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]").click()
            else:
                driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()

    def got_to_profile(self): # go to your profile in Instagram
        prf_link = driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')
        prf_link.click()


    def wait_action(self):
        self.url = driver.current_url
        while True:
            get_nurl = driver.current_url
            driver.implicitly_wait(5)
            if get_nurl != self.url :
                break

    def get_links_in(self): #Get all links in instagram photos and append to slist
        driver.implicitly_wait(3)


        source = driver.page_source
        soup = BeautifulSoup(source, 'html.parser')
        image_elements = driver.find_elements_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div/div//img")  # Xpath to the images

        for image in image_elements:  # Get all image link and append to  slist
            img_src = image.get_attribute("src")
            slist.append(img_src)

        return slist
    def save_l_in(self):#save all links to a notepad
        self.get_links_in()
        f = open("in_links.txt", "a", encoding="utf-8")
        for word in slist:
            f.write(word)
            f.write('\n')
        f.close()
        print("ALL LINKS HAVE BEEN SCRAPED , PLEASE MOVE TO NEXT STEP")

numb_a_sel = list()
class gg_in():

    def __init__(self):

        pass

    def get_start(self):  # simple get the driver to instagram page
        pass

    def sel_img(self , urls):  # that the url from  a list made by the first script
        driver.get("https://www.google.com/searchbyimage?image_url="+urls)
        driver.implicitly_wait(5)
        driver.maximize_window()


    def soup_fs(self):  # that do most of the program it scrape  google search and it append everything to the list
        self.my_results = list()  # LIST WHERE ALL LINKS
        urll = driver.current_url

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}  # headers
        source = requests.get(urll, headers=headers).text  # url source

        # BeautifulSoup
        soup = BeautifulSoup(source, 'lxml')
        search_div = soup.find_all(class_='rc')  # find all divs tha contains search result
        for result in search_div:  # loop result list
            self.my_results.append('Title: %s' % result.h3.string)  # geting h3
            self.my_results.append('.........')
            self.my_results.append('Url: %s' % result.a.get('href'))  # geting a.href
            self.my_results.append('.........')
            self.my_results.append('Description: %s' % result.find(class_='st').text)  # description
            self.my_results.append('\n###############\n')
        print(self.my_results)
        return self.my_results

    def save_list(self):  # It runs the method SOUP_FS and then save all links in a file
        self.soup_fs()
        f = open("insta_int.txt", "a", encoding="utf-8")
        for word in self.my_results:
            f.write(word)
        f.close()


ab = itim()
ab.get_start()
ab.get_login()
ab.check_banner()
ab.wait_action()
ab.save_l_in()


ab1 = gg_in()
ab1.get_start()


int_f = open("in_links.txt", "r")
int_r = int_f.read()
print(slist)

for item in slist:
    my_url = urllib.parse.quote(item)
    ab1.sel_img(my_url)
    driver.implicitly_wait(5)
    ab1.save_list()

print("The script Scraped all links , the insta_int.txt file was generated")
print("Thank you ")

