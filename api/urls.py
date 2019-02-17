from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .views import *

from rest_auth.views import PasswordResetConfirmView



router = DefaultRouter()
router.register('user-blog', BlogViewSet, base_name='user-blog')
router.register('user-detail', DetailViewSet, base_name='user-detail')

urlpatterns = [
     url(r'^auth/', include('rest_auth.urls')),
     url(r'^rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),
     url(r'^auth/registration/', include('rest_auth.registration.urls')),
     url(r'^social-auth/', include('rest_framework_social_oauth2.urls')),
 ]

urlpatterns += router.urls

