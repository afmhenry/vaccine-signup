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
* Replace the dummy info in data.json with yours, make sure to select the right vaccination place, which is saved as a variable in the code for reasons. Make sure to update the path of the file in your code, to match your machine.
* Make it executable(shell script) `chmod u+x vaccine.py` or just execute as normal python file. 
* Execute `./vaccine.py`
* Get yo ass vaccinated!

## Or make it cool
* Set up a cronjob for this. I've been running it for a while without issue on a mac, on ubuntu should be trivial. Unsure about windows. 
* Replace the paths in the config file to match your machine in the example config file
* Run `crontab -e` in terminal
* Paste in the edited config file. It is planned to run at 9am, you can change using this site https://crontab.guru to guide on syntax
* I can suggest testing with a minute schedule, (not submitting mode,), you can check results in log.txt. You should see a start and end time.
* You will probably find that it doesnt work, with the log containing permission issue. You have to give cron access to the filesystem. Do at your own risk: https://blog.bejarano.io/fixing-cron-jobs-in-mojave/
* Then it should work :) Any other debugging can probably be helped by this: https://askubuntu.com/questions/23009/why-crontab-scripts-are-not-working


I want to thank stackoverflow, my incredible google abilities, and shameless lack of python knowledge to complete this feat of ingenuity.