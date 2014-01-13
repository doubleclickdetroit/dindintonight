# DiNDiN TONiGHT

### Getting Started (This will need to be reconfigured DISREGARD for now)
Ensure that Yeoman, Grunt and Bower are installed.

* First install Yeoman:
    `npm install -g yo`

* Next install Grunt and Bower:
    `npm install -g grunt-cli bower`

* Then install Node and Bower dependencies:
    `npm install && bower install`

* Finally the app is ready to be built:
    `grunt build && grunt server:dist`

### Django Setup

* First install Pip `sudo easy_install pip`
* Next, install virtualenv and virtualenvwrapper `sudo pip install virtualenv` &  `sudo pip install virtualenvwrapper`
* Open up your .bash_profile or .profile (on all recent macs it is the .bash_profile and it is located at ~/.bash_profile), and after your PATH statement, add the following
```
# set where virutal environments will live
export WORKON_HOME=$HOME/.virtualenvs
# ensure all new environments are isolated from the site-packages directory
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'
# use the same directory for virtualenvs as virtualenvwrapper
export PIP_VIRTUALENV_BASE=$WORKON_HOME
# makes pip detect an active virtualenv and install to it
export PIP_RESPECT_VIRTUALENV=true
if [[ -r /usr/local/bin/virtualenvwrapper.sh ]]; then
    source /usr/local/bin/virtualenvwrapper.sh
else
    echo "WARNING: Can't find virtualenvwrapper.sh"
fi
```
* Now make sure you reload the your profile by doing a `source ~/.bash_profile` or `source ~/.profile`
* Open a new terminal window. You should see virtualenvwrapper.sh being run and setting up your .virtualenvs directory.
* Test creating a new virtualenv `mkvirtualenv dindintonight`
* You should see something in the console like
```
New python executable in dindintonight/bin/python
Installing setuptools............done.
Installing pip...............done.
virtualenvwrapper.user_scripts creating /Users/< mac username >/.virtualenvs/dindintonight/bin/predeactivate
virtualenvwrapper.user_scripts creating /Users/< mac username >/.virtualenvs/dindintonight/bin/postdeactivate
virtualenvwrapper.user_scripts creating /Users/< mac username >/.virtualenvs/dindintonight/bin/preactivate
virtualenvwrapper.user_scripts creating /Users/< mac username >/.virtualenvs/dindintonight/bin/postactivate
virtualenvwrapper.user_scripts creating /Users/< mac username >/.virtualenvs/dindintonight/bin/get_env_details
```
* Now after getting it all setup you can now perform a `workon dindintonight` to specify that you want to work on the virtual enviroment for the site. You can perform a `deactivate` when you are finished working on the enviroment.
* Now we need to setup a command in our bash profile to run start our django server and also to install any requirements that may have changed. Open up your .bash_profile or .profile (on all recent macs it is the .bash_profile and it is located at ~/.bash_profile), and at the end of the file, add the following (making sure to change anything that is required below)
```
alias dindintonight='workon dindintonight;export DJANGO_SETTINGS_MODULE=core.settings.local;export STIK_DJANGO_SECRET=buy-some-din-din-tonight-now;cd /PATH/TO/THE/DINDINTONIGHT;pip install -r requirements/local.txt;python manage.py runserver 0.0.0.0:9000;'
```
* Now make sure you reload the your profile by doing a `source ~/.bash_profile` or `source ~/.profile`, once you have done that you can now call anywhere `didintonight` and it will launch your django server and also make sure you are running the latest requirements and librarys

### GRUNT Commands (This will need to be reconfigured DISREGARD for now):
clean:
    `grunt clean`

test specs with Jasmine:
    `grunt test`

build:
    `grunt build`

server for dev:
    `grunt server`

server for dist:
    `grunt build && grunt server:dist`
