from django.urls import path,include
from application import views

# template urls!

app_name = 'application'

urlpatterns=[

   path('register/',views.register,name='register'),
   path('login/',views.user_login,name='user_login'),
]
