from django.shortcuts import render

# Create your views here.
def token_crawler(request):
	return render(request, 'token.html')