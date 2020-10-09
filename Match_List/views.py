from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .serializers import Match_Serializer,Match_Summary_Serializer
from django.views.decorators.csrf import csrf_exempt
from .models import Match_Details,Match_Summary

@csrf_exempt 
# ignore csrf_token
def match_detail(request):
    if request.method=="GET":
        data=Match_Details.objects.all()
        serialized_data=Match_Serializer(data,many=True)
        return JsonResponse(serialized_data.data,safe=False)

def match_summary(request,pk):
    if request.method=="GET":
        try:
            data=Match_Summary.objects.get(pk=pk)
            serializer=Match_Summary_Serializer(data)
            return JsonResponse(serializer.data,status=200,safe=False)
        except:
            return JsonResponse({'error':'The Match is yet to be played'},status=400,safe=False)
