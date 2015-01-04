from rest_framework import serializers
from feed.models import Member, Group, Link, Comment, Vote


class MemberSerializer(serializers.ModelSerializer):
    posted = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    comments = serializers.StringRelatedField(many=True)
    date_joined = serializers.DateTimeField(format="%m/%d/%Y")

    class Meta:
        model = Member
        fields = ('id', 'username', 'first_name', 'last_name', 'profile_photo', 'bio', 'date_joined', 'posted', 'comments',)


class GroupSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ('id', 'title', 'description', 'created_at', 'links')

    def get_links(self, obj):
        # values list for list
        return Link.objects.filter(group=obj).values_list('url', 'title', 'description', 'created_at', 'posted_user')
        # values for dict
        # return Link.objects.filter(group=obj).values('url', 'title', 'description', 'created_at', 'posted_user')


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    # link = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        # fields = ('id', 'created_at', 'body', 'link', 'author_name', 'parent',)
        fields = ('id', 'created_at', 'body', 'author_name', 'parent',)

    def get_author_name(self, obj):
        return obj.author.username

    # def get_link(self, obj):
    #     return obj.link.title


class LinkSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    posted_by = serializers.SerializerMethodField()

    class Meta:
        model = Link
        fields = ('id', 'title', 'url', 'posted_by', 'comments',)

    def get_posted_by(self, obj):
        return obj.posted_user.username

    def get_comments(self, obj):
        all_comments = Comment.objects.filter(link=obj, parent__isnull=True)
        serializer = CommentSerializer(all_comments, many=True)
        return serializer.data
