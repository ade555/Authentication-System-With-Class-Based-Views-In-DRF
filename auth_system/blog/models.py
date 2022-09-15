from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    post_body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', related_name='author', on_delete=models.CASCADE) 

    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return self.title
