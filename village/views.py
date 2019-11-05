from django.shortcuts import render,redirect
from .forms import ProfileForm,EventsForm
from  .models import Profile,Events,User
from django.contrib.auth.decorators import login_required
def hood(request):
    events = Events.objects.all()
    return render(request, 'home.html',{'events':events})

@login_required(login_url='/accounts/login/')       
def events(request):
    current_user = request.user
    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('index')

    else:
        form = EventsForm()
    return render(request, 'event.html', {"form": form})