from django.db import models
from django.urls import reverse
from django.conf import settings
import misaka

from groups.models import Group
 
from  django.contrib.auth import get_user_model
User=get_user_model()

class Post(models.Model):
    user=models.ForeignKey(User,related_name='posts',on_delete=None)
    created_at=models.DateTimeField(auto_now=True)
    message=models.TextField(blank=True)
    notes_url=models.URLField(default='',blank=False)
    chapter_name=models.CharField(max_length=128,default='',blank=True) 
    subject_name=models.CharField(max_length=128,default='',blank=True)  
                                                                                # change blank to false later
    message_html=models.TextField(editable=True,default='')
    group=models.ForeignKey(Group,related_name='posts',null=True,blank=True,on_delete=None)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html=misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})

    class Meta:
        ordering =['-subject_name']
        
        
        