from django.urls import path
from .views import Register_page, Login_page,Logout_page



urlpatterns = [
          path('register/', Register_page, name='register'),
          path('login/', Login_page, name='login'),
          path('logout/', Logout_page, name= 'logout')

]