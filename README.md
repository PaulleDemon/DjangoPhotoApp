# DjangoPhotoApp
Django photo app for studying deployment:

### Follow the instruction from here:
    [Deploying Django to AWS using ElasticBeanstalk (EB):](https://github.com/PaulleDemon/AWS-deployment/blob/master/deploying_django.md)
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
