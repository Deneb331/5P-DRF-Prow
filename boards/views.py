from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Board
from drow_drfapi.permissions import IsOwnerOrReadOnly


class BoardList(APIView):
    