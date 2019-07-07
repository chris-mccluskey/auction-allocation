
import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Allocation, Bid, Comment
from api.serializers import AllocationModelSerializer, BidModelSerializer, CommentModelSerializer
from api.permissions import IsOwnerOrReadOnly
from rest_framework import permissions

class AllocationModelViewSet(viewsets.ModelViewSet):

    serializer_class = AllocationModelSerializer
    queryset = Allocation.objects.all()

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BidModelViewSet(viewsets.ModelViewSet):

    serializer_class = BidModelSerializer
    queryset = Bid.objects.all()

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    # def create(self, request):
    #     serialized = self.serializer_class(data=request.data)
    #     if serialized.is_valid():
    #         serialized.save()
    #         return Response(status=HTTP_202_ACCEPTED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentModelViewSet(viewsets.ModelViewSet):

    serializer_class = CommentModelSerializer
    queryset = Comment.objects.all()

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
