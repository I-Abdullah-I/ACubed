from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

from projects.models import DoneProjects
from projects.api.serializers import DoneProjectsSerializer


class AllProjectsApi(viewsets.ModelViewSet):
    queryset = DoneProjects.objects.all().order_by('-id')
    serializer_class = DoneProjectsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

