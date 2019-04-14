# -*- coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = 'https://www.damai.cn'
id = "14777xxxxxx"
password = "xxxxx"
driver = webdriver.Chrome()
driver.get(url)

def search():	
	#look for the concert 
	lookup = driver.find_element_by_tag_name('input')
	lookup.send_keys("piano")
	lookup.send_keys(Keys.RETURN)
	
	#pick concert 
	place = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[2]/div/div[1]/a')
	place.send_keys(Keys.RETURN)
	sleep(0.5)
	confirm = driver.find_element_by_class_name("buybtn")
	confirm.send_keys(Keys.RETURN)
	
def login():
	
	sleep(0.5)
	driver.switch_to_frame("alibaba-login-box")
	driver.find_element_by_id('fm-login-id').send_keys(id)
	driver.find_element_by_id('fm-login-password').send_keys(password)

	#slide to verify 暂时用不了
	ActionChains(driver).click_and_hold(driver.find_element_by_id('nc_1_n1z')).perform()
	ActionChains(driver).move_by_offset(xoffset=250, yoffset=0).perform()
	for i in range(2):
   		ActionChains(driver).move_by_offset(xoffset=10, yoffset=0).perform()
   		sleep(0.1)
	sleep(0.5)
	ActionChains(driver).release().perform()
	
	click_login = driver.find_element_by_tag_name("button")
	click_login.send_keys(Keys.RETURN)


search()
login()