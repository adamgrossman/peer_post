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
        return Link.objects.filter(group=obj).values_list('url', 'title', 'description', 'created_at', 'posted_user')


class ChildCommentSerializer(serializers.Serializer):

    def to_native(self, value):
        return self.parent.to_native(value)


class CommentSerializer(serializers.ModelSerializer):
    children = ChildCommentSerializer(many=True,)
    child = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'created_at', 'body', 'author_name', 'parent', 'children', 'child')

    def get_author_name(self, obj):
        return obj.author.username

    def get_child(self, obj):
        children = Comment.objects.filter(lft=obj.id)
        print children
        child = ChildCommentSerializer(children, many=True)
        return child


class TopLevelCommentSerializer(serializers.Serializer):
    class Meta:
        model = Comment


class LinkSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    posted_by = serializers.SerializerMethodField()
    group = serializers.StringRelatedField()
    score = serializers.SerializerMethodField()

    class Meta:
        model = Link
        fields = ('id', 'title', 'url', 'created_at', 'posted_by', 'group', 'flag', 'score', 'comments',)

    def get_posted_by(self, obj):
        return obj.posted_user.username

    def get_comments(self, obj):
        all_comments = Comment.objects.filter(link=obj, parent__isnull=True)
        serializer = CommentSerializer(all_comments, many=True)
        return serializer.data

    def get_score(self, obj):
        up_votes = Vote.objects.filter(link=obj).filter(up_vote=True).count()
        down_votes = Vote.objects.filter(link=obj).filter(up_vote=False).count()
        score = up_votes - down_votes
        return score
