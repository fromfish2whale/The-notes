from django.shortcuts import render,redirect, get_object_or_404
from .models import blank_for_notes
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add_note(request):
    if request.method =="POST":
        date = request.POST['date']
        title = request.POST['title']
        description = request.POST['description']
    
    if date == "":
        return render(request, "home.html")
    else:
        blank = blank_for_notes.objects.create(date = date,title = title, description = description)
    return redirect('notes_list')



def notes_list(request):
    list_data = blank_for_notes.objects.all()
    return render(request, 'notes_list.html', {'list_data':list_data})

def delete_data(request, pk):
    data = get_object_or_404(blank_for_notes,pk = pk)
    if request.method == "POST":
        data.delete()
        return redirect('notes_list')
    return redirect('notes_list')