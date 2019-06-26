#!/usr/bin/env python
import pytest
import time
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    browser.find_element_by_css_selector(".btn-add-to-basket")
