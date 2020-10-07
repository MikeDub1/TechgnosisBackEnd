# Welcome to the back end of Chaos!

In order to test this environment, please make sure that you always pull from this repository before attempting to run the APIs.

## Setup
In order to set up these APIs, you must do the following:

1. Install [python3](https://www.python.org/downloads/)
2. Either install [PyCharm](https://www.jetbrains.com/pycharm/) or install pip
3. Set up Flask:
  3. If you are using Pycharm, read [this](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html) to set up a virtual environment
      on an existing project in PyCharm.
  3. If you are using pip:
      3. run `python3 -m pip install --user virtualenv` on Linux or `py -m pip install --user virtualenv` on Windows
      3. then run `python3 -m venv /path/to/the/local/repository`
4. After installing a virtual environment on either PyCharm or pip, navigate to your local repository using a terminal and run 'source bin/activate'
to activate the virtual environment.
5. On pip, run `pip install flask` in order to install flask.
6. On PyCharm, go to `File->Settings->Project interpreter` and click the green `+` button. Type `Flask` in the search bar and install the package.
7. export the variables FLASK_APP AND FLASK_ENV by running `export FLASK_APP=path/to/root/python/file` and `export FLASK_ENV=development`. replace `export` with `set` if you are on windows.
Note: FLASK_ENV determines the environment that you will be running the API. Setting it to  `development` will cause the python interpreter to output debug information to the client.
DO NOT, I REPEAT, DO NOT RUN FLASK ON DEVELOPMENT MODE IF YOU ARE DEPLOYING THE SERVER AS THIS WILL ALLOW EVERYONE TO SEE DEBUG INFORMATION FROM THE SERVER!

Other than that, happy coding!!!




