from os import name
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path("board/<int:id>", views.board, name='board'),
    path("board/<int:id>/newCard", views.new_card, name='new card'),
    path("update_card/<int:cardId>/<int:newColumn>", views.update_card, name="update card")
]