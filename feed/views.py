from django.shortcuts import render, redirect
from feed.forms import CustomUserCreationForm


def index(request):
    # data = {'logged_in_user': request.user}
    # return render(request, 'index.html', data)
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            if form.save():
                return redirect('index')
    else:
        form = CustomUserCreationForm()
    data = {'form': form}
    return render(request, 'registration/register.html', data)

