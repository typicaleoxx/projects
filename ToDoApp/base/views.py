from django.shortcuts import render
from .models import ToDo


# Create your views here.
def index(request):
    ToDo_obj = ToDo.objects.all()
    data = {"todos": ToDo_obj}
    return render(request, "index.html", context=data)



def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        status = request.POST.get("status")
        ToDo.objects.create(name=name, description=description, status=status)
    return render(request, "create.html")
