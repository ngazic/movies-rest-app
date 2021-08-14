from rest_framework import serializers
from user_app.models import User


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
