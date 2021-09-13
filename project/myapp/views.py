from django.shortcuts import redirect, render
from rest_framework import generics
from django.http import HttpResponse
from .models import *
from .serializers import *
from .forms import *

class API_objects(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def newpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('/')
        else:
            return HttpResponse('Bad Request')
    else:
         form = PostForm()
         ctx = {'form': form}
         return render(request, 'newpost.html', ctx)
            

