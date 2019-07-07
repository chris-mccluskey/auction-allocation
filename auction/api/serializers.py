from rest_framework import serializers

from api.models import Allocation, Bid, Comment

class AllocationModelSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Allocation
        fields = ('user', 'project_name', 'description', 'url', 'base_price', 'end_date')

class BidModelSerializer(serializers.ModelSerializer):
    # allocation = serializers.CharField(source='allocation.project_name', read_only=True)
    # allocation = serializers.StringRelatedField()
    project_name = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')
    # allocation = AllocationModelSerializer()
    class Meta:
        model = Bid
        fields = ('user', 'project_name', 'allocation', 'bid')

    def validate(self, data):
        for obj in  Bid.objects.filter(allocation__project_name__icontains=data['allocation']):
            if data['bid'] < obj.bid:
                raise serializers.ValidationError("This bid is less than the current bids!")
        return data


class CommentModelSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ('user', 'auction', 'message')
