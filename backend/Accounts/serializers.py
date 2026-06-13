from rest_framework import serializers
from .models import Users
from django.contrib.auth import get_user_model  
from rest_framework_simplejwt.tokens import RefreshToken
User = get_user_model()
class UserRegisterSerializer(serializers.ModelSerializer):

    password=serializers.CharField(write_only=True)

    class Meta:
        model=Users
        fields=["username","email","first_name","last_name","role","cin","image","password"]

    extra_Kwargs={
        "username":{"required":True,"allow_blank":True},
        "first_name":{"required":True,"allow_blank":False},
        "last_name":{"required":True,"allow_blank":False},
        "email":{"required":True,"allow_blank":False},
        "cin":{"required":True,"allow_blank":False},
        "role":{"required":True,"allow_blank":False},
        "image":{"required":False,"allow_blank":False},
        "password":{"required":True,"allow_blank":False,"min_length":8}
    }

    def create(self, validated_data):
        password=validated_data.pop("password")

        user=Users.objects.create_user(**validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["first_name", "last_name", "email", "image", "cin"]

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    



   


class ChangePassword(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = Users
        fields = ["old_password", "new_password", "confirm_password"]
    
    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()

        return instance

class EmailRest(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not Users.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user found with this email address.")
        return value

class ForgotPassword(serializers.Serializer):
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    class Meta:
        model = Users
        fields = ["password", "confirm_password"]

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers   
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    

class Logout(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except Exception as e:
            raise serializers.ValidationError({"detail": str(e)})
        return self.token