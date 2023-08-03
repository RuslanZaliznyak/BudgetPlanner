from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField


class UserRegistrationForm(UserCreationForm):
    email = EmailField(
        max_length=100
    )

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'phone_number',
                  'gender')
