from rest_framework import serializers

# from ordered_set import OrderedSet

from members.models import TeamMembers

class TeamMembersSerializer(serializers.ModelSerializer):
    
    # social = serializers.SerializerMethodField('accountparser')
    skills = serializers.SerializerMethodField('skillsparser')
    id = serializers.SerializerMethodField('idretriever')

    class Meta():
        model = TeamMembers
        fields = ['name', 'position', 'skills', 'facebook_account', 'linkedin_account', 'github_account', 'id']

    # def accountparser(self, team_member):
    #     accounts = team_member.accounts
        
    #     accounts = accounts.split(',')

    #     social_array = {}

    #     for acc in accounts:
    #         acc = acc.split(':')
    #         social_array[acc[0].strip()] = acc[1].strip()
        
    #     return social_array


    def skillsparser(self, team_member):
        skills = team_member.skills
        
        skill = skills.split(',')

        skills_array = []

        for skill in skill:
            skills_array = skills_array + [skill.strip()] 
        
        return skills_array

    def idretriever(self, team_member):
        return team_member.pk