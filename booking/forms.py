# forms.py
from django import forms
from .models import AvailableTime


class AppointmentForm(forms.Form):
    client_name = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    client_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    available_time = forms.ModelChoiceField(
        queryset=AvailableTime.objects.all(), empty_label=None)

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['available_time'].widget = forms.Select(
            choices=self.get_available_times())

    def get_available_times(self):
        available_times = AvailableTime.objects.all()
        return [(time.id, f"{time.administrator.name} -  {time.time.strftime('%d/%m : %H:%M')} ") for time in available_times]
