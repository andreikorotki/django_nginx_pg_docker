from django.urls import path

from web import views

urlpatterns = [
    path('', views.index),
    path('contacts', views.contacts),
    path('status', views.status),
    path('post', views.post),
    path('publications', views.publications),
    path('publications/<int:pub_id>', views.publication),
    path('sendfeedback', views.sendfeedback),
]
