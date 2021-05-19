import time
import json
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

#radio selection of vaccine site, number 1-9 as string
area = "6"

#personal info
answers = '[\
  { \
    "type": "t50100775",\
    "value": "Test Name"\
  },\
  {\
    "type": "n35965768",\
    "value": "AGE"\
  },\
  {\
    "type": "t50088645",\
    "value": "ADDRESS"\
  },\
  {\
    "type": "t50088674",\
    "value": "CITY"\
  },\
  {\
    "type": "n50088775",\
    "value": "PHONENUM"\
  }\
]'

answer_dict = json.loads(answers)

with Chrome() as driver:
    #url for the form
    driver.get("https://www.survey-xact.dk/LinkCollector?key=JPH8ZGHNL21N")

    #hacky time delays to avoid async messiness. 
    time.sleep(1)
    firstNext = driver.find_element_by_class_name("next-area")
    firstNext.click()
    time.sleep(1)

    #iterate over the first pages and put in values.
    for entry in answer_dict:
        input_field = driver.find_element_by_name(entry['type'])
        next_button = driver.find_element_by_class_name("next-area")
        input_field.send_keys(entry['value'])
        time.sleep(.5)
        next_button.click()
        time.sleep(1)

    #radio needs weird stuff, so had to do seperate. 
    input_field = driver.find_element_by_css_selector("input[type='radio'][data-choice-label-value='"+area+"']")
    input_field.find_element_by_xpath('..').click()
    next_button = driver.find_element_by_class_name("next-area")
    next_button.click()
    time.sleep(1)

    #data acceptance confirmation page
    next_button = driver.find_element_by_class_name("next-area")
    next_button.click()
    time.sleep(1)

    #submission page
    #Commented so you don't submit without testing first
    #next_button = driver.find_element_by_class_name("next-area")
    #next_button.click()
    time.sleep(2)