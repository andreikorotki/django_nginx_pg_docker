
Test project for checking  docker-compose
**Django, Gunicorn, Postgres, NGINX and Gunicorn** 
  
  
for launch perform following commands:  
  
**dev**  

    docker-compose down -v
    docker-compose -f docker-compose.yml up -d --build
    docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
     

then navigate to http://localhost:8000  
  
  
  
**PROD**  

    docker-compose down -v  
    docker-compose -f docker-compose.prod.yml down -v
    docker-compose -f docker-compose.prod.yml build  
    docker-compose -f docker-compose.prod.yml up -v  
    docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

  
then navigate to http://localhost:1337/post

