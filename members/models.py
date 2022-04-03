from django.db import models


class TeamMembers(models.Model):
    name                          = models.CharField(max_length=256, null=False, blank=False)
    position                      = models.CharField(max_length=256, null=False, blank=False)
    skills                        = models.CharField(max_length=256, null=False, blank=False)
    facebook_account              = models.CharField(max_length=265, null=True, blank=True)
    linkedin_account              = models.CharField(max_length=265, null=True, blank=True)
    github_account                = models.CharField(max_length=265, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = 'Members'
        verbose_name_plural = 'Team Members'
