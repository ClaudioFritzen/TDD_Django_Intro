from django.db import models

# Create your models here.

"""
    class Post
        -id:int
        -title: varchar
        -body: textarea
        -created_at: datetime
        - modifiel_at: datetime

"""

class Post(models.Model):
    title =  models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
