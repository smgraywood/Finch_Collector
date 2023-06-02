from django.shortcuts import render
from .models import Finch

# Create your views here.
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates (.ejs extension)
    return render(request, 'home.html')

def about(request):
    # Include an .html file extension - unlike when rendering EJS templates (.ejs extension)
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})