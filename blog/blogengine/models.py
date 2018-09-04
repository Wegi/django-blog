from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    pub_date = models.DateTimeField()
    text = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title+'-'+str(self.pub_date))
        super(Post, self).save(*args, **kwargs)