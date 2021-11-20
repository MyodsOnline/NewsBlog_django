from django import forms

from .models import News


class OrderForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['number', 'title', 'content', 'file', 'category']
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'file': forms.FileInput(),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
