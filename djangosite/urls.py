from django.conf.urls import url
from django.urls import path
from .views import createView, deleteEmp, store, index, updateEmp, updateView, viewEmp

urlpatterns = [
    path('', index),
    path('create/', createView, name='createView'),
    path('store', store, name='store'),
    path('view/<int:pk>', viewEmp, name="viewEmp"),
    path('delete/<int:pk>', deleteEmp, name='deleteEmp'),
    path('update/<int:pk>', updateView, name='updateEmp'),
    path('edit/<int:pk>', updateEmp, name='editEmp')
]
