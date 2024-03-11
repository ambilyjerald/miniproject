from django.urls import path

from mini_app import views

urlpatterns = [
    path("",views.todo,name='test'),
    path("registration",views.notify,name='test1')

]
