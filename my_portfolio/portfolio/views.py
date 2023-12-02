from django.shortcuts import render,HttpResponseRedirect,redirect

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def skill(request):
    return render(request,'skill.html')

def contact(request):
    return render(request,'contact.html')

def project(request):
    return render(request,'project.html')

def certificate(request):
    return render(request,'certificate.html')

def hire(request):
    return render(request,'hire.html')

# color: #666666;
# todo project ==========================================================================================================
def card(request):
    return render(request,'card.html')

def data(request):
    return render(request,'data.html')


# todo student marks prediction ===========================================================================================
def value(request):
    return render(request,'value.html')



# todo project page =====================================================================================================



