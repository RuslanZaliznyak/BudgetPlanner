from django.urls import path
from users.views import UserLoginView, UserLogoutView, UserRegistrationView, ActivateUserView, index_view

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('activate/<uuid:uuid>/<str:token>/', ActivateUserView.as_view(), name='activate_user'),
]