from rest_framework import serializers

from api.models import Allocation, Bid, Comment

class AllocationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        user = serializers.HiddenField(default=serializers.CurrentUserDefault())
        fields = ('user', 'project_name', 'description', 'url', 'base_price', 'end_date')

class BidModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        user = serializers.HiddenField(default=serializers.CurrentUserDefault())
        fields = ('allocation', 'bid')


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        user = serializers.HiddenField(default=serializers.CurrentUserDefault())
        fields = ('auction', 'message')
