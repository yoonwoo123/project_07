from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
        # path('', views.index),
        path('', views.index, name="index"),
        path('<int:movie_pk>/', views.detail, name="detail"),
        path('<int:movie_pk>/delete/', views.delete, name="delete"),
        path('<int:movie_pk>/scores/new/', views.scnew, name="scnew"),
        path('<int:movie_pk>/scores/<int:score_pk>/delete/', views.scdel, name="scdel"),
        path('<int:movie_pk>/edit/', views.edit, name="edit"),
        path('<int:pk>/update/', views.update),
    ]