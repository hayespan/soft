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
    url(r'^$', 'guest.views.home'),
    # 第一注册页
    url(r'^register$', 'guest.views.register_page'),
    # 买家信息注册页
    url(r'^register/buyer$','guest.views.register_page2'),
    # 卖家信息注册页
    url(r'^register/seller$', 'guest.views.register_page3'),
    # 注册成功页
    url(r'^register/success$', TemplateView.as_view(template_name="register4.html")),

    # profile相关
    url(r'^profile/(?P<userid>\d+)$', 'guest.views.profile'),
    url(r'^profile/resetpasswd$', 'guest.views.resetPassword'),
    url(r'^profile/modify/buyer$', 'guest.views.modifyBuyerProfile'),
    url(r'^profile/modify/seller$', 'guest.views.modifySellerProfile'),
    url(r'^item/add$','items.views.addItem'),
    url(r'^item/mote/add$', 'items.views.addMote'),

    # 登陆注销
    url(r'^login$', 'guest.views.user_login'),
    url(r'^logout$', 'guest.views.user_logout'),

    # 管理员
    url(r'^admin/', include(admin.site.urls)),

    # 临时
    url(r'^userpage1$', TemplateView.as_view(template_name='userpage1.html')),
)

if settings.DEBUG:
    # 配置media文件访问
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT},
            ), 
    )
