Test project for checking
**Django, Gunicorn, Postgres, NGINX in Docker**


for launch perform following commands:

**dev**

`docker-compose down -v
docker-compose -f docker-compose.yml up -d --build
docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput`

navigate to http://localhost:8000


**prod**

`docker-compose down -v`
`docker-compose -f docker-compose.prod.yml down -v`
`docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml up -v
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput`
`

navigate to http://localhost:1337/post


