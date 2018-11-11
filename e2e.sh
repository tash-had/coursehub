#!/bin/bash

nc -z 127.0.0.1 5000
if [ "$?" -gt 0 ]
then
    echo "ERR: You API server isn't running. Start it using PyCharm or by running sh start_server.sh"
    exit 1
else
    echo "LOG: Killing web-app port"
    app_port=`lsof -t -i :4200 -s TCP:LISTEN`
    kill $app_port
    cd coursehub-app/
    echo "LOG: Installing npm"
    npm install
    npm run e2e > e2e/log
    cat e2e/log
fi

