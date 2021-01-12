from rest_framework import serializers


class DataSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    month = serializers.CharField()
    day = serializers.CharField()
    birth = serializers.IntegerField()
