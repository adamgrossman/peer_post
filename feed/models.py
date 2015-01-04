from django.contrib.auth.models import AbstractUser
from django.db import models
from mptt.managers import TreeManager
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


class Member(AbstractUser):
    profile_photo = models.ImageField(upload_to='member_photos', blank=True, null=True)
    bio = models.TextField()

    def __unicode__(self):
        return u'{}'.format(self.username)


class Group(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    member = models.ManyToManyField(Member, related_name="subscriber")

    def __unicode__(self):
        return u'{}'.format(self.title)


class Link(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    flag = models.IntegerField(default=0)
    star = models.ManyToManyField(Member, blank=True, null=True, related_name="starred")
    # changed from ForeignKey to ManytoManyField to have many users star links
    posted_user = models.ForeignKey(Member, related_name="posted")
    group = models.ForeignKey(Group, related_name="links")

    def __unicode__(self):
        return u'{}'.format(self.title)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    link = models.ManyToManyField(Link, related_name="tags")

    def __unicode__(self):
        return u'{}'.format(self.name)


class Vote(models.Model):
    up_vote = models.BooleanField(default=True)
    voter = models.ForeignKey(Member, related_name="votes")
    link = models.ForeignKey(Link, related_name="votes")

    def __unicode__(self):
        return u'{} voted on: {}'.format(self.voter.username, self.link.title)


class Comment(MPTTModel):
    all_objects = TreeManager()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Member, related_name="comments")
    link = models.ForeignKey(Link, related_name="comments")
    parent = TreeForeignKey('self', blank=True, null=True, related_name="children")

    def __unicode__(self):
        return u'{} by {}'.format(self.body, self.author.username)
