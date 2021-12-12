from django import forms

from .models import Email


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['number', 'date', 'time', 'text', 'file', 'email', 'author']
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control'}),
            'time': TimeInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'file': forms.ClearableFileInput(),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }

        def current_email(self):
            email = self.cleaned_data['email']
            if email:
                return email
