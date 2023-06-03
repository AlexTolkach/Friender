from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('main', main_page, name='main'),
    path('friends/', all_friends, name='friends'),
    path('establishments', PleaseListView.as_view(), name='establishments'),
    path('rating', RatingTemplateView.as_view(), name='rating'),
    path('booking_establishment', BookingEstablishmentForm.as_view(), name='booking_establishment_form'),
    re_path(r'^rating_user/(?P<id>[0-9]+)$', user_form_rating, name='user_form_rating'),
    re_path(r'^rating_establishment/(?P<id>[0-9]+)$', form_establishment_rating, name='form_establishment_rating'),
    path('create_user', create_user, name='create_user'),
    path('order_payment', order_payment, name='order_payment'),
    path('create_place', EstablishmentsCreateView.as_view(), name='create_place'),
    path("delete_user_rating/<int:pk>/delete/", UserRatingDeleteView.as_view(), name="delete_user_rating"),
]
