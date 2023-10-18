from django.urls import path
for . import views

urlpatterns = [
    path('', views.place_list, name='place_list')
]

