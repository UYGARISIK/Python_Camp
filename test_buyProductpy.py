# Generated by Selenium IDE
from lib2to3.pgen2 import driver
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




class TestTestbuyProductpy():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testbuyProductpy(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.maximize_window
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID,"login_button")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, "#item_4_img_link > .inventory_item_img").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"back-to-products\"]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-fleece-jacket")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
    self.driver.find_element(By.LINK_TEXT, "2").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID,"remove-sauce-labs-backpack")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "checkout")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".checkout_info").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "first-name")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("uygar")
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "last-name")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("isik")
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "postal-code")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("78563")
    self.driver.find_element(By.CSS_SELECTOR, ".checkout_buttons").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "continue")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "finish")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"finish\"]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "back-to-products")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"back-to-products\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "#inventory_container #inventory_container").text == "Sauce Labs Backpack\\\\ncarry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.\\\\n$29.99\\\\nAdd to cart\\\\nSauce Labs Bike Light\\\\nA red light isn\\\'t the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.\\\\n$9.99\\\\nAdd to cart\\\\nSauce Labs Bolt T-Shirt\\\\nGet your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.\\\\n$15.99\\\\nAdd to cart\\\\nSauce Labs Fleece Jacket\\\\nIt\\\'s not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.\\\\n$49.99\\\\nAdd to cart\\\\nSauce Labs Onesie\\\\nRib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won\\\'t unravel.\\\\n$7.99\\\\nAdd to cart\\\\nTest.allTheThings() T-Shirt (Red)\\\\nThis classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton.\\\\n$15.99\\\\nAdd to cart"
    self.driver.find_element(By.CSS_SELECTOR, ".header_label").click()
    self.driver.find_element(By.ID, "react-burger-menu-btn").click()
    self.driver.find_element(By.ID, "logout_sidebar_link").click()
  
