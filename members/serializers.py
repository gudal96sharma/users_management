from .models import *
from rest_framework import serializers
import string,random

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','name','emp_code','state','city')
        
    def create(self,validated_data):
        user = User(
            name        = validated_data['name'],
            email       = validated_data['email'],
            state       = validated_data['state'],
            emp_code    = validated_data['emp_code'],
            city        = validated_data['city'],
        )
        user.set_password(validated_data['password'])
        # password = (''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8)))
        # user.set_password(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8)))
        # user.set_password(password)
        user.save()
        return user