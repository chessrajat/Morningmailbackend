from rest_framework import serializers

from dashboard.models import Subscriber


class SubscriberSerializer(serializers.Serializer):
    email = serializers.EmailField()
    sent_count = serializers.SerializerMethodField()
    opened_count = serializers.SerializerMethodField()
    

    class Meta:
        model = Subscriber
        fields = ('id', 'email', 'sent_count', 'opened_count')

    def get_sent_count(self, obj):
        return obj.sent_emails.filter(is_successful=True).count()

    def get_opened_count(self, obj):
        return obj.sent_emails.filter(is_opened=True).count()
    