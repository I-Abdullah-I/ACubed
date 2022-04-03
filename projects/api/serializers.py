from rest_framework import serializers

from projects.models import DoneProjects

class DoneProjectsSerializer(serializers.ModelSerializer):

    frontend = serializers.SerializerMethodField('frontend_parser')
    backend = serializers.SerializerMethodField('backend_parser')

    class Meta():
        model = DoneProjects
        fields = ['name', 'id', 'thumbnail', 'frontend', 'backend']
        
    def frontend_parser(self, project):
        techs = project.frontend

        techs = techs.split(',')

        for i, tech in enumerate(techs):
            techs[i] = tech.strip()

        return techs
        
    def backend_parser(self, project):
        techs = project.backend

        techs = techs.split(',')

        for i, tech in enumerate(techs):
            techs[i] = tech.strip()

        return techs
