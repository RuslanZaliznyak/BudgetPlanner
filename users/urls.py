from django.urls import path
from users.views import UserLoginView, UserLogoutView, UserRegistrationView, ActivateUserView, index_view

app_name = 'users'

urlpatterns = [
    path(
        'activate/<str:uuid64>/<str:token>/',
        ActivateUserView.as_view(),
        name='activate'
    )
]