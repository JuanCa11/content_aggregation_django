# Content Aggregation Website

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/JuanCa11/content_aggregation_django.git
$ cd content_aggregation_django
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Make migrations and migrate models for website application:

```sh
(env)$ python manage.py makemigrations website
(env)$ python manage.py migrate
```

Run scripts to create Sites and News rows:

```sh
(env)$ python manage.py create_sites
(env)$ python manage.py fetch_news
```

Note that you will need to add `fetch_news` to contrab tab to run it periodically

Now you can run server:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/website/`.