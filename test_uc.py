from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import pytest

link_main = "https://demo.u-system.tech/dicts/ou"

@pytest.fixture()
def browser():
    print("\nStart browser Google Chrome ")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nQuit browser..")
    browser.quit()

    
def test_create_ou(browser):
    browser.get(link_main)
    
    button_create = browser.find_element(By.CSS_SELECTOR, ".el-button.el-button--primary.el-button--default")
    button_create.click()
    time.sleep(3)
    
    buttons_create = browser.find_elements(By.CSS_SELECTOR, ".el-button.el-button--primary.el-button--default")
    print(len(buttons_create))
    
    
    input_name = browser.find_elements(By.CSS_SELECTOR, ".el-input__inner")
    input_name[1].send_keys("Название")
    buttons_create[1].click()
    
    button_create = browser.find_element(By.CSS_SELECTOR, ".el-button.el-button--primary.el-button--default")
    button_create.click()
    time.sleep(3)
    
    
    
    input_name = browser.find_elements(By.CSS_SELECTOR, ".el-input__inner")
    input_name[1].send_keys("Название&Тип")
    
    input_type = browser.find_elements(By.CSS_SELECTOR, ".el-icon.el-select__caret.el-select__icon")
    input_type[0].click()
    
    time.sleep(3)
    input_type[0].click()
    
    input_select = browser.find_element(By.CSS_SELECTOR, "ul.el-scrollbar__view.el-select-dropdown__list> .el-select-dropdown__item:nth-child(1)")
    input_select.click()
    time.sleep(1)
    input_type[0].click()
                                   
    input_select = browser.find_element(By.CSS_SELECTOR, "ul.el-scrollbar__view.el-select-dropdown__list> .el-select-dropdown__item:nth-child(2)")
    input_select.click()
    time.sleep(1)
    input_type[0].click()
                                        
    input_select = browser.find_element(By.CSS_SELECTOR, "ul.el-scrollbar__view.el-select-dropdown__list> .el-select-dropdown__item:nth-child(3)")
    #input_select.click()
    time.sleep(1)
        
    buttons_create[1].click()   
