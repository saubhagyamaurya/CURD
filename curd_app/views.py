from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import Users,update,delete,single
from .serializers import usersSerializer,updateSerializer,deleteSerializer,singleSerializer
# Create your views here.

class createuser(APIView):
    queryset=Users.objects.all()
    serializer_class = usersSerializer

    def post(self,request,*args,**kwargs):
        serializer = usersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={"Code":200,"Sucess":"User registered sucessfully"}
            return Response(data)
        else:
            data={"Code":101,"Sucess":"User not registered sucessfully"}
            return Response(data)

class updateuser(APIView):
    queryset=update.objects.all()
    serializer_class = updateSerializer
    
    def post(self,request,*args,**kwargs):
        serializer = updateSerializer(data=request.data)
        if serializer.is_valid():
            ide = request.data['user_id']
            a = Users.objects.get(pk=ide)
            a.username = request.data['user_name']
            a.save()
            serializer.save()
            data={"Code":200,"Status":"User details update sucessfully"}
        return Response(data,status=status.HTTP_201_CREATED)

class listuser(APIView):
    def get(self,request,*args,**kwargs):
        queryset = Users.objects.all()
        serializer = usersSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)



class deleteuser(APIView):
    queryset = delete.objects.all()
    serializer_class = deleteSerializer

    def post(self,request,*args,**kwargs):
        ide=request.data['user_id']
        a = Users.objects.get(pk=ide)
        a.delete()
        data={"Code":200,"Status":"User delete Sucessfully"}
        return Response(data,status=status.HTTP_201_CREATED) 

class singleuser(APIView):
    queryset = single.objects.all()
    serializer_class = singleSerializer

    def post(self,request,*args,**kwargs):
        ide=request.data['user_id']
        a = Users.objects.get(pk=ide)
        return Response(a,status=status.HTTP_201_CREATED)

