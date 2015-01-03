from rest_framework import serializers
from feed.models import Member, Group, Link, Comment, Vote


class MemberSerializer(serializers.ModelSerializer):
    posted = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'profile_photo', 'bio', 'date_joined', 'posted', 'comments', 'votes',)

    def get_posted(self, obj):
        return Link.objects.filter(posted_user=obj)

    def get_comments(self, obj):
        return Comment.objects.filter(author=obj)

    def get_votes(self, obj):
        return Vote.objects.filter(voter=obj)


class GroupSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ('id', 'title', 'description', 'created_at', 'links')

    def get_links(self, obj):
        return Link.objects.filter(group=obj)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'created_at', 'body', 'link', 'author', 'parent',)


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('id', 'title', 'url',)

