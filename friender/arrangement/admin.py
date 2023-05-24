from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.display(description='фото')
def get_html_photo(objects):
    if objects.photo:
        return mark_safe(f'<img src={objects.photo.url} width=50>')


get_html_photo.short_descriptions = 'фото'


class HobbiesInline(admin.StackedInline):
    model = Hobbies.user.through
    extra = 1


@admin.action(description='Change city')
def change_city(modeladmin, request, queryset):
    queryset.update(city='Brest')


class UsersAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('photo', 'name', 'surname', 'age', 'sex')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('email', 'city'),
        }),
    )
    list_display = (get_html_photo, 'name', 'surname', 'age', 'sex', 'city')
    list_display_links = ['name', 'surname']
    ordering = ['name']
    search_fields = ['age', 'sex', 'city']
    list_per_page = 10
    save_on_top = True
    list_filter = ['age', 'sex', 'city']
    inlines = [
        HobbiesInline
    ]
    actions = [
        change_city
    ]


class UserRatingAdmin(admin.ModelAdmin):
    pass


class HobbiesAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_display_links = ['name']
    ordering = ['name']
    list_per_page = 10
    save_on_top = True
    list_filter = ['name', 'category']


class EstablishmentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'address', 'phone', get_html_photo]
    list_display_links = ['name']
    ordering = ['name']
    list_per_page = 10
    save_on_top = True
    list_filter = ['name', 'category']


class EstablishmentsRatingAdmin(admin.ModelAdmin):
    pass


class PassportAdmin(admin.ModelAdmin):
    pass


class ArrangementsAdmin(admin.ModelAdmin):
    pass


class HostAdmin(admin.ModelAdmin):
    pass


class GuestAdmin(admin.ModelAdmin):
    pass




admin.site.register(Users, UsersAdmin)
admin.site.register(UserRating, UserRatingAdmin)
admin.site.register(Hobbies, HobbiesAdmin)
admin.site.register(Establishments, EstablishmentsAdmin)
admin.site.register(EstablishmentsRating, EstablishmentsRatingAdmin)
admin.site.register(Passport, PassportAdmin)
admin.site.register(Arrangements, ArrangementsAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Order)

# Register your models here.
