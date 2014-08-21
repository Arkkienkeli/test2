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
    url(r'^products/$', 'test2.views.product_list'),
    url(r'^products/category/(?P<slug>[\w-]+)/$', 'test2.views.products_by_category',
    	name='products_by_category'),
	url(r'^products/test_case/$', 'test2.views.products_test_case', 
		name="test_case"),

    url(r'^trademark/(?P<slug>[\w-]+)/$', 'test2.views.trademark_details', 
    	name="trademark"),

    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
