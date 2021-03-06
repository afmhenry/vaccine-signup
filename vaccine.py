#!/usr/bin/env python3
import time
from datetime import datetime
import json
import sys
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from collections import OrderedDict

#radio selection of vaccine site, number 1-9 as string
area = "6"

print("Starting now: "+str(datetime.now()))

#read file from input cmd
with open(sys.argv[1]) as json_file:
    answer_dict = json.load(json_file,object_pairs_hook=OrderedDict)

    with Chrome() as driver:
        #url for the form
        driver.get("https://www.survey-xact.dk/LinkCollector?key=JPH8ZGHNL21N")

        #Less hacky implicit wait so no hardcoded wait time needed. 
        driver.implicitly_wait(15)

        firstNext = driver.find_element_by_class_name("next-area")
        firstNext.click()

        #iterate over the first pages and put in values.
        for entry in answer_dict:
            input_field = driver.find_element_by_name(entry['type'])
            next_button = driver.find_element_by_class_name("next-area")
            input_field.send_keys(entry['value'])
            next_button.click()

        #radio needs weird stuff, so had to do seperate. 
        input_field = driver.find_element_by_css_selector("input[type='radio'][data-choice-label-value='"+area+"']")
        input_field.find_element_by_xpath('..').click()
        next_button = driver.find_element_by_class_name("next-area")
        next_button.click()

        #data acceptance confirmation page
        next_button = driver.find_element_by_class_name("next-area")
        next_button.click()

        #submission page
        if(True):#change this to False for TEST mode. it won't submit then.
            next_button = driver.find_element_by_class_name("next-area")
            next_button.click()
            time.sleep(.5)
            result_page = driver.title == "Region Hovedstaden"
            print("True if completed: ", result_page)

print("Ending now: "+str(datetime.now())+"\n")


