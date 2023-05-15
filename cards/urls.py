from django.urls import path
from cards import views

urlpatterns = [
    path('cards/', views.CardList.as_view()),
    path('cards/<int:pk>', views.CardDetail.as_view()),
]
