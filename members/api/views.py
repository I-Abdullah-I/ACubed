from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from members.models import TeamMembers
from members.api.serializers import TeamMembersSerializer


class membersApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset           = TeamMembers.objects.all().order_by('id')
    serializer_class   = TeamMembersSerializer