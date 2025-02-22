from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import choose_form
from .models import Images

def filechooser(request):
    form = choose_form()
    return render(request=request, template_name='main.html', context={'form': form})

def saver(request):
    if request.method == 'POST':
        form = choose_form(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            name = form.cleaned_data['name']
            
            try:
                image_instance = Images(name=name, image=image)
                image_instance.save()
                return HttpResponseRedirect("/upload")
            except Exception as e:
                return HttpResponse(f"Saving faild")
        else:
            return HttpResponse("Not Valid Form")
    return HttpResponse("Not Valid Request")

def show_images(request):
    images = Images.objects.all()
    return render(request, 'show_images.html', {'images': images})
