from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group 

from .models import *
from .forms import ArtsForm, BookingsForm, CreateUserForm, ExhibitionsForm, MembersForm
from .filters import ArtsFilter, BookingsFilter, ExhibitionsFilter
from .decorators import unauthenticated_user, allowed_users, admin_only


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='members')
            user.groups.add(group)
            Members.objects.create(
                member = user,
            )

            messages.success(request, 'Account was sucessfully created for ' + username)

            return redirect('login')
    context= {'form':form}
    return render (request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect ')
    context= {}
    return render (request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect ('login')

@login_required(login_url='login')
@admin_only
def home(request):
    bookings = Bookings.objects.all()
    members = Members.objects.all()

    #total_members = members.count()
    total_bookings = bookings.count()
    booked = bookings.filter(status='Booked').count()
    pending = bookings.filter(status='Pending').count()
    context = {'bookings':bookings, 'member':members,'total_bookings':total_bookings,'booked':booked,'pending':pending }
    #'total_members':total_members
    
    return render(request,'accounts/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['members'])
def userPage(request):
    booking = request.user.members.bookings_set.all()
    total_bookings = booking.count()
    booked = booking.filter(status='Booked').count()
    pending = booking.filter(status='Pending').count()
    print('BOOKINGS:', booking)
    
    context = {'booking':booking,'total_bookings':total_bookings,'booked':booked,'pending':pending  }
    return render (request, 'accounts/user.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['members'])
def accountSettings(request):
    members = request.user.members
    form = MembersForm(instance=members)
    if request.method == 'POST':
        form = MembersForm(request.POST, request.FILES, instance=members)
        if form.is_valid():
            form.save()
    
    
    context = {'form':form}
    return render(request, 'accounts/account_settings.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def ticket(request):
     ticket = Ticket.objects.all()
     return render(request,'accounts/ticket.html',{'ticket':ticket})

def museum(request):
     return render(request,'accounts/museum.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def members(request, pk):
    members = Members.objects.get(member_id = pk)
    booking = members.bookings_set.all()
    bookings_count = booking.count()
    myFilter = BookingsFilter(request.GET, queryset=booking)
    booking = myFilter.qs
    context = {'members':members,'booking':booking,'bookings_count':bookings_count, 'myFilter':myFilter}
    return render(request,'accounts/members.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createBookings(request, pk):
    BookingsFormSet = inlineformset_factory(Members, Bookings, fields=('ticket','status', 'bookings_id'), extra=10) 
    member = Members.objects.get(member_id= pk)
    formset = BookingsFormSet(queryset=Bookings.objects.none(), instance = member)
    #form = BookingsForm( initial={'member':members})
    if request.method == 'POST':
        #print('Printing POST:',request.POST)
        #form = BookingsForm(request.POST)
        formset = BookingsFormSet(request.POST, instance = member)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}
    return render(request,'accounts/bookings_form.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateBookings(request, pk_test):
    bookings = Bookings.objects.get(bookings_id=pk_test)
    form = BookingsForm(instance = bookings)
    if request.method == 'POST':
        form = BookingsForm(request.POST,instance = bookings)
        if form.is_valid():
            form.save()
        return redirect('/')
    context ={'form':form}
    return render (request, 'accounts/bookings_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteBookings (request, pk_test):
    bookings = Bookings.objects.get(bookings_id=pk_test)
    if request.method == "POST":
        bookings.delete()
        return redirect('/')
    context = {'item':bookings}
    return render(request, 'accounts/delete.html', context)
    
@login_required(login_url='login')
def arts(request):
    exhibitions = Exhibitions.objects.all()
    arts = Arts.objects.all()
    myFilter2 = ExhibitionsFilter(request.GET, queryset=exhibitions)
    exhibitions = myFilter2.qs
    myFilter1 = ArtsFilter(request.GET, queryset=arts)
    arts = myFilter1.qs
    context = {'exhibitions': exhibitions, 'arts':arts, 'myFilter1':myFilter1, 'myFilter2':myFilter2}
    return render (request,'accounts/arts.html', context) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin']) 
def createArts(request):
    form_arts = ArtsForm()
    if request.method == 'POST':
       form_arts = ArtsForm(request.POST)
       if form_arts.is_valid():
        form_arts.save()
        return redirect('arts')
    context ={'form_arts':form_arts}
    return render(request, 'accounts/arts_form.html',context) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateArts(request, pk_test):
    arts = Arts.objects.get(art_piece_id=pk_test)
    form_arts = ArtsForm(instance = arts)
    if request.method == 'POST':
        form_arts = ArtsForm(request.POST,instance = arts)
        if form_arts.is_valid():
            form_arts.save()
        return redirect('arts')
    context ={'form_arts':form_arts}
    return render (request, 'accounts/arts_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteArts (request, pk_test):
    arts = Arts.objects.get(art_piece_id=pk_test)
    if request.method == "POST":
        arts.delete()
        return redirect('arts')
    context = {'item':arts}
    return render(request, 'accounts/delete_arts.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createExhibitions(request):
    form_exhibitions = ExhibitionsForm()
    if request.method == 'POST':
       form_exhibitions = ExhibitionsForm(request.POST)
       if form_exhibitions.is_valid():
        form_exhibitions.save()
        return redirect('arts')
    context ={'form_exhibitions':form_exhibitions}
    return render(request, 'accounts/exhibitions_form.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateExhibitions(request, pk_test):
    exhibitions = Exhibitions.objects.get(exhibition_id=pk_test)
    form_exhibitions = ExhibitionsForm(instance = exhibitions)
    if request.method == 'POST':
        form_exhibitions = ExhibitionsForm(request.POST,instance = exhibitions)
        if form_exhibitions.is_valid():
            form_exhibitions.save()
        return redirect('arts')
    context ={'form_exhibitions':form_exhibitions}
    return render (request, 'accounts/exhibitions_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteExhibitions(request, pk_test):
    exhibitions = Exhibitions.objects.get(exhibition_id=pk_test)
    if request.method == "POST":
        exhibitions.delete()
        return redirect('arts')
    context = {'item':exhibitions}
    return render(request, 'accounts/delete_exhibitions.html', context)

@login_required(login_url='login')
def artworks(request):
    return render(request, 'accounts/artworks.html')

def about(request):
    return render(request, 'accounts/about.html')


