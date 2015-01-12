from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from feed.models import Member, Link, Group, Comment, Vote
from feed.v1.api.serializers import MemberSerializer, GroupSerializer, CommentSerializer, LinkSerializer


class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

    @detail_route(methods=['post'])
    def upvote(self, request, pk):
        link = Link.objects.get(pk=pk)
        vote, created = Vote.objects.get_or_create(voter=request.user, link=link)
        vote.up_vote = True
        vote.save()
        return Response(status=status.HTTP_200_OK)

    @detail_route(methods=['post'])
    def downvote(self, request, pk):
        link = Link.objects.get(pk=pk)
        vote, created = Vote.objects.get_or_create(voter=request.user, link=link)
        vote.up_vote = False
        vote.save()
        return Response(status=status.HTTP_200_OK)

    @detail_route(methods=['post'])
    def flag(self, request, pk):
        link = Link.objects.get(pk=pk)
        link.flag += 1
        if link.flag >= 10:
            link.delete()
        else:
            link.save()
        return Response(status=status.HTTP_200_OK)
