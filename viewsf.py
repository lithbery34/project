from django.shortcuts import render
import pyautogui
import time
from selenium import webdriver
import time
# Create your views here.
def index(request):
    a=sel()
    #time.sleep(5)
    #pyautogui.click(3641, 286)
    #time.sleep(2)
    #pyautogui.typewrite(a)
    return render(request, "mcv.php")
def sel():
    driver=webdriver.Firefox()
    a=input('Enter elemnt')
    driver.get('https:flipkart.com/search?q='+a)
    info=driver.find_element_by_class_name('_3O0U0u')
    print(info.text)
    return info.text