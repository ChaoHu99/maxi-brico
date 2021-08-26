% prepara el repositorio para su despliegue. 
release: sh -c 'cd backend && python manage.py makemigrations && python manage.py migrate && python manage.py migrate --run-syncdb'
% especifica el comando para lanzar Decide
web: sh -c 'cd backend && gunicorn backend.wsgi --log-file -'
