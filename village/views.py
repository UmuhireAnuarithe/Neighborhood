from django.shortcuts import render
from django.contrib.auth.decorators import login_required
def hood(request):
    return render(request, 'village.html')

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