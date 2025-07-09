from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(                                    
                                    max_length=30,
                                    min_length=3,
                                    required=True,
                                    widget=forms.TextInput()
                                )
    email   =   forms.EmailField(                                      
                                    max_length=60,
                                    min_length=8,
                                    required=True,
                                    widget=forms.EmailInput()
                                )


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Common style and placeholder map
        field_config = {
            'username': 'Enter username *',
            'email': 'Enter email *',
            'password1': 'Enter password *',
            'password2': 'Enter confirm password *'
        }

        for field_name, placeholder in field_config.items():
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control fields',
                'placeholder': placeholder
            })

            # Optional: Remove labels if not needed
            self.fields[field_name].label = ''

        # Remove Django's default password help text
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''