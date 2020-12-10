from django import forms
from myblog.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # fields = ['first_name', 'last_name', 'email', 'message'] # individual fields can be included this way
        fields = '__all__'  # includes all the fields from the model

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'})
    }