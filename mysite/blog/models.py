from django.db import models

#model is your entire database


class Post(models.Model): #each class is like a table
    title = models.CharField(max_length = 140) #each var is a column
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self): #returns title in string format
        return self.title