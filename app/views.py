from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
  
def display_topic(request):
    LOT=Topic.objects.all()
    d={'topic':LOT}
    return render(request,'display_topic.html',context=d)
def display_webpagee(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='cricket')
    LOW=Webpage.objects.filter(topic_name='chess')
    LOW=Webpage.objects.exclude(topic_name='cricket')
    LOW=Webpage.objects.all()[1:4:]
    LOW=Webpage.objects.all().order_by('name')
    LOW=Webpage.objects.all().order_by('-name')
    LOW=Webpage.objects.all().order_by(Length('name'))
    LOW=Webpage.objects.all().order_by(Length('name').desc())
    LOW=Webpage.objects.all().filter(name__startswith='k')
    LOW=Webpage.objects.all().filter(url__endswith='.com')
    LOW=Webpage.objects.all().filter(name__contains='i')
    LOW=Webpage.objects.all().filter(name__in=('dhoni','kohli'))
    LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{7}')
    LOW=Webpage.objects.filter(Q(name='dhoni')& Q(topic_name='cricket'))
    LOW=Webpage.objects.filter( Q(topic_name='cricket'))
    d={'webpages':LOW}
    return render(request,'display_webpagee.html',d)
def display_access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2023-01-16')
    LOA=AccessRecord.objects.filter(date__gte='2023-01-16')
    LOA=AccessRecord.objects.filter(date__lt='2023-03-8')
    LOA=AccessRecord.objects.filter(date__lte='2023-03-16')
    LOA=AccessRecord.objects.filter(date__gt='2023-01-16')
    LOA=AccessRecord.objects.filter(date__month='01')
    LOA=AccessRecord.objects.filter(date__year='2023')
    LOA=AccessRecord.objects.all()
    
    d={'access':LOA}
    return render(request,'display_access.html',d)
    return render(request,'display_webpagee.html',d)
def display_update(request):
    AccessRecord.objects.filter(name=1).update(author='virat')
    
    LOA=AccessRecord.objects.all()
    AccessRecord.objects.filter(name=2).update(author='kiran')
    LOA=AccessRecord.objects.all()
    d={'access':LOA}
    return render(request,'display_access.html',d)
def display_wupdate(request):
    
    Webpage.objects.filter(name='kohli').update(url='http://kohli.com')
    LOW=Webpage.objects.all()
    d={'webpages':LOW}
    return render(request,'display_webpagee.html',d)




def display_webupdate(request):
    To=Topic.objects.get_or_create(topic_name='rubby')[0]
    To.save()
   
    Webpage.objects.update_or_create(topic_name=To,name='kranthi',url='http://kranthi.com',	email='rubbykranthin@gmail.com')
    LOW=Webpage.objects.all()
    d={'webpages':LOW}
    return render(request,'display_webpagee.html',d)