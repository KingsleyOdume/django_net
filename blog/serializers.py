from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ("id", "comment", "created_by",)
    read_only_fields = ("created_by",)

  def create(self, validated_data):
    user = self.context.get("request").user
    return Comment.objects.create(**validated_data, created_by=user)