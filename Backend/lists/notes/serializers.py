from rest_framework import serializers
from notes.models import Note, Item


class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Note
        fields = [
            "id",
            "owner",
            "title",
            "created",
            "updated",
            "sort_by",
            "increasing_order",
            "tick",
            "color_tags",
            "grouping",
            "group_by",
            "descriptions",
            "descriptions_view",
            "show_date",
        ]


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    note = serializers.ReadOnlyField(source="note.title")

    class Meta:
        model = Item
        fields = [
            "id",
            "owner",
            "note",
            "created",
            "updated",
            "title",
            "description",
            "rating",
            "ticked",
            "color",
        ]
