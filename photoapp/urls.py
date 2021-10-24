from django.urls import path
from photoapp.views import home_page, redirect_home, detailed_view, create_post


urlpatterns = [
    path('', redirect_home),
    path('home/', home_page),
    path('create/', create_post),
    path('photos/<int:id>/', detailed_view)
]