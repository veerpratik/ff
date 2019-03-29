from django.shortcuts import render
import datetime
# Create your views here.
def datetime_view(request):
    date = datetime.datetime.now()

    h = int(date.strftime('%H'))

    if h<12:
        msg='Hello Guest!!!! Very Good Morning'
    elif h<16:
        msg='Hello Guest!!!! Very Good Afternoon'
    elif h<21:
        msg='Hello Guest!!!! Very Good Evening'
    else:
        msg='Hello Guest!!!! Very Good Night'


    mydict = {'date':date,'msg':msg}


    return render(request,'myapp/result.html',mydict)
