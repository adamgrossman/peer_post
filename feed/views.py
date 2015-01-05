from django.shortcuts import render


def index(request):
    # data = {'logged_in_user': request.user}
    # return render(request, 'index.html', data)
    return render(request, 'index.html')
