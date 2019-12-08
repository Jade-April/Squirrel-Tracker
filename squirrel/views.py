from django.shortcuts import render
from .models import Squirrel
import random

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

def get_map(request):
    squirrel=Squirrel.objects.all()
    myitems=[]
    for i in range(50):
        j=random.randint(0,len(squirrel))
        item=list(squirrel)[j]
        item_list=[float(item.Longitude),float(item.Latitude)]
        myitems.append(item_list)
    title='squirrel map'
    context={
            'title':title,
            'myItems':myitems,
            }
    return render(request,'squirrel/address.html',context)
# Create your views here.
