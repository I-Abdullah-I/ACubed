from rest_framework import serializers

from services.models import Services

class ServicesSerializer(serializers.ModelSerializer):

    class Meta():
        model = Services
        fields = ('name','icon', 'body', 'image')