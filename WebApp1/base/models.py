from django.db import models
import uuid


#Classes like ROom topic and message

class Project(models.Model):
    title=models.CharField(max_length=200)
    userName = models.CharField(max_length=200, null = False, blank= False, default="Anonymous user")
    description = models.TextField(null = True, blank=True)
    demo_link =models.CharField(max_length=2000, null=True,blank=True)
    user_image = models.ImageField(null=True, blank = True, default = "default.png")
    source_link =models.CharField(max_length=2000, null=True,blank=True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key = True, editable=False)
    tags = models.ManyToManyField('Tag', blank=True) #creating relatiponship with Tags
    vote_total = models.IntegerField(default=0,null=True, blank=True)#creating relatiponship with review
    vote_ratio = models.IntegerField(default=0,null=True, blank=True)
    def __str__(self):
        return self.title

class Review(models.Model):

    VOTE_TYPE =(
        ('up','Up Vote'),
        ('down','Down Vote')
    )
    #owner=
    project = models.ForeignKey(Project,on_delete = models.CASCADE)#what if we delete a project? all the reviews will be deleted
    #sa
    body = models.TextField(null = True, blank=True)
    value =models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key = True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):

   
    name=models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key = True, editable=False)

    def __str__(self):
        return self.name
