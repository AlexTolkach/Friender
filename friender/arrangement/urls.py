from django.urls import path
from .views import *

urlpatterns = [
    path('main', main_page, name='main'),
    path('friends', all_friends, name='friends'),
    path('establishments', please_arrangements, name='establishments'),
    path('rating', rating_page, name='rating'),
]
