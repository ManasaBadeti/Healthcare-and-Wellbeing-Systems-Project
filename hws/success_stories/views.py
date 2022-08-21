from django.shortcuts import render
from .models import Success_Stories
# Create your views here.
def stories_view(request):
    stories = Success_Stories.objects.all()
    return render(request, 'success_stories/dss.html', {'stories': stories})



def enterstories_view(request):
    return render(request,"success_stories/ss.html")

def enter_stories(request):
   title = request.POST['title']
   body = request.POST['body']

   obj=Success_Stories(title=title, body=body)
   obj.save()

   stories = Success_Stories.objects.all().order_by('date')
   return render(request, 'success_stories/dss.html', {'stories': stories})





