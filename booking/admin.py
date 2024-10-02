# admin.py
from django.contrib import admin
from .models import Administrator, Client, Appointment, AvailableTime


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'administrator', 'get_scheduled_time')

    def get_scheduled_time(self, obj):
        return obj.available_time.time
    get_scheduled_time.short_description = 'Scheduled Time'


@admin.register(AvailableTime)
class AvailableTimeAdmin(admin.ModelAdmin):
    list_display = ('administrator', 'time', )


class AppointmentInline(admin.TabularInline):
    model = Appointment
    extra = 0  # Number of extra forms to display


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    inlines = [AppointmentInline]
