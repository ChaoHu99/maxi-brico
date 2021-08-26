% prepara el repositorio para su despliegue. 
release: sh -c 'cd backend && python manage.py migrate'
% especifica el comando para lanzar Decide
web: sh -c 'cd backend && gunicorn backend.wsgi --log-file -'
