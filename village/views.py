from django.shortcuts import render,redirect
from .forms import ProfileForm,EventsForm ,HoodForm ,BusinessForm
from  .models import Profile,Events,User,Village,Business
from django.contrib.auth.decorators import login_required


def hood(request):
    # events = Events.objects.all()
    hoods = Village.objects.all()
    return render(request, 'home.html',{'hoods':hoods})

@login_required(login_url='/accounts/login/')       
def new_events(request):
    current_user = request.user
    events = Events.objects.all()
    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('events')

    else:
        form = EventsForm()
    return render(request, 'event.html', {"form": form,'events':events})

@login_required(login_url='/accounts/login/')       
def events(request):
    events = Events.objects.all()
    return render(request, 'villageevent.html',{'events':events})


@login_required(login_url='/accounts/login/')       
def new_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.save()
        return redirect('business')

    else:
        form = BusinessForm()
    return render(request, 'business.html', {"form": form})

@login_required(login_url='/accounts/login/')       
def business(request):
    business = Business.objects.all()
    return render(request, 'buz.html',{'business':business})



@login_required(login_url='/accounts/login/')       
def hoods(request):
    current_user = request.user
    if request.method == 'POST':
        form = HoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
            hood.save()
        return redirect('index')

    else:
        form = HoodForm()
    return render(request, 'new.html', {"form": form})




@login_required(login_url='/accounts/login/')
def profile(request, profile_id):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.save()
            return redirect('index')

    else:
        form = ProfileForm()
    username=User.objects.all()    
    profiles = Profile.objects.filter(username = current_user)  
    
    return render(request, 'profile.html', {"form": form, "username": username,"profiles": profiles}) 

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user=request.user

    if request.method =='POST':
        
        if Profile.objects.filter(username_id=current_user).exists():
            form = ProfileForm(request.POST,request.FILES,instance=Profile.objects.get(username_id = current_user))    
        else:
            form=ProfileForm(request.POST,request.FILES)   
           
        if form.is_valid():
            profile=form.save(commit=False)
            profile.username=current_user
            profile.save()
            return redirect('profile', current_user.id)    
     
    else:
        if Profile.objects.filter(username_id = current_user).exists():
            form=ProfileForm(instance =Profile.objects.get(username_id=current_user))
        else:
            form=ProfileForm()     
            
    return render(request,'edit_profile.html',{"form":form})


@login_required(login_url='/accounts/login/')
def search_business(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        business =Business.search_business(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"business":business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
