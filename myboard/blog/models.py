from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='TITLE',max_length=100)
    content = models.TextField('CONTENT',default='')
    pub_date = models.DateTimeField('PUBLISH DATA',default = timezone.now)
    mod_date = models.DateTimeField('MODIFY DATE',auto_now=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
        db_table='blog_posts'
        ordering =['-mod_date',]

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=(self.id,))

    def previous(self):
        return self.get_previous_by_mod_date()

    def get_next(self):
        return self.get_next_by_mod_date()

