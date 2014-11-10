from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from fig_demo.apps.page.api import PageAPIView


admin.autodiscover()

router = DefaultRouter()
router.register(r'page', PageAPIView, base_name='page')


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    # Examples:
    # url(r'^$', 'fig_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^api/', include(router.urls)),

)
