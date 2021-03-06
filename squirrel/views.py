from django.shortcuts import render,redirect
from .models import Squirrel
import random
from django.http import HttpResponse
from .forms import SquirrelForm
from django.contrib import messages
from django.db.models import Avg,Max,Min,Count


def general_state(request):
    run=list(Squirrel.objects.values('Running').annotate(num_count=Count('Running')))
    shift=list(Squirrel.objects.values('Shift').annotate(num_count=Count('Shift')))
    primary_fur_color=list(Squirrel.objects.values('Primary_Fur_Color').annotate(num_count=Count('Primary_Fur_Color')))
    latitude=Squirrel.objects.aggregate(range_max=Max('Latitude'),range_min=Min('Latitude'))
    longitude=Squirrel.objects.aggregate(range_max=Max('Longitude'),range_min=Min('Longitude'))
    print(latitude.items())
    title='general state'
    context={
            'title':title,
            'run':run,
            'shift':shift,
            'primary_fur_color':primary_fur_color,
            'latitude':latitude,
            'longitude':longitude,
            }
    return render(request,'squirrel/stat.html',context)

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

def add(request):
    if request.method=='POST':
        form=SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/squirrel/sightings/')
    else:
        form=SquirrelForm()
    title='create new sightings'
    messages.success(request,'Now you can add a new squirrel')
    context={
            'title':title,
            'form':form,
            }
    return render(request,'squirrel/add.html',context)

def update(request,unique_squirrel_id):
    to_update=Squirrel.objects.get(Unique_Squirrel_ID=unique_squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=to_update)
        if form.is_valid():
           form.save()
           return redirect(f'/squirrel/sightings')
    else:
        form = SquirrelForm(instance=to_update)
    messages.success(request,'Now you can update this squirrel')
    context={
            'form':form,
            }
    return render(request,'squirrel/update.html',context)

# Create your views here.
