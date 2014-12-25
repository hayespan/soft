#coding: utf-8
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'soft.views.home', name='home'),
    # url(r'^soft/', include('soft.foo.urls')),
    #主页
    url(r'^$',TemplateView.as_view(template_name="home.html")),
    # 第一注册页
    url(r'^register$', 'guest.views.register_page'),
    # 买家信息注册页
    url(r'^register/buyer$','guest.views.register_page2'),
    # 卖家信息注册页
    url(r'^register/seller$', 'guest.views.register_page3'),
    # 注册成功页
    url(r'^register/success$', TemplateView.as_view(template_name="register4.html")),

    url(r'^login$', 'guest.views.login'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # 配置media文件访问
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT},
            ), 
    )
