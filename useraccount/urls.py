from .views import RegisterView, LoginView
from django.urls import path
from knox import views as knox_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout')

]
