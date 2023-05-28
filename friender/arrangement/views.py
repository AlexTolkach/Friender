from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.db import transaction
from django.contrib.auth.decorators import login_required, permission_required
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, FormView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission
from django.http import HttpResponse
import datetime

# функция представления (вьюшка)


def main_page(request):
    return render(request, 'main.html')


@login_required(login_url="/admin/login/")
@permission_required("arrangement.view_users", login_url="/admin/login/")
def all_friends(request):
    users = Users.objects.all().prefetch_related('hobbies_set', 'userrating_set').order_by('name')
    paginator = Paginator(users, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'friends': users,
        'page_obj': page_obj,
    }
    return render(request, 'friends.html', context=context)


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
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('friends')
    else:
        form = CreateUserForm()
        context['form'] = form
    return render(request, 'form_create_user.html', context=context)


# def booking_establishment_form(request):
#     context = {}
#     if request.method == 'POST':
#         form = BookingEstablishmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('main')
#     else:
#         form = BookingEstablishmentForm(request.POST)
#         context['form'] = form
#     return render(request, 'form_booking_establishment.html', context=context)


def order_payment(request):
    context = {}
    if request.method == 'POST':
        form = OrderPayment(request.POST)
        context['form'] = form
        if form.is_valid():
            arrangement = (request.POST['arrangement'][0])
            price = int(request.POST['price'])
            host = Host.objects.get(arrangements=arrangement)
            with transaction.atomic():
                if host.max_spent_value >= price:
                    host.max_spent_value -= price
                    host.save()
                    form.save()
                else:
                    raise ValueError('Недостаточно средств')
                return redirect('main')
    else:
        form = OrderPayment(request.POST)
        context['form'] = form
    return render(request, 'form_order_payment.html', context=context)


class PleaseListView(ListView):
    template_name = "establishments.html"
    model = Establishments
    context_object_name = 'establishments'
    paginate_by = 2


class RatingTemplateView(TemplateView):
    template_name = 'rating.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EstablishmentsCreateView(CreateView):
    model = Establishments
    fields = ('name', 'category', 'address', 'phone')
    template_name = "form_create_place.html"
    success_url = reverse_lazy('establishments')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["photo"] = self.request.FILES
    #     return context


class BookingEstablishmentForm(FormView):
    template_name = "form_booking_establishment.html"
    form_class = BookingEstablishmentForm
    success_url = reverse_lazy('establishments')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserRatingDeleteView(DeleteView):
    model = UserRating
    success_url = reverse_lazy("friends")
