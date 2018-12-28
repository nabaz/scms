# Student Course Management System

This is test app

## Installation
 
- Install [Docker](https://docs.docker.com/docker-for-mac/install/) to successfully run this app.
- create .env file inside ./scms/.env and define these vars
Note: for more updated version take a look at .env.example file
```
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=
DB_HOST=db
DB_HOST_PORT=5432
````

- inside the root dir run

```bash
docker-compose up --build 
```

- migrate db

```
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```

```
navigate to http://0.0.0.0:9001/
```

## Api Endpoints:
```python
^api/courses/$ [name='course-list']
^api/courses\.(?P<format>[a-z0-9]+)/?$ [name='course-list']
^api/courses/(?P<pk>[^/.]+)/$ [name='course-detail']
^api/courses/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='course-detail']
^api/students/$ [name='student-list']
^api/students\.(?P<format>[a-z0-9]+)/?$ [name='student-list']
^api/students/(?P<pk>[^/.]+)/$ [name='student-detail']
^api/students/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='student-detail']
^$ [name='api-root']
^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
rest-auth/ ^password/reset/$ [name='rest_password_reset']
rest-auth/ ^password/reset/confirm/$ [name='rest_password_reset_confirm']
rest-auth/ ^login/$ [name='rest_login']
rest-auth/ ^logout/$ [name='rest_logout']
rest-auth/ ^user/$ [name='rest_user_details']
rest-auth/ ^password/change/$ [name='rest_password_change']
rest-auth/registration/
```

## Create User endpoint (Registration) (Authentication and different permissions)

```
rest-auth/registration/
rest-auth/ ^login/$ [name='rest_login'] # for login
```

## Rate-limitting
each api endpoint is limitted 1000 request per day per user and this can be changed from setting
```
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day', 
        'user': '1000/day' 
    }
}
```

## Running Test

```python
docker-compose run web python manage.py test
```


## TODO

```python
- Add 'is_teached', 'is_student' to rest-auth/registration/
```

