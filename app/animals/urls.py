from django.urls import include, path

from rest_framework.routers import SimpleRouter

from . import apis

router = SimpleRouter()
router.register('images', apis.AnimalImageViewSet)

urlpatterns = [
    path('', include(router.urls))

]
