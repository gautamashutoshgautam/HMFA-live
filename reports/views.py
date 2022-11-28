from django.shortcuts import render
from django.http import HttpResponse
from . models import Exhibitions
from . models import Arts
from . forms import ExhibitionsForm
from . models import Bookings


def reports(request):
    context={
        
    }
    return render(request,'reports/reports_main_index.html',context)


def report_art(request):
    watercolor_no = Arts.objects.filter(art_type='watercolor').count()
    watercolor_no = int(watercolor_no)

    painting_no = Arts.objects.filter(art_type='Painting').count()
    painting_no = int(painting_no)

    gelatin_silver_no=  Arts.objects.filter(art_type='gelatin silver paint').count()
    gelatin_silver_no = int(gelatin_silver_no)

    oil_no=  Arts.objects.filter(art_type='Oil on Canvas').count()
    oil_no = int(oil_no)

    bronze_no=  Arts.objects.filter(art_type='Bronze').count()
    bronze_no = int(bronze_no)

    marble_no=  Arts.objects.filter(art_type='Marble').count()
    marble_no = int(marble_no)

    art_type_list = ['watercolor', 'painting', 'gelatin silver paint', 'Oil on Canvas', 'Bronze', 'Marble']
    art_type_no = [watercolor_no,painting_no,gelatin_silver_no,oil_no,bronze_no,marble_no]
   

    context = {'art_type_list': art_type_list, 'art_type_no': art_type_no}
    return render( request,'reports/report_art_index.html',context)


def report_bookings(request):
    pending_no = Bookings.objects.filter(status='Pending').count()
    pending_no= int(pending_no)

    booked_no = Bookings.objects.filter(status='Booked').count()
    booked_no = int(booked_no)

    processing_no = Bookings.objects.filter(status='Processing').count()
    processing_no = int(processing_no)

    status_list = ['Pending', 'Booked', 'Processing']
    status_no = [pending_no, booked_no, processing_no]
   
    context ={'status_list': status_list, 'status_no': status_no}

    return render(request,'reports/report_bookings_index.html',context)

def report_exhibitions(request):
   Y2003_no = Exhibitions.objects.filter(exhibition_year='2003').count()
   Y2003_no = int(Y2003_no)
   print ('Number of Exhibitions in 2003 is', Y2003_no) 

   Y2011_no = Exhibitions.objects.filter(exhibition_year='2011').count()
   Y2011_no = int(Y2011_no)
   print ('Number of Exhibitions in 2011 is', Y2011_no)

   Y2012_no = Exhibitions.objects.filter(exhibition_year='2012').count()
   Y2012_no = int(Y2012_no)
   print ('Number of Exhibitions in 2012 is', Y2012_no)
   
   Y2013_no = Exhibitions.objects.filter(exhibition_year='2013').count()
   Y2013_no = int(Y2013_no)
   print ('Number of Exhibitions in 2013 is', Y2013_no) 
  

   Y2015_no = Exhibitions.objects.filter(exhibition_year='2015').count()
   Y2015_no = int(Y2015_no)
   print ('Number of Exhibitions in 2015 is', Y2015_no)

   Y2016_no = Exhibitions.objects.filter(exhibition_year='2016').count()
   Y2016_no = int(Y2015_no)
   print ('Number of Exhibitions in 2016 is', Y2016_no)

   Y2018_no = Exhibitions.objects.filter(exhibition_year='2018').count()
   Y2018_no = int(Y2018_no)
   print ('Number of Exhibitions in 2018 is', Y2018_no)

   
   exhibition_year_list = ['2003','2011','2012','2013','2015','2016', '2018']
   exhibition_number_list = [Y2003_no, Y2011_no, Y2012_no, Y2013_no, Y2015_no, Y2016_no, Y2018_no]
   
   form = ExhibitionsForm()
   print(dir(form))
   context = {'exhibition_year_list': exhibition_year_list, 'exhibition_number_list': exhibition_number_list,'form':form}

   if request.method == 'POST':
       
        if request.method == 'POST':
             form =ExhibitionsForm(request.POST)
             if form.is_valid():
                exhibition_year = form.data.get('exhibition_year')
                form.save()
               
             else:
                 form = ExhibitionsForm()
   return render( request,'reports/reports_exhibitions_index.html',context)

