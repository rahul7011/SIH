
from django.shortcuts import render
from django.urls import reverse_lazy
from accounts.forms import RegisterForm
from django.views.generic.edit import CreateView

def dashboard(request):
    return render(request, "SIHdemo/html/Homepage.html")

# class SignUp(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"

def Faq(request):
    return render(request, "faq/index.html")


# def note_list_view(request):
#     return render(request, "note_list.html", context)

# def finish_item(request,id):
#     note=get_object_or_404(Note,id=id)
#     note.finished=True
#     note.save()
#     return redirect('note-list')

# def recover_item(request,id):
#     note=get_object_or_404(Note,id=id)
#     note.finished=False
#     note.save()
#     return redirect('note-list')

# def delete_item(request,id):
#     note=get_object_or_404(Note,id=id)
#     note.delete()
#     return redirect('note-list')