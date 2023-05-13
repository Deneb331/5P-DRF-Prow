from django.urls import path
from workspaces import views

urlpatterns = [
    path('workspaces/', views.WorkspaceList.as_view()),
]
