from django.shortcuts import render

from django.http import HttpResponse
import datetime

friends = {
    'Max': [34, 'ma@mail.ru'],
    'Grigory': [32, 'grigory@mail.ru'],
    'Anna': [30, 'ann@mail.ru'],
    'Kate': [29, 'kate@gmail.com']
}

establishments = ['Butter bro', 'Terra', 'Golden Cafe', 'Depo']


# функция представления (вьюшка)
def main_page(request):
    return render(request, 'main.html')


def please_arrangements(request):
    context = {
        "establishments": establishments,
    }
    return render(request, 'establishments.html', context=context)


def all_friends(request):
    context = {
        "friends": friends,
    }
    return render(request, 'friends.html', context=context)


def rating_page(request):
    return render(request, 'rating.html')

