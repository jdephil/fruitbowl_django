from django.db import models

# Create your models here.
class Tip(models.Model):
  title = models.CharField(max_length=264)
  category = models.CharField(max_length=50)
  url = models.URLField(max_length=200)
  urlTitle = models.CharField(max_length=264, blank=True, null=True)

  def __str__(self):
      return self.title
  