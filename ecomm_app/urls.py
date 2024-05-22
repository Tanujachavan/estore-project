from django.urls import path
from ecomm_app import views

urlpatterns = [
    path('about',views.about),
    path('home',views.home),
    path('edit/<rid>',views.edit),
    path('delete/<x1>/<x2>',views.delete),
    path('myview',views.SimpleView.as_view()),
    path('hello',views.hello),
    path('sweet',views.Sweet)
]