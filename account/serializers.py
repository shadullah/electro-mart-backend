from rest_framework import serializers
from django.contrib.auth.models import User
# from .models import CustomUser
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    # user_type = serializers.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES,required= False, allow_null=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name' ,'email', 'password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        # user_type = self.validated_data.get['user_type']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']

        if password != password2:
            raise serializers.ValidationError({"error":"password not matched"})
        if User.objects.filter(email=email).exists():
            serializers.ValidationError({"error":"email exists"})
        
        account = User(username=username, email=email, first_name=first_name, last_name=last_name)
        print(account)
        account.set_password(password)
        account.save()
        return account
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    # username = serializers.CharField(required=True)
    password = serializers.CharField(required = True)

# user list serializer
# User = get_user_model()

class UserlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']