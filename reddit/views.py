from django.shortcuts import render
from .models import reddit
from .forms import redditForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def index(request):
  return render(request, 'index.html')


def reddit_list(request):
  reddits = reddit.objects.all().order_by('-created_at')
  return render(request, 'reddit_list.html', {'reddits': reddits})

@login_required
def reddit_create(request):
  if request.method == "POST":
    form = redditForm(request.POST, request.FILES)
    if form.is_valid():
      reddit = form.save(commit=False)
      reddit.user = request.user
      reddit.save()
      return redirect('reddit_list')
  else:
    form = redditForm()
  return render(request, 'reddit_form.html', {'form': form})

@login_required
def reddit_edit(request, reddit_id):
  reddit = get_object_or_404(reddit, pk=reddit_id, user = request.user)
  if request.method == 'POST':
    form = redditForm(request.POST, request.FILES, instance=reddit)
    if form.is_valid():
      reddit = form.save(commit=False)
      reddit.user = request.user
      reddit.save()
      return redirect('reddit_list')
  else:
    form = redditForm(instance=reddit)
  return render(request, 'reddit_form.html', {'form': form})

@login_required
def reddit_delete(request, reddit_id):
  reddit = get_object_or_404(reddit, pk=reddit_id, user = request.user)
  if request.method == 'POST':
    reddit.delete()
    return redirect('reddit_list')
  return render(request, 'reddit_confirm_delete.html', {'reddit': reddit})
  

def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password1'])
      user.save()
      login(request, user)
      return redirect('reddit_list')
  else:
    form = UserRegistrationForm()

  return render(request, 'registration/register.html', {'form': form})