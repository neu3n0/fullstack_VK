from rest_framework import serializers

from .models import Chat, ChatMember
from messageschat.models import Message
from django.shortcuts import get_object_or_404


from django.db.models import Q

from messageschat.serializers import LastMessageSerializer

from django.db import transaction

from users.models import User


def check_user_in_chat(chat, user):
    return chat.chat_members.filter(user=user).exists()


class ChatCreateSerializer(serializers.ModelSerializer):
    """Serializer for chat"""

    # write_only_char_field = serializers.CharField(write_only=True)
    new_members = serializers.ListField(write_only=True)

    members = serializers.SerializerMethodField()
    admins = serializers.SerializerMethodField()

    # @transaction.atomic
    # def create(self, validated_data):
    #     # print('create', validated_data)
    #     # validated_data.pop('memberst', None)
    #     chat = super().create(validated_data)
    #     # ChatMember.objects.create(
    #     #     chat=chat, user=self.context['request'].user, chat_admin=True)
    #     # print('create', chat)
    #     return chat

    @transaction.atomic
    def save(self, **kwargs):
        members = self.validated_data.pop('new_members', None)
        chat = super().save(**kwargs)
        ChatMember.objects.create(
            chat=chat,
            user=self.context['request'].user,
            chat_admin=True
        )
        for member in members:
            user = get_object_or_404(User, id=member)
            ChatMember.objects.create(
                chat=chat, user=user, added_by_user=self.context['request'].user)
        return chat

    class Meta:
        model = Chat
        fields = '__all__'

    def get_members(self, obj):
        return ChatMember.objects.filter(chat__id=obj.pk).values_list('user__username', flat=True)

    def get_admins(self, obj):
        return ChatMember.objects.filter(Q(chat__id=obj.pk) & Q(chat_admin=True)).values_list('user__username', flat=True)


class ChatMemberListSerializer(serializers.ModelSerializer):

    chat = serializers.SerializerMethodField()

    last_message = serializers.SerializerMethodField()

    def get_chat(self, obj):
        return ChatListSerializer(obj.chat).data

    def get_last_message(self, obj):
        if (Message.objects.filter(chat__id=obj.chat.id).exists()):
            return LastMessageSerializer(Message.objects.filter(chat__id=obj.chat.id).first()).data
        return None

    class Meta:
        model = ChatMember
        fields = ('chat', 'muted', 'last_message',)


class ChatSerializer(serializers.ModelSerializer):
    """Serializer for chat"""

    members = serializers.SerializerMethodField()
    admins = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = '__all__'

    def get_members(self, obj):
        return ChatMember.objects.filter(chat__id=obj.pk).values_list('user__username', flat=True)

    def get_admins(self, obj):
        return ChatMember.objects.filter(Q(chat__id=obj.pk) & Q(chat_admin=True)).values_list('user__username', flat=True)


class ChatEditSerializer(serializers.ModelSerializer):

    new_members = serializers.ListField(write_only=True)

    @transaction.atomic
    def update(self, instance, validated_data):
        members = validated_data.get('new_members')
        for member in members:
            user = get_object_or_404(User, id=member)
            ChatMember.objects.create(
                chat=instance,
                user=user,
                added_by_user=self.context['request'].user
            )
        return super().update(instance, validated_data)

    """Serializer for chat"""
    class Meta:
        model = Chat
        fields = ('title', 'description', 'new_members')


class ChatMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatMember
        fields = ('user', 'chat_admin')


class ChatListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('title', 'category')