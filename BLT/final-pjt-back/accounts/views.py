import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserDetailsSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

@api_view(['GET','PUT', 'DELETE'])
def update(request, username):    
    user = get_object_or_404(User, username=username)

    #수정입력폼 (페이지) #회원정보 읽기
    if request.method == 'GET': 
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'DELETE': # 회원탈퇴...
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT': #회원정보 수정
        print("in put")
        print(request.user)
        print(user.username)
        serializer = UserSerializer(user, data=request.data, partial=True)
        print(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(status=status.HTTP_403_FORBIDDEN)
        