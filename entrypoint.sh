#! /bin/sh

until nc -z hivedb 3306; do
	echo "waiting on db"
	sleep 2
done

sleep 2
python manage.py runserver 0.0.0.0:8000
