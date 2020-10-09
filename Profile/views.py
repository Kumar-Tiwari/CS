from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .serializers import Profile_Serializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
User=get_user_model()

@csrf_exempt 
# ignore csrf_token
def users_data(request):
    if request.method=="GET":
        data=User.objects.all()
        serialized_data=Profile_Serializer(data,many=True)
        return JsonResponse(serialized_data.data,safe=False)

    if request.method=="POST":
        data=JSONParser().parse(request)
        serializer=Profile_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        else:
            return JsonResponse(serializer.errors,status=400)
