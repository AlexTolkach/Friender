from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from .models import Users, Arrangements, Order


class RatingUserForm(forms.Form):
    rating = forms.IntegerField(validators=[
        MinValueValidator(1, message='input rating between 1 and 5'),
        MaxValueValidator(5, message='input rating between 1 and 5')
    ])
    description = forms.CharField(validators=[
        MinLengthValidator(3, message='input more than 3 symbols')
    ])


class RatingEstablishmentForm(forms.Form):
    rating = forms.IntegerField(validators=[
        MinValueValidator(1, message='input rating between 1 and 5'),
        MaxValueValidator(5, message='input rating between 1 and 5')
    ])
    description = forms.CharField(
        widget=forms.Textarea,
        validators=[
            MinLengthValidator(3, message='input more than 3 symbols'),
            MaxLengthValidator(100, message='no more than 100 characters')
        ])


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ('email',)


class BookingEstablishmentForm(forms.ModelForm):
    class Meta:
        model = Arrangements
        fields = ('host', 'guest', 'establishments')


class OrderPayment(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('place', 'price', 'date_order', 'arrangement')
