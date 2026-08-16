from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.get_all_todo, name='all'),
    path('add/', view=views.add_todo, name='add_todo'),
    path('remove/', view=views.remove_todo, name='remove_todo'),
    path('edit/', view=views.edit_todo, name='edit_todo'),
]