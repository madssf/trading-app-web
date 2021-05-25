from rest_framework import serializers

from .models import Strategy, ParameterType, Parameter, StrategyParameter


class StrategySerializer(serializers.ModelSerializer):

    class Meta:
        model = Strategy
        fields = ['created_at', 'created_by', 'name',
                  'description']


class ParameterTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParameterType
        fields = ['created_at', 'created_by', 'name']


class ParameterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parameter
        fields = ['created_at', 'created_by',
                  'name', 'description', 'parameter_type']


class StrategyParameterSerializer(serializers.ModelSerializer):

    class Meta:
        model = StrategyParameter
        fields = ['strategy', 'parameter']
