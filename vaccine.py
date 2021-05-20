#!/usr/bin/env python3
import time
from datetime import datetime
import json
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from collections import OrderedDict

#radio selection of vaccine site, number 1-9 as string
area = "6"
wait_time = .5

print("Starting now: "+str(datetime.now()))

with open('/Users/manebjaelke/Documents/vaccine-signup/data.json') as json_file:
    answer_dict = json.load(json_file,object_pairs_hook=OrderedDict)

    with Chrome() as driver:
        #url for the form
        driver.get("https://www.survey-xact.dk/LinkCollector?key=JPH8ZGHNL21N")

        #hacky time delays to avoid async messiness. 
        time.sleep(1)
        firstNext = driver.find_element_by_class_name("next-area")
        firstNext.click()
        time.sleep(wait_time)

        #iterate over the first pages and put in values.
        for entry in answer_dict:
            input_field = driver.find_element_by_name(entry['type'])
            next_button = driver.find_element_by_class_name("next-area")

            time.sleep(wait_time)
            input_field.send_keys(entry['value'])
            time.sleep(wait_time)
            next_button.click()
            time.sleep(wait_time)

        #radio needs weird stuff, so had to do seperate. 
        input_field = driver.find_element_by_css_selector("input[type='radio'][data-choice-label-value='"+area+"']")
        input_field.find_element_by_xpath('..').click()
        next_button = driver.find_element_by_class_name("next-area")
        next_button.click()
        time.sleep(wait_time)

        #data acceptance confirmation page
        next_button = driver.find_element_by_class_name("next-area")
        next_button.click()
        time.sleep(wait_time)

        #submission page
        #Commented so you don't submit without testing first
        #next_button = driver.find_element_by_class_name("next-area")
        #next_button.click()
        time.sleep(10)
print("Ending now: "+str(datetime.now())+"\n")


