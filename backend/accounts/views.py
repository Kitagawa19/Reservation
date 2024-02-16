from django.shortcuts import render
from django.contrib.auth import authenticate ,login,logout
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
# Create your views here.

class StudentRegisterView(APIView):
  def post(self,request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = CustomUser.objects.create_user(username=username,password=password)
    return Response("アカウントが作成されました")

class SuperUserRegisterView(APIView):
  def post(self,request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = CustomUser.objects.create_superuser(username=username,password=password)
    return Response("アカウントが作成されました")
  
class StudentLoginView(APIView):
  def post(self,request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username,password=password)
    if user is not None:
      login(request,user)
      return Response("ログインしました")
    else:
      return Response("ログインできませんでした")
    
class SuperUserLoginView(APIView):
  def post(self,request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username,password=password)
    if user is not None:
      login(request,user)
      return Response("ログインしました")
    else:
      return Response("ログインできませんでした")

class UserLogoutView(APIView):
  def post(self,request):
    logout(request)
    return Response("ログアウトしました")