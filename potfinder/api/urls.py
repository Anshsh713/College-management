from django.urls import path
from .views import login_view, logout_view, current_user_view,signup_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('current_user/', current_user_view, name='current_user'),
    path('signup/', signup_view)
]

