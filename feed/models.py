from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


class TimeStampedBaseMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Member(AbstractUser, TimeStampedBaseMixin):
    profile_photo = models.ImageField(upload_to='member_photos', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __unicode__(self):
        return u'{}'.format(self.username)


class Group(TimeStampedBaseMixin):
    title = models.CharField(max_length=50)
    description = models.TextField()
    subscribers = models.ManyToManyField(Member, related_name="subscribers", blank=True)

    def __unicode__(self):
        return u'{}'.format(self.title)


class Link(TimeStampedBaseMixin):
    url = models.URLField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    submitted_by = models.ForeignKey(Member, related_name="links", null=True)
    group = models.ForeignKey(Group, related_name="links")

    def __unicode__(self):
        return u'{}'.format(self.title)


class Tag(TimeStampedBaseMixin):
    name = models.CharField(max_length=50)
    link = models.ManyToManyField(Link, related_name="tags")

    def __unicode__(self):
        return u'{}'.format(self.name)


class Vote(TimeStampedBaseMixin):
    up_vote = models.BooleanField(default=True)
    voter = models.ForeignKey(Member, related_name="votes")
    link = models.ForeignKey(Link, related_name="votes")

    def __unicode__(self):
        return u'{} voted on: {}'.format(self.voter.username, self.link.title)


class Comment(TimeStampedBaseMixin):
    body = models.TextField()
    author = models.ForeignKey(Member, related_name="comments")
    link = models.ForeignKey(Link, related_name="comments")
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children")

    def __unicode__(self):
        return u'{} by {}'.format(self.body, self.author.username)


class Star(TimeStampedBaseMixin):
    link = models.ForeignKey(Link, related_name="stars")
    member = models.ForeignKey(Member, related_name="stars")
