from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            'password': {'required': True, 'write_only': True}
        }

    def create(self, validated_data):
        # Todo: add confirm password validation
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
