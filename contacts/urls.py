from rest_framework import routers

from contacts.views import ContactView

router = routers.DefaultRouter()
router.register('', ContactView)
urlpatterns = router.urls
