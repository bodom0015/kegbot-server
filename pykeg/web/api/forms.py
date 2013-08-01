# Copyright 2010 Mike Wakerly <opensource@hoho.com>
#
# This file is part of the Pykeg package of the Kegbot project.
# For more information on Pykeg or Kegbot, see http://kegbot.org/
#
# Pykeg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# Pykeg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pykeg.  If not, see <http://www.gnu.org/licenses/>.

from django import forms

from pykeg.core import models

class DrinkPostForm(forms.Form):
    """Form to handle posts to /tap/<tap_id>/"""
    ticks = forms.IntegerField()
    volume_ml = forms.FloatField(required=False)
    username = forms.RegexField(required=False, max_length=30, regex=r"^[\w-]+$")
    pour_time = forms.IntegerField(required=False)
    now = forms.IntegerField(required=False)
    duration = forms.IntegerField(required=False)
    shout = forms.CharField(required=False)
    tick_time_series = forms.CharField(required=False)

class CancelDrinkForm(forms.Form):
    """Form to handled posts to /cancel-drink/"""
    id = forms.IntegerField()
    spilled = forms.BooleanField(required=False)

class ThermoPostForm(forms.Form):
    """Handles posting new temperature sensor readings."""
    temp_c = forms.FloatField()
    when = forms.IntegerField(required=False)
    now = forms.IntegerField(required=False)

class CreateKegTapForm(forms.ModelForm):
    class Meta:
        model = models.KegTap
        fields = ('name', 'meter_name', 'relay_name', 'ml_per_tick', 'description')

class CalibrateTapForm(forms.Form):
    ml_per_tick = forms.FloatField()

class TapSpillForm(forms.Form):
    volume_ml = forms.FloatField()

class PhotoForm(forms.Form):
    photo = forms.ImageField()
    time = forms.CharField(required=False)

class DebugLogForm(forms.Form):
    message = forms.CharField()
    client_name = forms.CharField(required=False)

class RegisterForm(forms.Form):
    username = forms.RegexField(max_length=30, regex=r"^[\w-]+$")
    email = forms.EmailField()
    password = forms.CharField()
    photo = forms.ImageField(required=False)

class AssignTokenForm(forms.Form):
    username = forms.RegexField(max_length=30, regex=r"^[\w-]+$")
