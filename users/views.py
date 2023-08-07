from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView, RedirectView

from .forms import UserRegistrationForm
from .services.emails import send_registration_email
from .utils.token_generator import TokenGenerator


class UserLoginView(LoginView):
    def get_default_redirect_url(self):
        return reverse('dashboard')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('users:user_login')


class UserRegistrationView(CreateView):
    template_name = 'users_auth/registration_form.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()

        send_registration_email(
            request=self.request,
            user_instance=self.object
        )

        return super().form_valid(form)


class ActivateUserView(RedirectView):
    url = reverse_lazy('users:login')

    def get(self, request, uuid64, token, *args, **kwargs):
        try:
            pk = force_str(urlsafe_base64_decode(uuid64))

            current_user = get_user_model().objects.get(pk=pk)
        except (get_user_model().DoesNotExist, TypeError, ValueError):
            return HttpResponse('User does not exist')

        if current_user and TokenGenerator().check_token(current_user, token):
            current_user.is_active = True
            current_user.save()

            login(request, current_user)
            return super().get(request, *args, **kwargs)

        return HttpResponse('Wrong data 2')







