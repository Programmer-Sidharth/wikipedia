from django.shortcuts import render, redirect
import wikipedia
# Create your views here.
def home(request):
    context = {'title':'Home'}
    return render(request, 'home.html', context)

def results(request):
    try:
        if request.method == 'POST':
            topic = request.POST['topic']
            data = wikipedia.summary(topic)
            context = {'data':data, 'title':topic}
        else:
            context = {'data':'page does not exist', 'title':'Does Not Exist!'}
    except Exception as e:
        context = {'data':e}
    return render(request, 'results.html', context)
