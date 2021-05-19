# vaccine-signup

I used chrome for this--I assume some change are needed if you use a different browser. 

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

* Unpack it, move it to any of the paths there.

* Try to execute the file via cmd to confirm

** On Mac, I had a permissions issue. Go to Settings=>Security=>General=>Allow chromedriver
** Then retry the command, it should work

* Clone the repo
* go to the folder
* replace the dummy info with yours
* execute `python3 vaccine.py`
* and get yo ass vaccinated!