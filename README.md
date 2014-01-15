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
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'
export PIP_VIRTUALENV_BASE=$WORKON_HOME
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

What the commands look like broken down and the explanations of what they do

```
sudo ipfw flush;                                                # this will flush out all existing custom firewall rules that may exist in the system firewall
sudo ipfw add 100 fwd 127.0.0.1,8080 tcp from any to any 80 in; # add a firewall rule that will forward anything coming in on port 80 to port 8080
workon dindintonight;                                           # change the virtual enviroment to dindintonight
export DJANGO_SETTINGS_MODULE=core.settings.local;              # export out what the settings file is that we are going to load for the dev server
export STIK_DJANGO_SECRET=buy-some-din-din-tonight-now;         # set the secret key which we use for debugging (this can be anything)
cd /PATH/TO/THE/DINDINTONIGHT;                                  # change directory to the path that the dindintonight git repo is at
pip install -r requirements/local.txt;                          # now install any requirements or update them with any libraries that are required
python manage.py syncdb;                                        # tell django that we want to sync the db so we are working with the latest and greatest
python manage.py runserver 127.0.0.1:8080;                      # now fire up the server and run it on port 8080 (which if we remember will get anything from port 80)
```

What it looks like all together

```
alias dindintonight='sudo ipfw flush;sudo ipfw add 100 fwd 127.0.0.1,8080 tcp from any to any 80 in;workon dindintonight;export DJANGO_SETTINGS_MODULE=core.settings.local;export STIK_DJANGO_SECRET=buy-some-din-din-tonight-now;cd /PATH/TO/THE/DINDINTONIGHT;pip install -r requirements/local.txt;python manage.py syncdb;python manage.py runserver 0.0.0.0:8080;'
```
* Now make sure you reload the your profile by doing a `source ~/.bash_profile` or `source ~/.profile`, once you have done that you can now call anywhere `didintonight` and it will launch your django server and also make sure you are running the latest librarys and also will sync any db changes that are needed

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
