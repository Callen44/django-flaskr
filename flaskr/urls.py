from django.urls import path

from . import views

app_name = 'flaskr'
urlpatterns = [
    path('',views.index, name='index'),
    path('create/',views.create, name='create'),
    path('<str:pk>/update/',views.update, name = 'update'),
    path('<str:pk>/delete/',views.delete, name = 'delete')
]