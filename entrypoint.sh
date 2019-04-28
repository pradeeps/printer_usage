rm -rf /Users/susarla/Desktop/DockerAll/todo/todoapp/migrations
rm /Users/susarla/Desktop/DockerAll/todo/db.sqlite3

python manage.py makemigrations
python manage.py makemigrations todoapp
python manage.py migrate
python manage.py createsuperuser --username pradeep --email pradeep@pradeeps.org
python manage.py loaddata todoapp
python manage.py runserver
