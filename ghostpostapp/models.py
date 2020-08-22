from django.db import models
from django.utils import timezone


class BoastRoast(models.Model):
    isroast = models.BooleanField()
    post_content =models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    submissiondate = models.DateTimeField(default=timezone.now)


    @property
    def score(self):
        return self.upvotes - self.downvotes