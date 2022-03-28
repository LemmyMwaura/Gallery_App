from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add_image/',views.add_image, name='add-image'),
    path('update_image/<str:pk>',views.update_image, name='update-image'),
    path('delete_image/<str:pk>',views.delete_image, name='delete-image')
]