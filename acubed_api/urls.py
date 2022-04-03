from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

#importing all views to regiseter to router
from feedbacks.api.views import feedbacksApi
from members.api.views   import membersApi
from projects.api.views  import AllProjectsApi
from services.api.views  import ServicesApi



router = routers.SimpleRouter()
router.register(r'feedbacks', feedbacksApi)
router.register(r'members'  , membersApi )
router.register(r'projects' , AllProjectsApi)
router.register(r'services' , ServicesApi)





urlpatterns = [
    # path('admin/', admin.site.urls),
    path('appadmin/', admin.site.urls),

    # api
    path('api/', include(router.urls)),
    path('get/', include('auth_token.api.urls')),
]
