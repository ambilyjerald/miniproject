from django.urls import path

from mini_app import views

urlpatterns = [
    path("",views.todo,name='test'),
    path("registration",views.notify,name='test1'),
    path("tables",views.data,name='test2'),
    path("dash",views.dash,name='test3'),

    path('loginpage',views.login_page,name='login')

]
