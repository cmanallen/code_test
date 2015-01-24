###Code Test
---
*Written in Python 3 and ReactJS.*

####Installation and Requirements

On a Mac?  Try using `pyenv` to set a local environment (pyenv local 3.4.1).  You'll need to `brew install` pyenv and then install the appropriate `python-version` with `pyenv`.

Linux installations should default to Python 3.  If you're runnig an LTS, try installing the python3 package and running all files with the `python3` command.

Create a virtual environment `pyvenv env_name` and `pip install -r requirements.txt`.

####Running the api

* In your environment, `./manage.py runserver --settings=financier.settings.base`.
* On the command line: (linux) chromium --disable-web-security or whatever you have aliased as your browser.
	* Mac users: it's easier to install the Chrome extension "Allow-Control-Allow-Origin"
* Open `index.html` in the `api` folder in your Chrome browser.

####Tasks

Folders are loosely named after the task they're associated with:

* Task 1: `counter` function in `word_count` module.
* Task 2: `financier` is the RESTful API Backend.
* Task 3: `api/index.html` is the consumer.
* Task 4: ajax form submission in `api/index.html` 

####Notes

* I naively round to keep things simple.
* Because we're dealing with Floats, Javascript will routinely make up decimals.
	* Solution is to wrap parseInt() around everything.
* DOM doesn't automatically update with React because of time constraints.  Refresh the page to see new payments added.