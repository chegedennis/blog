from django.shortcuts import render,get_object_or_404, HttpResponseRedirect,redirect
from django.db.models import Q
from .models import Article, Category, Comment
from .forms import CommentForm,ContactForm


recent_article = Article.objects.first()
popular_articles = Article.objects.all()[4:7]
categories = Category.objects.all()
form = ContactForm()

def index(request):
    articles = Article.objects.all()
    context = {"articles": articles, "recent_article":recent_article, 'categories':categories,'popular_articles':popular_articles,"contactform":form}
    return render(request, 'blog/index.html', context)

def article(request, category_slug, slug):
    article = get_object_or_404(Article,slug=slug)
    category = get_object_or_404(Category, slug=category_slug)
    related_articles = category.articles.all()[1:3]

    ### check errors here ###

    comments = article.comments.filter(active=True, parent__isnull=True)
    if request.method == 'POST':
        #comment has been added
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            # get parent comment id from hidden input
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exists
                if parent_obj:
                    # create reply comment object
                    reply_comment = comment_form.save(commit=False)
                    # assign parent_obj to reply comment
                    reply_comment.parent = parent_obj
            #normal comment
            # create comment object but do not save to database
            new_comment = comment_form.save(commit=False)
            # assign ship to the comment
            new_comment.article = article
            # save
            new_comment.save()
            return HttpResponseRedirect(article.get_absolute_url())
    else:
        comment_form = CommentForm()


    ### errors end here###
    
    context = {'article': article, "recent_article":recent_article, "related_articles":related_articles, 'categories':categories, 'popular_articles':popular_articles
    , 'comments':comments, 'comment_form':comment_form,"contactform":form}
    return render(request, 'blog/article.html', context)

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    category_articles = category.articles.all()
    context = {'category_articles': category_articles, 'categories':categories,"recent_article":recent_article, 'popular_articles':popular_articles,"contactform":form}
    return render(request, 'blog/category.html', context)

def search(request):
    query = request.GET.get('query', '')
    search_articles = Article.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    print(search_articles)
    context = {'search_articles':search_articles, "recent_article":recent_article, 'popular_articles':popular_articles,"contactform":form}
    return render(request, 'blog/search.html', context)


 