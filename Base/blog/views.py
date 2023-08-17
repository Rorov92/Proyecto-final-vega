from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.


#esta funcion crea posts
@login_required
def home(request):
	posts = Post.objects.all()
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('home')
	else:
		form = PostForm()

	context = {'posts':posts, 'form' : form }
	return render(request, 'newsfeed.html', context) #cambiar template________________________________________*
 
#esta funcion borra posts
def delete(request, post_id):
	post = Post.objects.get(id=post_id)
	post.delete()
	return redirect('home')