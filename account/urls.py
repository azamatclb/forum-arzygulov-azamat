from django.urls import path

from .views import login_view, logout_view, RegisterView, ProfileView

app_name = 'account'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile_view'),
]
