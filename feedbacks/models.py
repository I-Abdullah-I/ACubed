from django.db import models

class Feedbacks(models.Model):
    name = models.CharField(max_length=254, null=False, default = "name", blank=False)
    email = models.EmailField(max_length=254, null=False, default = "email", blank=False)
    feedback = models.TextField(max_length=2000, null=False, blank=False)
    date_submitted = models.DateTimeField(auto_now_add=True, verbose_name='date_submitted')

    def __str__(self):
        return self.email

    class Meta():
        verbose_name = 'feedback'
        verbose_name_plural = 'Feedbacks'
