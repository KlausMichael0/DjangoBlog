from django.shortcuts import render
from .models import ArticlePost

def article_list(request):
	articles = ArticlePost.objects.all()
	context = { 'articles': articles }
	return render(request, 'article/list.html', context)

def article_detail(request, id):
	article = ArticlePost.objects.get(id=id)

	article.body = markdown.markdown(article.body,
		ectensions=[
		'markdown.ectensions.extra',
		'markdown.ectensions.codehilite',
		])

	context = { 'article': article }
	return render(request, 'article/detail.html', context)