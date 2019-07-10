from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View

from Articles.forms import CommentForm
from .models import Articles, Classify, Comments
import markdown


class Detail(View):
    def get(self, request, aid):
        article = Articles.objects.get(id=aid)
        article.click_num = article.click_num + 1
        article.save()

        comment = Comments.objects.filter(article=article)
        classify = Classify.objects.all()

        article.content = markdown.markdown(article.content,
                                            extensions=[
                                                'markdown.extensions.extra',
                                                'markdown.extensions.codehilite',
                                                'markdown.extensions.toc',
                                            ], safe_mode=True, enable_attributes=False)

        return render(request, 'Art/detail.html', {'article': article, 'comments': comment, 'Classify': classify})


class Add_Comment(View):
    def post(self, request, aid):
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid() and aid:
            comment_content = form.cleaned_data['comment_content']
            comment_img = form.cleaned_data['comment_img']

            article = Articles.objects.get(pk=aid)

            comment = Comments()
            comment.comment_content = comment_content
            comment.comment_person = request.user
            comment.article = article
            comment.comment_img = comment_img
            comment.save()
            article.comment_num = article.comment_num + 1
            article.save()
            return redirect(reverse('articles:detail', args=[aid, ]))
