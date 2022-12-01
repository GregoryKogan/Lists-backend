from django.contrib.auth.models import User
from django.core import exceptions
import django.contrib.auth.password_validation as validators
from notes.models import Note
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())

    def validate(self, data):
        password = data.get('password')

        data_copy = data.copy()
        del data_copy['notes']
        user = User(**data_copy)

        errors = {}
        try:
            validators.validate_password(password=password, user=user)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)
        return super(UserSerializer, self).validate(data)

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )

    class Meta:
        model = User
        fields = ["id", "username", "password", "notes"]
