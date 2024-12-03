from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def veg(request):
    return HttpResponse(''' 
   <center>
        <h1>Veg Items </h1>       
        <h2>Vegetable Biriyani</h2>
        <h2>Paneer Tikka</h2> 
        <h2>Gobi Manjurian</h2>
        <h2>Masala Dosa</h2>               
                         <center>
      
''')

def nonveg(request):
    return render(request,'nonveg.html')


