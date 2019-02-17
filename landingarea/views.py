from django.shortcuts import render

# Create your views here.
def HomeView(request):
    return render(request, 'landingarea/index.html')

def UserPrivacyPolicy(request):
    return render(request, 'landingarea/user-privacy-policy.html')

def TermsConditions(request):
    return render(request, 'landingarea/terms-and-conditions.html')

def AuthorPrivacyPolicy(request):
    return render(request, 'landingarea/author-privacy-statement.html')
