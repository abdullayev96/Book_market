from django.urls import path
from .views import *


urlpatterns = [
          path('', index, name = 'home'),
          path('blog/', Blog_page, name='blog'),
          path('blog/<int:pk>/',Blog_detail, name='blog_detail')
]


