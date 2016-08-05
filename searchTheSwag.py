#!/usr/bin/env python
from selenium import webdriver
import loginToSwag

driver = webdriver.Firefox()
driver.get("http://search.swagbucks.com/p/login")

loginToSwag.login(driver)
