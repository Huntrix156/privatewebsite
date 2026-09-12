from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project_image = models.ImageField(upload_to='project/')
    published_at = models.DateTimeField(auto_now_add=True)
    project_url = models.URLField()
    vercel_url = models.URLField()

    def __str__(self):
        return self.title

