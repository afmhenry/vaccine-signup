# vaccine-signup

I used chrome for this--I assume some change are needed if you use a different browser. 


## To Setup

* Have python3

* Install selenium and time and json

`pip install selenium`


* Now we need browser drivers. I used this guide but will try to boil it down

https://www.selenium.dev/documentation/en/webdriver/driver_requirements/

* Download the google chrome driver, of the appropriate version you are running:

https://sites.google.com/a/chromium.org/chromedriver/downloads

* Go to terminal, echo your path, get some paths like this (separated by colon)

```
echo $PATH
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

* Unpack the driver, move it to any of the folders paths listed above.

* Try to execute the file via cmd to confirm: `./chromedriver` 
	* On Mac, I had a permissions issue. Go to Settings=>Security=>General=>Allow chromedriver
	* Then retry the command, it should work



* Clone the repo
* Go to the folder
* Replace the dummy info with yours, make sure to select the right vaccination place
* Execute `python3 vaccine.py`
* Get yo ass vaccinated!

I want to thank stackoverflow, my incredible google abilities, and shameless lack of python knowledge to complete this feat of ingenuity.