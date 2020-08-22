from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import BoastRoastForm
from .models import BoastRoast
from django.db.models import F

def index_view(request):
   post = BoastRoast.objects.order_by('-submissiondate')
   return render(request, 'index.html', {"posts": post})


def boast_view(request):
    post = BoastRoast.objects.filter(isroast=False).order_by('-submissiondate')
    return render(request, 'boast.html', {'posts': post}) 

def roast_view(request):
    post = BoastRoast.objects.filter(isroast=True).order_by('-submissiondate')
    return render(request, 'roast.html', {'posts': post})

def sort_view(request):
    post = BoastRoast.objects.order_by(
        -(F('upvotes') - F('downvotes'))
    )
    return render(request, 'sort.html', {'posts': post})

def createpost_view(request):
    if request.method == 'POST':
        form = BoastRoastForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BoastRoast.objects.create(isroast = data.get('isroast'),
            post_content = data.get('post_content'))
            return HttpResponseRedirect(reverse('home'))
    form = BoastRoastForm()
    return render(request, 'createpost.html', {"form": form})


def upvotes_view(request, post_id):
    post = BoastRoast.objects.get(id=post_id)
    post.upvotes = F('upvotes') + 1
    post.save()
    return HttpResponseRedirect(reverse('home'))

def downvote_view(request, post_id):
    post = BoastRoast.objects.get(id=post_id)
    post.downvotes = F('downvotes') + 1
    post.save()
    return HttpResponseRedirect(reverse('home'))