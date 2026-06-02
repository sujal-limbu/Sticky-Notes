from django.shortcuts import render,redirect,get_object_or_404
from .models import Note

# Create notes

def create_note(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')

        Note.objects.create(title=title,desc=desc)

        return redirect('note-list')

    return render(request,'core/create_note.html')

# Display notes

def note_list(request):

    note = Note.objects.filter(is_deleted = False)
    return render(request ,'core/note_list.html',{'note':note})

# Update notes

def note_update(request,id):

    note = get_object_or_404(Note,id=id)

    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.desc = request.POST.get('desc')
        note.save()

        return redirect("note-list")

    return render(request, "core/update_note.html", {"note": note})

# Delete notes

def delete_note(request, id):
    note = get_object_or_404(Note, id=id)
    note.is_deleted = True
    note.save()
    return redirect('note-list')



