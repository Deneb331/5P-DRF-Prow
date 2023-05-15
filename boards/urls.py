from django.urls import path
from boards import views

urlpatterns = [
    path('boards/', views.BoardList.as_view()),
    path('boards/<int:pk>', views.BoardDetail.as_view()),
]
