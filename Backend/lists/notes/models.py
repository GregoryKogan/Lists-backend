from django.db import models


SORT_CHOICES = [
    ("d", "date"),
    ("r", "rating"),
    ("a", "alphabet"),
]
GROUP_CHOICES = [
    ("c", "color"),
    ("t", "tick"),
]
DESC_VIEW_CHOICES = [
    ("f", "first"),
    ("t", "two"),
    ("a", "all"),
    ("n", "none"),
]


class Note(models.Model):
    owner = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, blank=True, default="")

    sort_by = models.CharField(choices=SORT_CHOICES, default="date", max_length=100)
    increasing_order = models.BooleanField(default=False)

    tick = models.BooleanField(default=False)
    color_tags = models.BooleanField(default=False)

    grouping = models.BooleanField(default=False)
    group_by = models.CharField(choices=GROUP_CHOICES, default="tick", max_length=100)

    descriptions = models.BooleanField(default=False)
    descriptions_view = models.CharField(
        choices=DESC_VIEW_CHOICES, default="first", max_length=100
    )

    show_date = models.BooleanField(default=False)

    class Meta:
        ordering = ["updated"]


COLOR_CHOICES = [
    ("rd", "red"),
    ("oe", "orange"),
    ("yw", "yellow"),
    ("gn", "green"),
    ("be", "blue"),
    ("pe", "purple"),
    ("gy", "grey"),
]


class Item(models.Model):
    note = models.ForeignKey('notes.Note', related_name='items', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, blank=True, default="")
    description = models.TextField(blank=True, default="")
    rating = models.DecimalField(default=0.0, decimal_places=1, max_digits=2)
    ticked = models.BooleanField(default=False)
    color = models.CharField(choices=COLOR_CHOICES, default="red", max_length=20)
