from django.utils.timezone import now
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .. import models
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from django.db.models import Q, Case, Value, When
from django_filters.rest_framework import BaseInFilter, NumberFilter



class Documents(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.LegalDocuments

    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return models.Documents.objects.filter(
             deleted_at=None
        ).order_by("-timestamp")

    # def get(self, request, *args, **kwargs):
    #     document = self.serializer_class_documents(self.get_queryset_Doc(), many=True)
    #     return Response({
    #         "documents": document.data,
    #         "response_dat":"Will update soon"
    #     })

    def delete(self, request):
        self.filter_queryset(self.get_queryset()).update(deleted_at=now())
        return Response({})


class DocumentsView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.LegalDocuments

    def get_queryset(self):
        return models.Documents.objects.all()

    def delete(self, request):
        self.filter_queryset(self.get_queryset()).update(deleted_at=now())
        return Response({"Deleted Successfully"})


class Country(APIView):
    def get(self, request):
        return Response({'some':  "vvv"})