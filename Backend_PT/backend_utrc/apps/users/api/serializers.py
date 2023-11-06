from rest_framework import serializers
from apps.users.models import User

#Retorna una instancia en tipo JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' #llama todos los campos del modelo 
        #fields = ('username', 'email', 'first_name', 'last_name','password', 'groups'

class TestUserSerielizer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()
    
    def validate_name(self, value):
        if 'Kflores' in value:
            raise serializers.ValidationError('Error, no puede existir un usuario con ese nombre')
        return value
    
    def validate_email(self,value):
        if value == 'karla.flores2@se.gob.hn':
            raise serializers.ValidationError('tiene que indicar un correo')
        return value
    def validate(self, data):
        if data['name'] in data['email']:
            raise serializers.ValidationError('el email no puede contener')
        return data        
    