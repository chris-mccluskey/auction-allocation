from django.db import models
from django.conf import settings


class Allocation(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    url = models.URLField(max_length=500)
    base_price = models.PositiveIntegerField(default=1)
    start_date = models.DateField(auto_now=False, auto_now_add=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.project_name


class Bid(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    allocation = models.ForeignKey(Allocation, on_delete=models.CASCADE)
    bid = models.PositiveIntegerField(unique=True)
    created = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.bid

    @property
    def project_name(self):
        return self.allocation.project_name


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    auction = models.ForeignKey(Allocation, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    created = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.message
