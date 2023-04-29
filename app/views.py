from django.shortcuts import render

# Create your views here.
def filters(request):
    d={'data':'shAhIDa  Is A BeaUTiFuL GIrL'}
    return render(request,'filters.html',d)