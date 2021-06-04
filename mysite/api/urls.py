from django.urls import path
from . import views
from rest_framework import routers
from .api import TestViewSet

router = routers.DefaultRouter()

router.register('test', TestViewSet, 'test')

urlpatterns = router.urls


#urlpatterns = [
#    path('', views.TestView.as_view())
#]
