# MOVIES REST API WITH DJANGO 

## Installation

1. Install Django REST framework
```
pip install djangorestframework ### install django rest framework
pip freeze ### to check which packages are installed in the Virtual environment
pip install psycopg2 ### module for postgresql connection
```
2. Add 'rest_framework' to your INSTALLED_APPS setting.
   
```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```
3. [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation)

4.[drf-yasg - Yet another Swagger generator](https://github.com/axnsan12/drf-yasg )

4. Send reset password email to your
   
   For this we could also use packages: [django-rest-passwordreset](https://github.com/anexia-it/django-rest-passwordreset) or [django rest authentication](https://django-rest-auth.readthedocs.io/en/latest/)

5. Import .env variables
   ```
   source .env
   ```
