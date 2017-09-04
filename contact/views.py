from django.shortcuts import render
from contact.forms import UserForm
# Create your views here.
def index(request):
    return render(request,'contact/index.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'contact/index.html')
    else:
        form = UserForm()
        return render(request, 'contact/registration.html', {'form': form})
