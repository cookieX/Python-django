from django.urls import path
from . import views


urlpatterns = [
    path("document/", views.Documents.as_view()),
    path("document/<int:pk>/", views.DocumentsView.as_view()),
    path("country/list/", views.Country.as_view()),
   
]
