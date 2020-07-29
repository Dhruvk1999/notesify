from django.db import models
from django.utils.text import slugify
import misaka
from django.contrib.auth import get_user_model
User=get_user_model()
from django import template
from django.urls import reverse
register=template.Library()
# Create your models here.

class Semester(models.Model):
    sem_no=models.CharField(max_length=128,unique=True,default='')

    def __str__(self):
        return self.sem_no

class Group(models.Model):
    name=models.CharField(max_length=256,unique=True)
    slug=models.SlugField(allow_unicode=True,unique=True)
    description=models.TextField(blank=True,default='')
    description_html=models.TextField(editable=False,default='',blank=True)
    members=models.ManyToManyField(User,through='GroupMember')
    which_semester=models.ForeignKey(Semester,related_name='sem',on_delete=None,default='',blank=True)
    

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        self.description_html=misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})

    class Meta:
        ordering =['-which_semester']

class GroupMember(models.Model):
    group=models.ForeignKey(Group,related_name='memberships',on_delete=None)
    user=models.ForeignKey(User,related_name='user_groups',on_delete=None)
    

    def __str__(self):
        return self.user.username 

    class Meta:
        unique_together=('group','user')
