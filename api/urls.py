from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .views import *

from rest_auth.views import PasswordResetConfirmView

from rest_framework.generics import ListCreateAPIView
from .serializers import UserSerializer


router = DefaultRouter()
router.register('user-blog', BlogViewSet, base_name='user-blog')
router.register('user-detail', DetailViewSet, base_name='user-detail')

router.register('facebookreport', FacebookReportViewSet, base_name='facebookreport')
router.register('twitterreport', TwitterReportViewSet, base_name='twitterreport')
router.register('wordpressreport', WordpressReportViewSet, base_name='wordpressreport')

router.register('facebooktrending', FacebookTrendingViewSet, base_name='facebooktrending')
router.register('twittertrending', TwitterTrendingViewSet, base_name='twittertrending')
router.register('tumblrtrending', TumblrTrendingViewSet, base_name='tumblrtrending')
router.register('newstrending', NewsTrendingViewSet, base_name='newstrending')


urlpatterns = [
     url(r'^auth/', include('rest_auth.urls')),
     url(r'^rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),
     url(r'^auth/registration/', include('rest_auth.registration.urls')),
     url(r'^social-auth/', include('rest_framework_social_oauth2.urls')),
     url(r'^users/', ListCreateAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='user-list')


 ]

urlpatterns += router.urls

