from rest_framework import viewsets
from feedbacks.models import Feedbacks
from feedbacks.api.serializers import FeedbacksSerializer


class feedbacksApi(viewsets.ModelViewSet):
    queryset           = Feedbacks.objects.all().order_by('-id')
    serializer_class   = FeedbacksSerializer
