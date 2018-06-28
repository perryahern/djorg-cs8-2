from rest_framework import serializers, viewsets
from .models import Bookmark, PrivateBookmark

#TODO: CRITICAL: disable this or modify to only work for admin

class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Bookmark
    fields = ('title', 'url', 'note', 'category')

class BookmarkViewSet(viewsets.ModelViewSet):
  serializer_class = BookmarkSerializer
  queryset = Bookmark.objects.all()

class PrivateBookmarkSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = PrivateBookmark
    fields = ('title', 'url', 'note', 'category')

  def create(self, validated_data):
    # import pdb; pdb.set_trace()
    user = self.context['request'].user
    private_bookmark = PrivateBookmark.objects.create(user=user, **validated_data)
    return private_bookmark

class PrivateBookmarkViewSet(viewsets.ModelViewSet):
  serializer_class = PrivateBookmarkSerializer
  queryset = PrivateBookmark.objects.none()

  def get_queryset(self):
    user = self.request.user
    if user.is_anonymous:
      return PrivateBookmark.objects.none()
    else:
      return PrivateBookmark.objects.filter(user=user)
