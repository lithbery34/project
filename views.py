from django.shortcuts import render
import pyautogui
import time
from selenium import webdriver
import time
# Create your views here.
def index(request):
    #time.sleep(1)
    #pyautogui.click(100,100)
    #time.sleep(1)
    #pyautogui.click(232,254)
    #time.sleep(1)
    #pyautogui.hotkey('ctrl','n')
    a=sel()
    time.sleep(30)
    pyautogui.click(3641,286)
    time.sleep(2)
    pyautogui.typewrite(a[0])
    time.sleep(3)
    pyautogui.click(4125, 331)
    time.sleep(2)
    pyautogui.typewrite(a[1])

    return render(request, "mcv.html")

def sel():
    driver=webdriver.Firefox()
    a = input('enter element ')
    print(a)
    driver.get("https:pricepirates.com/?q="+a)
    amaz=driver.find_element_by_id('td_amazon')
    print(amaz.text)
    ebay = driver.find_element_by_id('td_ebay')
    print(ebay.text)
    tab=[]
    tab.append(amaz.text)
    tab.append(ebay.text)
    if driver.close()==True:
        driver.quit()
    return tab
