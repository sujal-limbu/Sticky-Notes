from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list , name = 'note-list'),
    path('Create_list/', views.create_note , name = 'create'),
    path('note_update/<int:id>' , views.note_update , name = 'note-update'),
    path('note_delete/<int:id>' , views.delete_note , name = 'note-delete' )
]
