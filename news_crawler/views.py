from django.shortcuts import render

# Create your views here.

def news_crawler(request):
	return render(request, 'news.html')

