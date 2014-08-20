from django.conf.urls import patterns, include, url

from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', 'test2.views.product_list'),
    url(r'^trademark/(?P<id>[0-9]+)/$', 'test2.views.trademark_details'),
    #url(r'^products/category/')
    #url(r'^products/test_case/'')

    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
