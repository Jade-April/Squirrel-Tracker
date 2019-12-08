from django.shortcuts import render
from .models import Squirrel


def list_sightings(request):
    squirrel=Squirrel.objects.all()
    link_list=[]
    for s in squirrel:
        link_list.append(s.Unique_Squirrel_ID)
    title='list of sightings'
    context={
            'title':title,
            'link_list':link_list,
            }
    return render(request,'squirrel/list.html',context)

# Create your views here.
