from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('main', main_page, name='main'),
    path('friends', all_friends, name='friends'),
    path('establishments', please_arrangements, name='establishments'),
    path('rating', rating_page, name='rating'),
    re_path(r'^rating_user/(?P<id>[0-9]+)$', user_form_rating, name='user_form_rating'),
    re_path(r'^rating_establishment/(?P<id>[0-9]+)$', form_establishment_rating, name='form_establishment_rating'),
    path('create_user', create_user, name='create_user'),
    path('booking_establishment', booking_establishment_form, name='booking_establishment_form'),
    path('order_payment', order_payment, name='order_payment')
]
