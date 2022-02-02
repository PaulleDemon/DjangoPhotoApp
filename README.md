# DjangoPhotoApp
This project is create for the tutotial [Deploying Django to AWS using ElasticBeanstalk (EB)](https://github.com/PaulleDemon/AWS-deployment/blob/master/deploying_django.md)
    
This is a simple photo upload application where users can upload images.
### project structure:
```
.
└── photoproject
    ├── .ebextensions
    │   └── django.config
    ├── photoapp
    │   ├── migrations
    │   ├── admin.py
    │   ├── apps.py
    │   ├── test.py
    │   └── ...
    ├── photoproject
    │   ├── asgi.py
    │   ├── urls.py
    │   ├── settings.py
    │   ├── wsgi.py
    │   └── ...
    ├── manage.py
    └── requirements.py
```
