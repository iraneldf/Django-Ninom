#!/bin/sh

PIDFILE=/var/www/atlas/catalogos/ninom/run/ninom.pid

case $1 in 
start)
NAME="ninom"
DJANGODIR=/var/www/atlas/catalogos/ninom/
SOCKFILE=/var/www/atlas/catalogos/ninom/run/gunicorn.sock
USER=root
GROUP=root
NUM_WORKERS=1
DJANGO_SETTINGS_MODULE=Ninom.settings
DJANGO_WSGI_MODULE=Ninom.wsgi
echo "Starting $NAME as `whoami`"
cd $DJANGODIR
source /var/www/atlas/catalogos/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
# Start your Django Unicorn# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
/var/www/atlas/catalogos/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--bind=unix:$SOCKFILE \
--log-level=debug \
--log-file=- \
--pid=$PIDFILE &
;;
stop)
kill -9 $(cat $PIDFILE)
rm $PIDFILE
;;
restart)
/etc/init.d/ninom.sh stop
/etc/init.d/ninom.sh start
;;

esac

exit 0
