from django.shortcuts import render

# Create your views here.
def homepage_view(request):
    return render(request,'myapp/home.html')
def movienews_view(request):
    news1 = "salman is bussy in bharat movie shooting"
    news2 = "sonali slowely getting curing"
    news3 = "Akshaykumar replace by rushi kappor"

    my_dict = {'news1':news1,'news2':news2,'news3':news3}

    return render(request,'myapp/mnews.html',my_dict)

    #myapp/mnews.html :- is pointing to thw template/myapp/mnews.html
def sportsnews_view(request):
    news1 = "Ajinkya is play against Australiya"
    news2 = "Virat was not played against newzeland"
    my_dict = {'news1':news1,"news2":news2}

    return render(request,'myapp/snews.html',my_dict)

def Politicsnews_view(request):
    n1h1 = "We accuse each other, but remain friends: Sonia Gandhi"
    n1p1 = "Constituents of the anti-BJP opposition alliance nationally, the Congress and the TMC gave conflicting signals to each other throughout much of Wednesday"

    n2h2 = "Say sorry, BJP tells Rahul Gandhi who points to dissent note "
    n2p2 = "The Congress and BJP traded charges over the CAG’s findings on the Rafale deal in its report to Parliament Wednesday."

    my_dict = {'news1':n1h1,'news2':n1p1,'news3':n2h2,'news4':n2p2}

    return render(request,'myapp/pnews.html',my_dict)
