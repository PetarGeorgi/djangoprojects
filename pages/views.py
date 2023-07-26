from django.http import HttpResponse
 
 
def homepageview(response):
    return HttpResponse("Hello World")
