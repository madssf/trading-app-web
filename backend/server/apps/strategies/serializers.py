from rest_framework import serializers

from .models import Strategy, ParameterType, Parameter, StrategyParameter


class StrategySerializer(serializers.ModelSerializer):

    class Meta:
        model = Strategy
        fields = '__all__'


class ParameterTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParameterType
        fields = '__all__'


class ParameterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parameter
        fields = '__all__'


class StrategyParameterSerializer(serializers.ModelSerializer):

    class Meta:
        model = StrategyParameter
        fields = '__all__'
