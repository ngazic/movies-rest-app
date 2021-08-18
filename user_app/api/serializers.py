from user_app.utils import Util
from rest_framework import serializers
from user_app.models import User
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import  urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.exceptions import AuthenticationFailed



class AccountSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    is_admin = serializers.BooleanField(source='is_staff')
    # user = RegistrationSerializer(many=False, read_only=True)
    password = serializers.CharField(min_length=8, allow_blank=False)
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'password', 'username', 'email', 'is_admin', 'first_name', 'last_name', 'is_active', 'tel_number', 'contract_id', 'address',]
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'read_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        p = {**validated_data}
        print(p)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
   
        

class AdminSerializer(serializers.ModelSerializer):
    is_admin = serializers.BooleanField(source='is_staff')
    
    class Meta:
        model = User
        # fields = '__all__'
        # fields = ['id', 'password', 'username', 'email', 'is_admin', 'first_name', 'last_name', 'is_active', 'tel_number', 'contract_id', 'address',]
        fields = ['username', 'email', 'password', 'is_admin']
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        # model = User
        # fields = '__all__'
        # fields = ['id', 'password', 'username', 'email', 'is_admin', 'first_name', 'last_name', 'is_active', 'tel_number', 'contract_id', 'address',]
        fields = ['email']

    def validate(self, data):
     

        
        return data




class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    password2 = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'password2', 'token', 'uidb64']

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        
        if password != password2:
            raise serializers.ValidationError({'error': 'P1 and P2 should be same!'})
        
        token = data.get('token')
        uidb64 = data.get('uidb64')
        id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=id)

        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError({'error': 'Token not valid'})

        user.set_password(password)
        user.save()

        return (user)
