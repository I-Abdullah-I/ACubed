from django.urls import path

from auth_token.api.views import api_token_retrieval_view

urlpatterns = [
    path('token/', api_token_retrieval_view)
]