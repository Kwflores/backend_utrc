#from rest_framework.views import APIView
from rest_framework.views import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import *

@api_view(['GET', 'POST'])
def user_api_view(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        users_serialezer = UserSerializer(users, many = True)
        test_data={
             'name':'Kflores',
             'email':'karla.flores2@se.gob.hn'
                  }
        test_user = TestUserSerielizer(data = test_data)
        if test_user.is_valid():
            print('paso las validaciones')
        else:
            print(test_user.errors)
        return Response(users_serialezer.data, status= status.HTTP_200_OK)
    #Guardar Data 
    elif request.method == 'POST':
        users_serialezer = UserSerializer(data = request.data)
        if users_serialezer.is_valid():
            users_serialezer.save()
            return Response(users_serialezer.data,status= status.HTTP_201_CREATED)
        return Response(users_serialezer.errors, status= status.HTTP_400_BAD_REQUEST)
            

@api_view(['GET','PUT','DELETE'])
def user_detalles_view(request, pk=None):
    user = User.objects.filter(id = pk).first()
    if user:
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status= status.HTTP_200_OK)
        elif request.method == 'PUT':
            _user_serializer = UserSerializer(user,data =request.data)
            if _user_serializer.is_valid():
                _user_serializer.save()
                return Response(_user_serializer.data, status= status.HTTP_200_OK)
            return Response(_user_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            user.delete()
            return Response({'messag': 'Usuario Elminado correctamente.!'}, status= status.HTTP_200_OK)
    return Response({'message':'No se ha encontrado un usuario con los datos proporcionados'}, status= status.HTTP_400_BAD_REQUEST)
        
        
 
