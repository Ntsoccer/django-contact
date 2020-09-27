from django.urls import path, include
from . import views

app_name = 'contactapp'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('contact',views.ContactFormView.as_view(),name='contact')
]
