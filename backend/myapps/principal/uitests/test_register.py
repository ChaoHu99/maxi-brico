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

class TestRegister():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_register(self):
    self.driver.get("http://localhost:8080/")
    self.driver.set_window_size(1382, 744)
    self.driver.find_element(By.CSS_SELECTOR, ".logo").click()
    self.driver.find_element(By.CSS_SELECTOR, ".user-icon > .v-responsive__sizer").click()
    self.driver.find_element(By.LINK_TEXT, "Regístrate").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("atest@a.com")
    self.driver.find_element(By.ID, "name").send_keys("a")
    self.driver.find_element(By.ID, "surname").send_keys("a")
    self.driver.find_element(By.ID, "phone").send_keys("612345678")
    self.driver.find_element(By.ID, "password").send_keys("a")
    self.driver.find_element(By.ID, "checkbox").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
  
