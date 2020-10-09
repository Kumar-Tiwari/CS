from django.contrib.auth import get_user_model
from rest_framework import serializers
User=get_user_model()


class Profile_Serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user