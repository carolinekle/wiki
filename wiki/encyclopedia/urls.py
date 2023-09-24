from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry_page, name="entry"),
    path("wiki/error", views.entry_page, name="error"),
    path("search/", views.search, name="search"),
    path("new/", views.new, name="new"),
    path("new-submit/", views.new_submit, name="new_submit"),
    path("edit/", views.edit, name="edit"),
    path("save-edit/", views.save_edit, name="save_edit"),
    path("random-page/", views.random_page, name="random_page"),
]
