from config.urls.base import *

urlpatterns += path('admin/', include('admin_honeypot.urls',
                                      namespace='admin_honeypot')),
