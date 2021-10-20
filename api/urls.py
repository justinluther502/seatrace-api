from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from athletes import views

router = routers.DefaultRouter()
router.register(r'rowers', views.RowerViewSet)
router.register(r'hulls', views.HullViewSet)
router.register(r'races', views.RaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
