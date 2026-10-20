from django import forms
from .models import Feature

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ['name', 'description']

        labels = {
            'name': 'Feature Name',
            'description': 'Description',
        }

        help_texts = {
            'name': 'Enter a short, descriptive name.',
            'description': 'Describe what makes this trail feature special.',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. Waterfall',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe this feature...',
                'rows': 4,
            }),
        }

    def clean_name(self):
        name = self.cleaned_data['name'].strip()

        if len(name) < 2:
            raise forms.ValidationError(
                'Feature name must be at least 2 characters long.'
            )

        return name