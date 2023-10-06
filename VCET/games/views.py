from django.shortcuts import render

# Create your views here.

def story(request):
    return render(request, 'story.html')


def learn(request):
    return render(request, 'learn.html')