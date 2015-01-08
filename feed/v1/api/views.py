from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from feed.models import Member, Link, Group, Vote, Comment
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
    print "viewset"
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    # authentication_classes = (SessionAuthentication,)

    def pre_save(self, obj):
        print "presave"
        obj.posted_user = self.request.user.id
    # def perform_create(self, serializer):
    #     serializer.save(posted=self.request.user)
    #
    # def post(self, request, format=None):
    #     serializer = LinkSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def perform_create(self, serializer):
    #     serializer.save(posted_user=self.request.user)

