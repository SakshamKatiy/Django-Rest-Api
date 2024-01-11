from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *
# Create your views here.
@api_view(['GET'])
def home(request):
    student_objs = student.objects.all()
    serializer = studentSerializer(student_objs,many=True)
    return Response({'status':200,'playload':serializer.data})

@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = studentSerializer(data = request.data)

    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':403,'errors':serializer.errors,'playload':data,'message':'Something went wronge'})
    
    serializer.save()

    return Response({'status':200,'playload':serializer.data,'message':'sent'})

@api_view(['PUT'])
def update_student(request, id):
    try:
        student_obj = student.objects.get(id = id)
        serializer = studentSerializer(student_obj,data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors,'message':'Something went wronge'})
        
        serializer.save()

        return Response({'status':200,'playload':serializer.data,'message':'sent'})
    except Exception as e:
        print(e)
        return Response({'status':403,'message':'invalid id'})