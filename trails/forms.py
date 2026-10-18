from django import forms
from .models import Location, Trail


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'description', 'region']

    def clean_name(self):
        name = self.cleaned_data['name'].strip()

        if len(name) < 2:
            raise forms.ValidationError(
                'Name must be at least 2 characters long.'
            )

        return name


class TrailForm(forms.ModelForm):
    class Meta:
        model = Trail
        fields = [
            'name',
            'description',
            'distance',
            'duration',
            'difficulty',
            'location',
            'category',
            'features',
        ]

        labels = {
            'name': 'Trail Name',
            'distance': 'Distance (km)',
            'duration': 'Duration (hours)',
            'difficulty': 'Difficulty',
        }

    def clean_distance(self):
        distance = self.cleaned_data['distance']

        if distance <= 0:
            raise forms.ValidationError(
                'Distance must be greater than zero.'
            )

        return distance

    def clean_duration(self):
        duration = self.cleaned_data['duration']

        if duration <= 0:
            raise forms.ValidationError(
                'Duration must be greater than zero.'
            )

        return duration