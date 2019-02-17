from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeView, name='home'),
    path('UserPrivacyPolicy', UserPrivacyPolicy, name='UserPrivacyPolicy'),
    path('TermsConditions', TermsConditions, name='TermsConditions'),
    path('AuthorPrivacyPolicy', AuthorPrivacyPolicy, name='AuthorPrivacyPolicy'),
]