from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
import datetime

# friends = {
#     'Max': [34, 'ma@mail.ru'],
#     'Grigory': [32, 'grigory@mail.ru'],
#     'Anna': [30, 'ann@mail.ru'],
#     'Kate': [29, 'kate@gmail.com']
# }

# establishments = ['Butter bro', 'Terra', 'Golden Cafe', 'Depo']


# функция представления (вьюшка)
def main_page(request):
    return render(request, 'main.html')


def please_arrangements(request):
    context = {
        "establishments": Establishments.objects.all(),
    }
    return render(request, 'establishments.html', context=context)


def all_friends(request):
    context = {
        "friends": Users.objects.all().prefetch_related('hobbies_set', 'userrating_set'),
    }
    return render(request, 'friends.html', context=context)


def rating_page(request):
    return render(request, 'rating.html')


def form_establishment_rating(request, **kwargs):
    establishment_id = int(kwargs['id'])
    if request.method == 'POST':
        form = RatingEstablishmentForm(request.POST)
        if form.is_valid():
            EstablishmentsRating.objects.create(
                establishment_id=establishment_id,
                rating=request.POST['rating'],
                description=request.POST['description']
            )
            return redirect('establishments')
    else:
        form = RatingEstablishmentForm()
    context = {
        'form': form
    }
    return render(request, 'form_establishment_rating.html', context=context)


def user_form_rating(request, **kwargs):
    user_id = int(kwargs['id'])
    if request.method == 'POST':
        form = RatingUserForm(request.POST)
        if form.is_valid():
            UserRating.objects.create(
                user_id=user_id,
                rating=request.POST['rating'],
                description=request.POST['description']
            )
            return redirect('friends')
    else:
        RatingUserForm()
    context = {
        'user': Users.objects.get(id=user_id)
    }
    return render(request, 'form_user_rating.html', context=context)


def create_user(request):
    context = {}
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('friends')
    else:
        form = CreateUserForm()
        context['form'] = form
    return render(request, 'form_create_user.html', context=context)


def booking_establishment_form(request):
    context = {}
    if request.method == 'POST':
        form = BookingEstablishmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = BookingEstablishmentForm(request.POST)
        context['form'] = form
    return render(request, 'form_booking_establishment.html', context=context)

