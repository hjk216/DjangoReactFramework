from rest_framework import serializers
from .models import TestModel

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'
        #fields = ('id', 'title', 'number')
