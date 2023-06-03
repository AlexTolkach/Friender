from django.urls import path
from .views import *

urlpatterns = [
    # path('establishment', EstablishmentListAPIView.as_view()),
    # path('establishment/<int:pk>/', EstablishmentDetailAPIView.as_view()),
    path('establishments', EstablishmentAPIView.as_view()),
    path('establishments/<int:pk>/', EstablishmentAPIView.as_view()),
    path('establishment/<int:pk>/', EstablishmentDetailAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path('user/<int:pk>/', UserAPIView.as_view()),
    # path('user/<int:pk>/', UserDetailAPIView.as_view()),
    path('hobbies', HobbiesAPIView.as_view())

]
EstablishmentDetailAPIView