from notes.models import Note, Item
from notes.serializers import NoteSerializer, ItemSerializer
from rest_framework import generics, permissions, status
from notes.permissions import IsOwner
from django.http import Http404
from django.core.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.response import Response


class NoteList(APIView):
    """
    List all notes, or create a new note.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        notes = Note.objects.filter(owner=request.user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class ItemsOfNote(APIView):
    """
    List all items of some note or create a new item in it.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get_note(self, request, note_pk):
        try:
            note = Note.objects.get(pk=note_pk)
            if note.owner == request.user:
                return note
            else:
                raise PermissionDenied
        except Note.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, note_pk, format=None):
        note = self.get_note(request, note_pk)
        items = Item.objects.filter(note=note)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, note_pk, format=None):
        note = self.get_note(request, note_pk)
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user, note=note)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
