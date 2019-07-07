from django.contrib import admin
from .models import Allocation, Bid, Comment

@admin.register(Allocation)
class AllocationAdmin(admin.ModelAdmin):
    pass

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
