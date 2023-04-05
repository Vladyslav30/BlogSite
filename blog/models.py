from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.TextField(max_length=1000)
    post_date = models.DateTimeField('date published')
    post_image = models.ImageField(upload_to='post_images/')

    def get_summary(self):
        return self.post_text[:15]

