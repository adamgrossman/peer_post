import facebook
from django.shortcuts import render, redirect
from feed.forms import CustomUserCreationForm


def index(request):
    if request.user.is_authenticated():
        user_social_auth = request.user.social_auth.filter(provider='facebook').first()
        if user_social_auth is not None:
            graph = facebook.GraphAPI(user_social_auth.extra_data['access_token'])
            profile_data = graph.get_object("me")
            picture_data = graph.get_object("me/picture")
            data = {
                'profile': profile_data,
                'profile_photo': picture_data,
                'user_id': request.user.id
            }
            return render(request, 'index.html', data)
        else:
            data = {
                'profile_photo': request.user.profile_photo,
                'user_id': request.user.id
            }
            return render(request, 'index.html', data)
    else:
        return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            if form.save():
                return redirect('login')
    else:
        form = CustomUserCreationForm()
    data = {'form': form}
    return render(request, 'registration/register.html', data)
