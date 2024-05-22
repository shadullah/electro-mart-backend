# importing from Django
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import serializers
from django.contrib.auth import authenticate,login,logout
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
# from .models import CustomUser

# import from Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

# Create your views here.
class UserRegistrationView(APIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self, req):
        serializer = self.serializer_class(data= req.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response("user signup successfull")
        return Response(serializer.errors)
    
def activate(req, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user=None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active=True
        user.save()
        return redirect('login')
    else:
        return redirect('register')
    
class UserLoginView(APIView):
    def post(self, req):
        serializer = serializers.UserLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            # username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=email, password=password)
            # user = authenticate(username=username, password=password)
            login(req, user)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error':"invalid credential"})
        return Response(serializer.errors)


class UserLogoutView(APIView):
    # authentication_classes = [BasicAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, req):
        try:
            req.user.auth_token.delete()
        except:
            return Response("token not found")
        logout(req)
        return redirect('login')

class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserlistSerializer

# def register(req):
#     return HttpResponse("register")