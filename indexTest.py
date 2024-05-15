# imports
from selenium import webdriver;
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
# set driver
browser = webdriver.Edge()
browser.get('http://127.0.0.1:5500/')
# functions

def test1():
    time.sleep(1)
    elem1=browser.find_element(By.ID,'element-one')
    elem1.click()
    print(elem1.get_attribute('class'))
    
    assert 'box1style' in elem1.get_attribute('class')
    
    print('box 1 jó')
    
def test2():
    time.sleep(1)
    elem2=browser.find_element(By.ID,'element-two')
    
    action=ActionChains(browser)
    action.double_click(elem2)
    action.perform()
    print(elem2.get_attribute('class'))
    
    assert 'box2style' in elem2.get_attribute('class')
   
    print('box 2 jó')
    
    
def test3():
    time.sleep(1)
    elem3 = browser.find_element(By.ID,'element-three')
    
    
    elem3.click()
    assert 'hidden' in elem3.get_attribute('class')
   
    print('box 3 jó')

def test4():
    
    elem4 = browser.find_element(By.ID,'element-four')
    
    elem4.click()
    assert 'color: red' in elem4.get_attribute('style')
 
    print('box 4 jó')

def test5():
    elem5= browser.find_element(By.ID, 'myInput')
    elem5.click()
    action=ActionChains(browser)
    action.key_down('a')
    action.perform()
    
    assert 'inputmezo' in elem5.get_attribute('class')
    
    print('input okés')


test1()
time.sleep(0.1)
test2()
time.sleep(0.1)
test3()
time.sleep(0.1)
test4()
time.sleep(0.1)
test5()