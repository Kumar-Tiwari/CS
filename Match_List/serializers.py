from rest_framework import serializers
from .models import Match_Details
from .models import Match_Summary

class Match_Serializer(serializers.ModelSerializer):
    player1=serializers.StringRelatedField()
    player2=serializers.StringRelatedField()
    Winner=serializers.StringRelatedField()
    class Meta:
        model=Match_Details
        fields="__all__"

class Match_Summary_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Match_Summary
        fields="__all__"

