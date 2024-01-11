from rest_framework import serializers
from .models import *
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = student
        # field = ['name','age']
        # exclude = ['father_name']
        fields = '__all__'
        
        
    def validate(self,data):
        if data['age'] < 18:
            raise serializers.ValidationError({'error':"age cannot be less than 18"})
        if data['name']:
            for i in data['name']:
                i.isdigit()
                raise serializers.ValidationError({'error':'name cannot contain alphabets'})
        return data


        
        
        
