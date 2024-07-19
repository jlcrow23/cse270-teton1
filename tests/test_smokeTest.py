# Generated by Selenium IDE
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
from selenium.webdriver.chrome.options import Options

class TestSmokeTest():
  def setup_method(self, method):
    options = Options()
    options.add_argument("--headless=new")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_homePageTest(self):
    self.driver.get("http://127.0.0.1:5500//teton/1.6/index.html")
    self.driver.set_window_size(1509, 949)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-title > h1")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
    assert self.driver.title == "Teton Idaho CoC"
  
  def test_homePageTest2(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/")
    self.driver.set_window_size(1509, 949)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 > h4")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Join Us")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Join Us").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, "nav")
    assert len(elements) > 0
  
  def test_joinPageTest(self):
    self.driver.get("http://127.0.0.1:5500/")
    self.driver.set_window_size(1509, 949)
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) .name").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) .name").click()
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").send_keys("Julie")
    self.driver.find_element(By.NAME, "lname").send_keys("Smith")
    self.driver.find_element(By.NAME, "bizname").send_keys("HappyTails")
    self.driver.find_element(By.NAME, "biztitle").send_keys("Manager")
    self.driver.find_element(By.NAME, "submit").click()
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
  
  def test_directoryPageTest(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/")
    self.driver.set_window_size(1509, 949)
    self.driver.find_element(By.LINK_TEXT, "Directory").click()
    self.driver.find_element(By.ID, "directory-grid").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9)")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
    self.driver.find_element(By.ID, "directory-list").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
  
  def test_adminPageTest(self):
    self.driver.get("http://127.0.0.1:5500/")
    self.driver.set_window_size(1509, 949)
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) .name").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) .name").click()
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "username").send_keys("pickle")
    self.driver.find_element(By.ID, "password").send_keys("funnypic")
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".errorMessage").text == "Invalid username and password."
  
