from ressources.models import Depency, Salary , Category

from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class SalarySerializer(serializers.ModelSerializer):
	class Meta:
		model = Salary
		fields ='__all__'

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields ='__all__'

class DepencySerializer(serializers.ModelSerializer):
    #category = CategorySerializer()
    class Meta:
        model = Depency
        fields =['amount','salary','category','date','user']	
	
		
class DepencySerializer2(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Depency
        fields =['amount','salary','category','date','user']	
	
		

   	
   