from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Product
from .forms import ProductForm


# Create your views here.
class create_view(View):
    template_name = 'app1/create.html'
    form = ProductForm
    def get(self,request):
        form= self.form()
        context = {"form":form}
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        return render(request,self.template_name,{"form":form})

class Show_view(View):
    template_name = "app1/show.html"
    form = ProductForm

    def get(self, request):
        form = self.form()
        obj = Product.objects.all()
        context = {"obj":obj, "form": form}
        return render(request, self.template_name, context)

    def post(self, request,*args,**kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        return render(request, self.template_name, {"form":form})

class Update_view(View):
    template_name = "app1/create.html"
    form = ProductForm

    def get(self, request, pk):
        obj = Product.objects.get(id=pk)
        form = ProductForm(request.POST,instance=obj)
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        template_name = "app1/create.html"
        obj = Product.objects.get(id=pk)
        form = ProductForm(request.POST, instance=obj)
        context = {"form": form}
        if form.is_valid():
            form.save()
            return redirect("show_url")
        return render(request, template_name, context)

class Cancel_view(View):
    template_name = "app1/confirm.html"
    form = ProductForm

    def get(self, request, pk):
        obj = Product.objects.get(id=pk)
        form = self.form(request.POST,instance=obj)
        context = {"obj": obj, "form": form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        obj = Product.objects.get(id=pk)
        obj.delete()
        return redirect("show_url")