from django.shortcuts import render,redirect
from.forms import PostCreateForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import PostModel

# Create post views here.
@login_required
def post_create(request):
    if request.method=='POST':
        form=PostCreateForm(data=request.POST)
        if form.is_valid():
            new_item=form.save(commit=False)
            new_item.user=request.user
            new_item.save()
    else:
        form=PostCreateForm(data=request.GET)
    return render(request,'posts/create.html',{'form':form})    


# feed page view
@login_required
def feedPage(request):
    if request.method=='POST':
        commnet_form=CommentForm(data=request.POST)
        new_comment=commnet_form.save(commit=False)
        post_id=request.POST.get('post_id')
        post=get_object_or_404(PostModel,id= post_id)
        new_comment.post=post
        new_comment.save()
    else:
        commnet_form=CommentForm()
    posts=PostModel.objects.all()
    logged_user=request.user
    return render(request,'posts/feed.html',{'posts':posts,'logged_user': logged_user,'comment_form':commnet_form})

# like view
def like_post(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(PostModel, id=post_id)
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
    return redirect('feed') 
