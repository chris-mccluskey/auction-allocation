from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()

router.register('allocation', views.AllocationModelViewSet, base_name='allocation')
router.register('bid', views.BidModelViewSet, base_name='bid')
router.register('comment', views.CommentModelViewSet, base_name='comment')

urlpatterns = router.urls
