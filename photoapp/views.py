from django.shortcuts import render, redirect
from django.contrib import messages
from photoapp.models import PhotoModel
from photoapp.forms import PhotoForm


def home_page(request):

    context = {"gallery": PhotoModel.objects.all()}
    return render(request, 'home.html', context)


def redirect_home(request):
    """ retdirects empty url to home page """
    return redirect('/home/')


def detailed_view(request, id=None):
    
    context = {"image": PhotoModel.objects.get(id=id)}

    return render(request, template_name='detailed.html', context=context)


def create_post(request):
    if request:
        print(request.method)
    if request.method == "POST":
        print("POSTING...", request.POST)
        form = PhotoForm(data=request.POST, files=request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.save()
            messages.success(request, "Data Saved successfully")

            return redirect('/home/')

    form = PhotoForm()
    context = {"create_form": form}

    return render(request, 'create.html', context)

    