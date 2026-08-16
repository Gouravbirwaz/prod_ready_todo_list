from django.db import models

# Create your models here.

class ToDoModel(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    head_line=models.CharField(max_length=100,blank=True,null=True)
    title=models.TextField(max_length=200)
    created_at=models.DateTimeField(auto_now=True)
    image_attched=models.ImageField(upload_to="user/image",blank=True,null=True)
