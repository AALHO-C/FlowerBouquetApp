# FlowerBouquetApp


my_project/
├── manage.py
├── config/
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── __init__.py
│   ├── app1/
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── static/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   └── app2/
│       ├── migrations/
│       ├── templates/
│       ├── static/
│       ├── models.py
│       ├── views.py
│       └── urls.py
├── static/
├── media/
├── templates/
│   ├── base.html
│   └── <app-specific templates>
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
└── .env
