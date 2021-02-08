#!/bin/bash

if psql -lqt | cut -d \| -f 1 | grep -qw mpharma-diagnosis; then
    # database exists...start sever
    cd diagnosis_api;

    # run migration
    python manage.py migrate;

    # run gunicorn (http server)
    gunicorn diagnosis_api.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3;
else
    printf "Couldn't establish connection to postgres server or database 'mpharma-diagnosis' doesn't exist.\n";
    printf "waiting for 10 seconds...\n";
    sleep 10;
    exit 1;
fi
