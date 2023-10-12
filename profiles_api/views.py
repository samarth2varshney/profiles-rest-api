from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer # make the variable only serializer_class 

    def get(self, request, format=None):
        """Return a list APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'messgae':'Hello!','an_apivew':an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            messaage = f'hello {name}'
            return Response({'message':messaage})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """"hanlde updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handel a papartial update of an object"""
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
        


class HelloViewSet (viewsets.ViewSet):
    """Test Api ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return Hello message"""

        a_viewset = [
            'Uses action (list,create,retireve,update,partial_update)',
            'Automatically maps to URLs using Routres',
            'Provides more functionality with less code',
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})
    
    def create(self,request):
        """create a new hello message"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """handle getting an object by its id"""
        return Response({'http_method':'GET'})
    
    def update(self,request,pk=None):
        """handle updating an object by its id"""
        return Response({'http_method':'PUT'})
    
    def partial_update(self,request,pk=None):
        """handle updating an object by its id"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self,request,pk=None):
        """handle removing an object by its id"""
        return Response({'http_method':'DELETE'})