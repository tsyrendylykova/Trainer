from django.shortcuts import render

def trainer(request):
    return render(request, 'trainer/trainer.html', {})
