from django.shortcuts import render


def profile(request):
    """ Displays the users profile"""

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
