from django.contrib.auth.models import User
from notes.models import Note
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'notes']
