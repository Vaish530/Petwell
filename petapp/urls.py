from django.urls import path
from . import views


urlpatterns=[

  path('',views.user_login,name='login'),
  path('home/',views.index,name='index'),
  path('services/',views.services,name='services'),
  path('bowlsparadise/',views.bowlsparadise,name='bowlsparadise'),
  path('training/',views.training,name='training'),
  path('training/mapindex.html',views.mapindex,name='mapindex'),
  path('healthline/',views.healthline,name='healthline'),
  path('healthline/appointment.html',views.appointment,name='appointment'),
  path('chatbot/',views.chatbot,name='chatbot'),
  path('getUserResponse/',views.getUserResponse,name='getUserResponse'),
  
  
  
]
