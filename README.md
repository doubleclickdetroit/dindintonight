# DiNDiN TONiGHT

### Getting Started
Ensure that Yeoman, Grunt and Bower are installed.

* First install Yeoman:
    `npm install -g yo`

* Next install Grunt and Bower:
    `npm install -g grunt-cli bower`

* Then install Node and Bower dependencies:
    `npm install && bower install`

* Finally the app is ready to be built:
    `grunt build && grunt server:dist`

### GRUNT Commands:
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
