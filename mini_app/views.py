from django.shortcuts import render, redirect

from mini_app.forms import reg_form


# Create your views here.
def todo(request):
    return render(request,'index.html')
def notify(request):
    data=reg_form()
    if request.method =='POST':
        obj=reg_form(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect("/")
    return render(request,'registration.html',{'regkey':data})
