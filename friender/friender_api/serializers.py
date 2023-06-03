from rest_framework import serializers
from arrangement.models import Establishments, Users, Hobbies


class EstablishmentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    category = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Establishments.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance


class UsersSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
    age = serializers.CharField(max_length=100)
    sex = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.age = validated_data.get('age', instance.age)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.email = validated_data.get('email', instance.email)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance


class HobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbies
        fields = ['name', 'category']
