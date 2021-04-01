from config.urls.base import *
from config.settings import local
from django.conf.urls.static import static

urlpatterns += static(local.STATIC_URL,
                      document_root=local.STATIC_ROOT)
urlpatterns += static(local.MEDIA_URL,
                      document_root=local.MEDIA_ROOT)
