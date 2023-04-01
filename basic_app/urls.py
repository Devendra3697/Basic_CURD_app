from django.urls import path
from . import views
# App_name = 'basic_app'
urlpatterns = [
    path('post/<int:pk>/', views.post_details, name='post_details'),
    path('creat_post/', views.creat_post, name = "new"),
    path('post/<int:pk>/edit/', views.update_post, name="edit_post"),
    path('post/<int:pk>/delete/', views.delet_post, name="delete_objet")
    

]
