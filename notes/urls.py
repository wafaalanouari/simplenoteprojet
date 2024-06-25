from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('notes/', views.note_list, name='note_list'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('note/new/', views.note_new, name='note_new'),
    path('note/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),
]
