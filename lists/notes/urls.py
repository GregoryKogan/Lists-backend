from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from notes import views

urlpatterns = [
    path("notes/", views.NoteList.as_view()),
    path("notes/<int:pk>/", views.NoteDetail.as_view()),
    path("items/<int:note_pk>/", views.ItemsOfNote.as_view()),
    path("items/<int:note_pk>/<int:pk>", views.ItemDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
