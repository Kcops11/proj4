import tempfile
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from boto3.dynamodb.conditions import Key, Attr
from django.conf import settings
from django.contrib.auth import login as auth_login
from PIL import Image, ImageOps, ImageFilter
from django.core.files.storage import FileSystemStorage
import pymysql
from django.http import HttpResponse
from django.template import loader
from django import forms
from collections import namedtuple
from .models import *
from django.shortcuts import render, get_object_or_404

conn = pymysql.connect(
        host="db422.czapl9tugwnt.us-east-2.rds.amazonaws.com",
        port=3306,
        user= 'admin',
        password= 'pH7fqHAnyvNY',
        db= 'user_db',
)



def home(request):
    template = loader.get_template('home.html')
    is_logged_in = request.session.get('is_logged_in', False)
    context = {
        'is_logged_in': is_logged_in,
        }
    return HttpResponse(template.render(context,request))


def sale(request):
    template = loader.get_template('sale.html')
    is_logged_in = request.session.get('is_logged_in', False)
    cars = getCarsTrucks()
    motorcycles = getmotorcycles()
    boats = getboats()
    books = getbooks()
    furniture = getfurniture()
    context = {
        'is_logged_in': is_logged_in,
        'cars':cars,
        'motorcycles': motorcycles,
        'boats' : boats,
        'books' : books,
        'furnitures' : furniture
        }
    return HttpResponse(template.render(context,request))


def house(request):
    template = loader.get_template('house.html')
    is_logged_in = request.session.get('is_logged_in', False)
    estate = getestate()
    swap = getswap()
    apt = getapts()
    parking = getparking()
    vacay = getvacay()
    context = {
        'is_logged_in': is_logged_in,
        'estates': estate,
        'swaps': swap,
        'apts': apt, 
        'parkings': parking,
        'vacays': vacay
        }
    return HttpResponse(template.render(context,request))


def service(request):
    template = loader.get_template('service.html')
    is_logged_in = request.session.get('is_logged_in', False)
    cleaning = getcleaning()
    lawn = getlawn()
    cardetail = getcardetail()
    pet = getpets()
    catering = getcatering()
    context = {
        'is_logged_in': is_logged_in,
        'cleanings': cleaning,
        'lawns': lawn,
        'cardetails': cardetail, 
        'pets': pet,
        'caterings': catering
        }
    return HttpResponse(template.render(context,request))



def job(request):
    template = loader.get_template('job.html')
    is_logged_in = request.session.get('is_logged_in', False)
    contract = getcontract()
    odd = getodd()
    full = getfull()
    part = getpart()
    manu = getmanu()
    context = {
        'is_logged_in': is_logged_in,
        'contracts': contract,
        'odds': odd,
        'fulls': full, 
        'parts': part,
        'manu': manu
        }
    return HttpResponse(template.render(context,request))


def community(request):
    template = loader.get_template('community.html')
    is_logged_in = request.session.get('is_logged_in', False)
    activity = getactivity()
    lost = getlost()
    child = getchild()
    ride = getride()
    volunteer = getvolunteer()
    context = {
        'is_logged_in': is_logged_in,
        'activitys': activity,
        'losts': lost,
        'childs': child, 
        'rides': ride,
        'volunteers': volunteer
        }
    return HttpResponse(template.render(context,request))


def carsTrucks(request):
    template = loader.get_template('carsTrucks.html')
    is_logged_in = request.session.get('is_logged_in', False)
    cars = getCarsTrucks()
    context = {
        'is_logged_in': is_logged_in,
        'cars': cars,
        }
    return HttpResponse(template.render(context,request))


def motorcycles(request):
    template = loader.get_template('motorcycles.html')
    is_logged_in = request.session.get('is_logged_in', False)
    motorcycles = getmotorcycles()
    context = {
        'is_logged_in': is_logged_in,
        'motorcycles': motorcycles,
        }
    return HttpResponse(template.render(context,request))


def boats(request):
    template = loader.get_template('boats.html')
    is_logged_in = request.session.get('is_logged_in', False)
    boats = getboats()  
    context = {
        'is_logged_in': is_logged_in,
        'boats': boats,
    }
    return HttpResponse(template.render(context, request))


def books(request):
    template = loader.get_template('books.html')
    is_logged_in = request.session.get('is_logged_in', False)
    books = getbooks()
    context = {
        'is_logged_in': is_logged_in,
        'books': books
        }
    return HttpResponse(template.render(context,request))


def furniture(request):
    template = loader.get_template('furniture.html')
    is_logged_in = request.session.get('is_logged_in', False)
    furniture = getfurniture()
    context = {
        'is_logged_in': is_logged_in,
        'furnitures': furniture
        }
    return HttpResponse(template.render(context,request))


def realEstate(request):
    template = loader.get_template('realEstate.html')
    is_logged_in = request.session.get('is_logged_in', False)
    estate = getestate()
    context = {
        'is_logged_in': is_logged_in,
        'estates': estate
        }
    return HttpResponse(template.render(context,request))


def swap(request):
    template = loader.get_template('swap.html')
    swap = getswap()
    is_logged_in = request.session.get('is_logged_in', False)
    context = {
        'is_logged_in': is_logged_in,
        'swap': swap
    }
    return HttpResponse(template.render(context, request))



def apts(request):
    template = loader.get_template('apts.html')
    is_logged_in = request.session.get('is_logged_in', False)
    apts = getapts()
    context = {
        'is_logged_in': is_logged_in,
        'apts': apts,
    }
    return HttpResponse(template.render(context, request))

def parking(request):
    template = loader.get_template('parking.html')
    is_logged_in = request.session.get('is_logged_in', False)
    parking = getparking()
    context = {
        'is_logged_in': is_logged_in,
        'parking': parking,
    }
    return HttpResponse(template.render(context, request))



def vacay(request):
    template = loader.get_template('vacay.html')
    is_logged_in = request.session.get('is_logged_in', False)
    vacay = getvacay()
    context = {
        'is_logged_in': is_logged_in,
        'vacay': vacay,
    }
    return HttpResponse(template.render(context, request))


def cleaning(request):
    template = loader.get_template('cleaning.html')
    is_logged_in = request.session.get('is_logged_in', False)
    cleaning = getcleaning()
    context = {
        'is_logged_in': is_logged_in,
        'cleaning': cleaning,
    }
    return HttpResponse(template.render(context, request))



def lawn(request):
    template = loader.get_template('lawn.html')
    is_logged_in = request.session.get('is_logged_in', False)
    lawn = getlawn()
    context = {
        'is_logged_in': is_logged_in,
        'lawn': lawn,
    }
    return HttpResponse(template.render(context, request))



def cardetail(request):
    template = loader.get_template('cardetail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    cardetail = getcardetail()
    context = {
        'is_logged_in': is_logged_in,
        'cardetail': cardetail,
    }
    return HttpResponse(template.render(context, request))



def pets(request):
    template = loader.get_template('pets.html')
    is_logged_in = request.session.get('is_logged_in', False)
    pets = getpets()
    context = {
        'is_logged_in': is_logged_in,
        'pets': pets,
    }
    return HttpResponse(template.render(context, request))



def catering(request):
    template = loader.get_template('catering.html')
    is_logged_in = request.session.get('is_logged_in', False)
    catering = getcatering()
    context = {
        'is_logged_in': is_logged_in,
        'catering': catering,
    }
    return HttpResponse(template.render(context, request))



def contract(request):
    template = loader.get_template('contract.html')
    is_logged_in = request.session.get('is_logged_in', False)
    contract = getcontract()
    context = {
        'is_logged_in': is_logged_in,
        'contract': contract,
    }
    return HttpResponse(template.render(context, request))



def odd(request):
    template = loader.get_template('odd.html')
    is_logged_in = request.session.get('is_logged_in', False)
    odd = getodd()
    context = {
        'is_logged_in': is_logged_in,
        'odd': odd,
    }
    return HttpResponse(template.render(context, request))



def full(request):
    template = loader.get_template('full.html')
    is_logged_in = request.session.get('is_logged_in', False)
    full = getfull()
    context = {
        'is_logged_in': is_logged_in,
        'full': full,
    }
    return HttpResponse(template.render(context, request))



def part(request):
    template = loader.get_template('part.html')
    is_logged_in = request.session.get('is_logged_in', False)
    part = getpart()
    context = {
        'is_logged_in': is_logged_in,
        'part': part,
    }
    return HttpResponse(template.render(context, request))



def manu(request):
    template = loader.get_template('manu.html')
    is_logged_in = request.session.get('is_logged_in', False)
    manu = getmanu()
    context = {
        'is_logged_in': is_logged_in,
        'manu': manu,
    }
    return HttpResponse(template.render(context, request))



def activity(request):
    template = loader.get_template('activity.html')
    is_logged_in = request.session.get('is_logged_in', False)
    activity = getactivity()
    context = {
        'is_logged_in': is_logged_in,
        'activity': activity,
    }
    return HttpResponse(template.render(context, request))



def lost(request):
    template = loader.get_template('lost.html')
    is_logged_in = request.session.get('is_logged_in', False)
    lost = getlost() #;)
    context = {
        'is_logged_in': is_logged_in,
        'lost': lost,
    }
    return HttpResponse(template.render(context, request))



def child(request):
    template = loader.get_template('child.html')
    is_logged_in = request.session.get('is_logged_in', False)
    child = getchild()
    context = {
        'is_logged_in': is_logged_in,
        'child': child,
    }
    return HttpResponse(template.render(context, request))


def ride(request):
    template = loader.get_template('ride.html')
    is_logged_in = request.session.get('is_logged_in', False)
    ride = getride()
    context = {
        'is_logged_in': is_logged_in,
        'ride': ride,
    }
    return HttpResponse(template.render(context, request))



def volunteer(request):
    template = loader.get_template('volunteer.html')
    is_logged_in = request.session.get('is_logged_in', False)
    volunteer = getvolunteer()
    context = {
        'is_logged_in': is_logged_in,
        'volunteer': volunteer,
    }
    return HttpResponse(template.render(context, request))


def account(request):
    return render(request, "loginSignup.html")
 
def createpost(request):
    template = loader.get_template('listcategories.html')
    is_logged_in = request.session.get('is_logged_in', False)
    context = {
        'is_logged_in': is_logged_in,
        }
    if not is_logged_in:
        return render (request, 'loginSignup.html')
    else:
        return HttpResponse(template.render(context,request)) 
    
    
def createpostcarsTrucks(request):
    return render(request, 'createpostcarsTrucks.html')

def createpostactivity(request):
    return render(request, 'createpostactivity.html')

def createpostapts(request):
    return render(request, 'createpostapts.html')

def createpostboats(request):
    return render(request, 'createpostboats.html')

def createpostbooks(request):
    return render(request, 'createpostbooks.html')

def createpostcardetail(request):
    return render(request, 'createpostcardetail.html')

def createpostfurniture(request):
    return render(request, 'createpostfurniture.html')

def createpostcatering(request):
    return render(request, 'createpostcatering.html')

def createpostchild(request):
    return render(request, 'createpostchild.html')

def createpostcleaning(request):
    return render(request, 'createpostcleaning.html')

def createpostcontract(request):
    return render(request, 'createpostcontract.html')

def createpostfull(request):
    return render(request, 'createpostfull.html')

def createpostlawn(request):
    return render(request, 'createpostlawn.html')

def createpostlost(request):
    return render(request, 'createpostlost.html')

def createpostmanu(request):
    return render(request, 'createpostmanu.html')

def createpostmotorcycles(request):
    return render(request, 'createpostmotorcycles.html')

def createpostodd(request):
    return render(request, 'createpostodd.html')

def createpostparking(request):
    return render(request, 'createpostparking.html')

def createpostpart(request):
    return render(request, 'createpostpart.html')

def createpostpets(request):
    return render(request, 'createpostpets.html')

def createpostrealEstate(request):
    return render(request, 'createpostrealEstate.html')

def createpostride(request):
    return render(request, 'createpostride.html')

def createpostswap(request):
    return render(request, 'createpostswap.html')

def createpostvacay(request):
    return render(request, 'createpostvacay.html')

def createpostvolunteer(request):
    return render(request, 'createpostvolunteer.html')


def carssubmit(request):
    if request.method == 'POST':
        form = CreatePostFormCars(request.POST)
        if form.is_valid():
            year_built = form.cleaned_data['year_built']
            make_model = form.cleaned_data['make_model']
            color = form.cleaned_data['color']
            type = form.cleaned_data['type']
            condition = form.cleaned_data['condition']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailscars(year_built, make_model, color, type, condition, price, description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('carsTrucks')  
    else:
        form = CreatePostFormCars()
    return render(request, 'createpostcarsTrucks.html', {'form': form})

def motorcyclesubmit(request):
    if request.method == 'POST':
        form = CreatePostFormMotorcycles(request.POST)
        if form.is_valid():
            year_built = form.cleaned_data['year_built']
            make_model = form.cleaned_data['make_model']
            color = form.cleaned_data['color']
            type = form.cleaned_data['type']
            condition = form.cleaned_data['condition']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailsmotorcycle(year_built, make_model, color, type, condition, price, description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('motorcycles')  
    else:
        form = CreatePostFormMotorcycles()
    return render(request, 'createpostmotorcycles.html', {'form': form})

def boatsubmit(request):
    if request.method == 'POST':
        form = CreatePostFormBoats(request.POST)
        if form.is_valid():
            year_built = form.cleaned_data['year_built']
            make_model = form.cleaned_data['make_model']
            color = form.cleaned_data['color']
            type = form.cleaned_data['type']
            condition = form.cleaned_data['condition']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']

            if insert_detailsboats(year_built, make_model, color, type, condition, price, description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('boats')
    else:
        form = CreatePostFormBoats()
    return render(request, 'createpostboats.html', {'form': form})

def booksubmit(request):
    if request.method == 'POST':
        form = CreatePostFormBooks(request.POST)
        if form.is_valid():
            year_published = form.cleaned_data['year_published']
            author = form.cleaned_data['author']
            title = form.cleaned_data['title']
            genre = form.cleaned_data['genre']
            condition = form.cleaned_data['condition']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']

            if insert_detailsbooks(year_published, author, title, genre, condition, price, description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('books')

    else:
        form = CreatePostFormBooks()

    return render(request, 'createpostbooks.html', {'form': form})

def furnituresubmit(request):
    if request.method == 'POST':
        form = CreatePostFormFurniture(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['item_name']
            brand = form.cleaned_data['brand']
            material = form.cleaned_data['material']
            furniture_condition = form.cleaned_data['furniture_condition']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']

            if insert_detailsfurniture(item_name, brand, material, furniture_condition, price, description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('furniture')

    else:
        form = CreatePostFormFurniture()
    return render(request, 'createpostfurniture.html', {'form': form})

def realEstatesubmit(request):
    if request.method == 'POST':
        form = CreatePostFormRealEstate(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            bedrooms = form.cleaned_data['bedrooms']
            bathrooms = form.cleaned_data['bathrooms']
            features = form.cleaned_data['features']
            price = form.cleaned_data['price']
            estate_description = form.cleaned_data['estate_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailsrealestate(address, bedrooms, bathrooms, features, price, estate_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('realEstate')  
    else:
        form = CreatePostFormRealEstate()
    return render(request, 'createpostrealEstate.html', {'form': form})

def swapsubmit(request):
    if request.method == 'POST':
        form = CreatePostFormSwap(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            bedrooms = form.cleaned_data['bedrooms']
            bathrooms = form.cleaned_data['bathrooms']
            features = form.cleaned_data['features']
            swap_reason= form.cleaned_data['swap_reason']
            estate_description = form.cleaned_data['estate_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailsswap(address, bedrooms, bathrooms, features, swap_reason, estate_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('swap')  
    else:
        form = CreatePostFormSwap()
    return render(request, 'createpostswap.html', {'form': form})

def aptssubmit(request):
    if request.method == 'POST':
        form = CreatePostFormApts(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            bedrooms = form.cleaned_data['bedrooms']
            bathrooms = form.cleaned_data['bathrooms']
            features = form.cleaned_data['features']
            rent = form.cleaned_data['rent']
            apt_description = form.cleaned_data['apt_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailsapts(address, bedrooms, bathrooms, features, rent, apt_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('apts')  
    else:
        form = CreatePostFormApts()
    return render(request, 'createpostapts.html', {'form': form})

def parkingsubmit(request):
    if request.method == 'POST':
        form = CreatePostFormParking(request.POST)
        if form.is_valid():
            parking_name = form.cleaned_data['parking_name']
            address = form.cleaned_data['address']
            parking_type = form.cleaned_data['parking_type']
            size = form.cleaned_data['size']
            price = form.cleaned_data['price']
            parking_description = form.cleaned_data['parking_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailsparking(parking_name, address, parking_type, size, price, parking_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('parking')  
    else:
        form = CreatePostFormParking()
    return render(request, 'createpostparking.html', {'form': form})

def vacaysubmit(request):
    if request.method == 'POST':
        form = CreatePostFormVacay(request.POST)
        if form.is_valid():
            vacay_name = form.cleaned_data['vacay_name']
            address = form.cleaned_data['address']
            vacay_type = form.cleaned_data['vacay_type']
            amenities = form.cleaned_data['amenities']
            price = form.cleaned_data['price']
            vacay_description = form.cleaned_data['vacay_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailsvacay(vacay_name, address, vacay_type, amenities, price, vacay_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('vacay')  
    else:
        form = CreatePostFormVacay()
    return render(request, 'createpostvacay.html', {'form': form})

def cleaningsubmit(request):
    if request.method == 'POST':
        form = CreatePostFormCleaning(request.POST)
        if form.is_valid():
            cleaning_name = form.cleaned_data['cleaning_name']
            address = form.cleaned_data['address']
            cleaning_type = form.cleaned_data['cleaning_type']
            cleaning_hours = form.cleaned_data['cleaning_hours']
            price = form.cleaned_data['price']
            cleaning_description = form.cleaned_data['cleaning_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailscleaning(cleaning_name, address, cleaning_type, cleaning_hours, price, cleaning_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('cleaning')  
    else:
        form = CreatePostFormCleaning()
    return render(request, 'createpostcleaning.html', {'form': form})

def lawnsubmit(request):
    if request.method == 'POST':
        form = CreatePostFormLawn(request.POST)
        if form.is_valid():
            lawn_name = form.cleaned_data['lawn_name']
            address = form.cleaned_data['address']
            lawn_type = form.cleaned_data['lawn_type']
            lawn_hours = form.cleaned_data['lawn_hours']
            price = form.cleaned_data['price']
            lawn_description = form.cleaned_data['lawn_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailslawn(lawn_name, address, lawn_type, lawn_hours, price, lawn_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('lawn')  
    else:
        form = CreatePostFormLawn()
    return render(request, 'createpostlawn.html', {'form': form})

def cardetailsubmit(request):
    if request.method == 'POST':
        form = CreatePostFormCarDetail(request.POST)
        if form.is_valid():
            cardetail_name = form.cleaned_data['cardetail_name']
            address = form.cleaned_data['address']
            cardetail_type = form.cleaned_data['cardetail_type']
            cardetail_hours = form.cleaned_data['cardetail_hours']
            price = form.cleaned_data['price']
            cardetail_description = form.cleaned_data['cardetail_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailscardetail(cardetail_name, address, cardetail_type, cardetail_hours, price, cardetail_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('cardetail')  
    else:
        form = CreatePostFormCarDetail()
    return render(request, 'createpostcardetail.html', {'form': form})

def petssubmit(request):
    if request.method == 'POST':
        form = CreatePostFormPets(request.POST)
        if form.is_valid():
            pets_name = form.cleaned_data['pets_name']
            address = form.cleaned_data['address']
            pets_type = form.cleaned_data['pets_type']
            pets_hours = form.cleaned_data['pets_hours']
            price = form.cleaned_data['price']
            pets_description = form.cleaned_data['pets_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailspets(pets_name, address, pets_type, pets_hours, price, pets_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('pets')  
    else:
        form = CreatePostFormPets()
    return render(request, 'createpostpets.html', {'form': form})

def cateringsubmit(request):
    if request.method == 'POST':
        form = CreatePostFormCatering(request.POST)
        if form.is_valid():
            catering_name = form.cleaned_data['catering_name']
            address = form.cleaned_data['address']
            catering_type = form.cleaned_data['catering_type']
            catering_hours = form.cleaned_data['catering_hours']
            price = form.cleaned_data['price']
            catering_description = form.cleaned_data['catering_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailscatering(catering_name, address, catering_type, catering_hours, price, catering_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('catering')  
    else:
        form = CreatePostFormCatering()
    return render(request, 'createpostcatering.html', {'form': form})

def contractsubmit(request):
    if request.method == 'POST':
        form = CreatePostFormContract(request.POST)
        if form.is_valid():
            contract_name = form.cleaned_data['contract_name']
            address = form.cleaned_data['address']
            contract_type = form.cleaned_data['contract_type']
            contract_hours = form.cleaned_data['contract_hours']
            wage = form.cleaned_data['wage']
            contract_description = form.cleaned_data['contract_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailscontract(contract_name, address, contract_type, contract_hours, wage, contract_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('contract')  
    else:
        form = CreatePostFormContract()
    return render(request, 'createpostcontract.html', {'form': form})

def oddsubmit(request):
    if request.method == 'POST':
        form = CreatePostFormOdd(request.POST)
        if form.is_valid():
            odd_name = form.cleaned_data['odd_name']
            address = form.cleaned_data['address']
            odd_type = form.cleaned_data['odd_type']
            odd_duration = form.cleaned_data['odd_duration']
            pay = form.cleaned_data['pay']
            odd_description = form.cleaned_data['odd_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailsodd(odd_name, address, odd_type, odd_duration, pay, odd_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('odd')  
    else:
        form = CreatePostFormOdd()
    return render(request, 'createpostodd.html', {'form': form})

def fullsubmit(request):
    if request.method == 'POST':
        form = CreatePostFormFull(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            address = form.cleaned_data['address']
            full_type = form.cleaned_data['full_type']
            full_hours = form.cleaned_data['full_hours']
            pay = form.cleaned_data['pay']
            full_description = form.cleaned_data['full_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailsfull(full_name, address, full_type, full_hours, pay, full_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('full')  
    else:
        form = CreatePostFormFull()
    return render(request, 'createpostfull.html', {'form': form})

def partsubmit(request):
    if request.method == 'POST':
        form = CreatePostFormPart(request.POST)
        if form.is_valid():
            part_name = form.cleaned_data['part_name']
            address = form.cleaned_data['address']
            part_type = form.cleaned_data['part_type']
            part_hours = form.cleaned_data['part_hours']
            pay = form.cleaned_data['pay']
            part_description = form.cleaned_data['part_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailspart(part_name, address, part_type, part_hours, pay, part_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('part')  
    else:
        form = CreatePostFormPart()
    return render(request, 'createpostpart.html', {'form': form})

def manusubmit(request):
    if request.method == 'POST':
        form = CreatePostFormManu(request.POST)
        if form.is_valid():
            manu_name = form.cleaned_data['manu_name']
            address = form.cleaned_data['address']
            manu_type = form.cleaned_data['manu_type']
            manu_hours = form.cleaned_data['manu_hours']
            pay = form.cleaned_data['pay']
            manu_description = form.cleaned_data['manu_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailsmanu(manu_name, address, manu_type, manu_hours, pay, manu_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('manu')  
    else:
        form = CreatePostFormManu()
    return render(request, 'createpostmanu.html', {'form': form})

def activitysubmit(request):
    if request.method == 'POST':
        form = CreatePostFormActivity(request.POST)
        if form.is_valid():
            activity_name = form.cleaned_data['activity_name']
            address = form.cleaned_data['address']
            activity_type = form.cleaned_data['activity_type']
            needed_items = form.cleaned_data['needed_items']
            price = form.cleaned_data['price']
            activity_description = form.cleaned_data['activity_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailsactivity(activity_name, address, activity_type, needed_items, price, activity_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('activity')  
    else:
        form = CreatePostFormActivity()
    return render(request, 'createpostactivity.html', {'form': form})

def lostsubmit(request):
    if request.method == 'POST':
        form = CreatePostFormLost(request.POST)
        if form.is_valid():
            lost_name = form.cleaned_data['lost_name']
            address = form.cleaned_data['address']
            lost_type = form.cleaned_data['lost_type']
            lost_found = form.cleaned_data['lost_found']
            contact_info = form.cleaned_data['contact_info']
            lost_description = form.cleaned_data['lost_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailslost(lost_name, address, lost_type, lost_found, contact_info, lost_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('lost')  
    else:
        form = CreatePostFormLost()
    return render(request, 'createpostlost.html', {'form': form})


def childsubmit(request):
    if request.method == 'POST':
        form = CreatePostFormChild(request.POST)
        if form.is_valid():
            child_name = form.cleaned_data['child_name']
            address = form.cleaned_data['address']
            child_type = form.cleaned_data['child_type']
            child_hours = form.cleaned_data['child_hours']
            price = form.cleaned_data['price']
            child_description = form.cleaned_data['child_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailschild(child_name, address, child_type, child_hours, price, child_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('child')  
    else:
        form = CreatePostFormChild()
    return render(request, 'createpostchild.html', {'form': form})

def ridesubmit(request):
    if request.method == 'POST':
        form = CreatePostFormRide(request.POST)
        if form.is_valid():
            ride_name = form.cleaned_data['ride_name']
            address = form.cleaned_data['address']
            ride_type = form.cleaned_data['ride_type']
            ride_hours = form.cleaned_data['ride_hours']
            price = form.cleaned_data['price']
            ride_description = form.cleaned_data['ride_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailsride(ride_name, address, ride_type, ride_hours, price, ride_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('ride')  
    else:
        form = CreatePostFormRide()
    return render(request, 'createpostride.html', {'form': form})


def volunteersubmit(request):
    if request.method == 'POST':
        form = CreatePostFormVolunteer(request.POST)
        if form.is_valid():
            volunteer_name = form.cleaned_data['volunteer_name']
            address = form.cleaned_data['address']
            volunteer_type = form.cleaned_data['volunteer_type']
            volunteer_hours = form.cleaned_data['volunteer_hours']
            contact_info = form.cleaned_data['contact_info']
            volunteer_description = form.cleaned_data['volunteer_description']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            
            if insert_detailsvolunteer(volunteer_name, address, volunteer_type, volunteer_hours, contact_info, volunteer_description, city, phone_number):
                messages.success(request, 'Successfully added post')
                return redirect('volunteer')  
    else:
        form = CreatePostFormVolunteer()
    return render(request, 'createpostvolunteer.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
             messages.error(request, 'Username already exists. Please choose a different one.')
             return render(request, 'loginSignup.html')
        else:
             myuser = User.objects.create_user(username=username, password=password)
             myuser.save()
        if(insert_details(username,password)):  
            messages.success(request, 'Your account has been created successfully!')
            request.session['is_logged_in'] = True
            return redirect('home')
        else:
            messages.error(request, 'An error occurred while creating your account. Please try again.')
            return render(request, 'loginSignup.html')
    else:
        return render(request, 'loginSignup.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        if not User.objects.filter(username=username).exists():
             messages.error(request, 'Username does not exist. Please register')
             return render(request, 'loginSignup.html')
        else:
            request.session['is_logged_in'] = True
            return redirect('home')
    else:
        return render(request, 'loginSignup.html')

def insert_details(username, password):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
    return True

def insert_detailscars(year_built, make_model, color, vehicle_type, vehicle_condition, price, vehicle_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO carsTrucks (year_built, make_model, color, vehicle_type, vehicle_condition, price, vehicle_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (year_built, make_model, color, vehicle_type, vehicle_condition, price, vehicle_description, city, phone_number))
        conn.commit()
    return True

def insert_detailsmotorcycle(year_built, make_model, color, vehicle_type, vehicle_condition, price, vehicle_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO motorcycles (year_built, make_model, color, vehicle_type, vehicle_condition, price, vehicle_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (year_built, make_model, color, vehicle_type, vehicle_condition, price, vehicle_description, city, phone_number))
        conn.commit()
    return True

def insert_detailsboats(year_built, make_model, color, vehicle_type, vehicle_condition, price, vehicle_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO boats (year_built, make_model, color, vehicle_type, vehicle_condition, price, vehicle_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (year_built, make_model, color, vehicle_type, vehicle_condition, price, vehicle_description, city, phone_number))
        conn.commit()
    return True

def insert_detailsbooks(year_published, author, title, genre, book_condition, price, book_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO books (year_published, author, title, genre, book_condition, price, book_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (year_published, author, title, genre, book_condition, price, book_description, city, phone_number))
        conn.commit()
    return True

def insert_detailsfurniture(item_name, brand, material, furniture_condition, price, description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO furniture (item_name, brand, material, furniture_condition, price, description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (item_name, brand, material, furniture_condition, price, description, city, phone_number))
        conn.commit()
    return True

def insert_detailsrealestate(address, bedrooms, bathrooms, features, price, estate_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO realEstate (address, bedrooms, bathrooms, features, price, estate_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (address, bedrooms, bathrooms, features, price, estate_description, city, phone_number))
        conn.commit()
    return True

def insert_detailsswap(address, bedrooms, bathrooms, features, swap_reason, estate_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO swap (address, bedrooms, bathrooms, features, swap_reason, estate_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (address, bedrooms, bathrooms, features, swap_reason, estate_description, city, phone_number))
        conn.commit()
    return True

def insert_detailsapts(address, bedrooms, bathrooms, features, rent, apt_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO apt (address, bedrooms, bathrooms, features, rent, apt_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (address, bedrooms, bathrooms, features, rent, apt_description, city, phone_number))
        conn.commit()
    return True

def insert_detailsparking(parking_name, address, parking_type, size, price, parking_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO parking (parking_name, address, parking_type, size, price, parking_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (parking_name, address, parking_type, size, price, parking_description, city, phone_number))
        conn.commit()
    return True

def insert_detailsvacay(vacay_name, address, vacay_type, amenities, price, vacay_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO vacay (vacay_name, address, vacay_type, amenities, price, vacay_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (vacay_name, address, vacay_type, amenities, price, vacay_description, city, phone_number))
        conn.commit()
    return True

def insert_detailscleaning(cleaning_name, address, cleaning_type, cleaning_hours, price, cleaning_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO cleaning (cleaning_name, address, cleaning_type, cleaning_hours, price, cleaning_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (cleaning_name, address, cleaning_type, cleaning_hours, price, cleaning_description, city, phone_number))
        conn.commit()
    return True

def insert_detailslawn(lawn_name, address, lawn_type, lawn_hours, price, lawn_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO lawn (lawn_name, address, lawn_type, lawn_hours, price, lawn_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (lawn_name, address, lawn_type, lawn_hours, price, lawn_description, city, phone_number))
        conn.commit()
    return True

def insert_detailscardetail(cardetail_name, address, cardetail_type, cardetail_hours, price, cardetail_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO cardetail (cardetail_name, address, cardetail_type, cardetail_hours, price, cardetail_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (cardetail_name, address, cardetail_type, cardetail_hours, price, cardetail_description, city, phone_number))
        conn.commit()
    return True

def insert_detailspets(pets_name, address, pets_type, pets_hours, price, pets_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO pets (pets_name, address, pets_type, pets_hours, price, pets_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (pets_name, address, pets_type, pets_hours, price, pets_description, city, phone_number))
        conn.commit()
    return True

def insert_detailscatering(catering_name, address, catering_type, catering_hours, price, catering_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO catering (catering_name, address, catering_type, catering_hours, price, catering_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (catering_name, address, catering_type, catering_hours, price, catering_description, city, phone_number))
        conn.commit()
    return True

def insert_detailscontract(contract_name, address, contract_type, contract_hours, wage, contract_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO contract (contract_name, address, contract_type, contract_hours, wage, contract_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (contract_name, address, contract_type, contract_hours, wage, contract_description, city, phone_number))
        conn.commit()
    return True

def insert_detailsodd(odd_name, address, odd_type, odd_duration, pay, odd_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO odd (odd_name, address, odd_type, odd_duration, pay, odd_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (odd_name, address, odd_type, odd_duration, pay, odd_description, city, phone_number))
        conn.commit()
    return True

def insert_detailsfull(full_name, address, full_type, full_hours, pay, full_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO full_time (full_name, address, full_type, full_hours, pay, full_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (full_name, address, full_type, full_hours, pay, full_description, city, phone_number))
        conn.commit()
    return True

def insert_detailspart(part_name, address, part_type, part_hours, pay, part_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO part_time (part_name, address, part_type, part_hours, pay, part_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (part_name, address, part_type, part_hours, pay, part_description, city, phone_number))
        conn.commit()
    return True

def insert_detailsmanu(manu_name, address, manu_type, manu_hours, pay, manu_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO manu (manu_name, address, manu_type, manu_hours, pay, manu_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (manu_name, address, manu_type, manu_hours, pay, manu_description, city, phone_number))
        conn.commit()
    return True

def insert_detailsactivity(activity_name, address, activity_type, needed_items, price, activity_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO activity (activity_name, address, activity_type, needed_items, price, activity_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (activity_name, address, activity_type, needed_items, price, activity_description, city, phone_number))
        conn.commit()
    return True

def insert_detailslost(lost_name, address, lost_type, lost_found, contact_info, lost_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO lost (lost_name, address, lost_type, lost_found, contact_info, lost_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (lost_name, address, lost_type, lost_found, contact_info, lost_description, city, phone_number))
        conn.commit()
    return True

def insert_detailschild(child_name, address, child_type, child_hours, price, child_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO child (child_name, address, child_type, child_hours, price, child_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (child_name, address, child_type, child_hours, price, child_description, city, phone_number))
        conn.commit()
    return True


def insert_detailsride(ride_name, address, ride_type, ride_hours, price, ride_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO ride (ride_name, address, ride_type, ride_hours, price, ride_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (ride_name, address, ride_type, ride_hours, price, ride_description, city, phone_number))
        conn.commit()
    return True

def insert_detailsvolunteer(volunteer_name, address, volunteer_type, volunteer_hours, contact_info, volunteer_description, city, phone_number):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO volunteer (volunteer_name, address, volunteer_type, volunteer_hours, contact_info, volunteer_description, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (volunteer_name, address, volunteer_type, volunteer_hours, contact_info, volunteer_description, city, phone_number))
        conn.commit()
    return True

def getCarsTrucks():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM carsTrucks")
        results = namedtuplefetchall(cur)
    return results

def getmotorcycles():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM motorcycles")
        results = namedtuplefetchall(cur)
    return results

def getboats():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM boats")
        results = namedtuplefetchall(cur)
    return results

def getbooks():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM books")
        results = namedtuplefetchall(cur)
    return results

def getfurniture():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM furniture")
        results = namedtuplefetchall(cur)
    return results

def getestate():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM realEstate")
        results = namedtuplefetchall(cur)
    return results

def getswap():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM swap")
        results = namedtuplefetchall(cur)
    return results

def getapts():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM apt")
        results = namedtuplefetchall(cur)
    return results

def getparking():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM parking")
        results = namedtuplefetchall(cur)
    return results

def getvacay():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM vacay")
        results = namedtuplefetchall(cur)
    return results

def getcleaning():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM cleaning")
        results = namedtuplefetchall(cur)
    return results

def getlawn():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM lawn")
        results = namedtuplefetchall(cur)
    return results

def getcardetail():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM cardetail")
        results = namedtuplefetchall(cur)
    return results

def getpets():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM pets")
        results = namedtuplefetchall(cur)
    return results

def getcatering():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM catering")
        results = namedtuplefetchall(cur)
    return results


def getcontract():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM contract")
        results = namedtuplefetchall(cur)
    return results

def getodd():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM odd")
        results = namedtuplefetchall(cur)
    return results

def getfull():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM full_time")
        results = namedtuplefetchall(cur)
    return results

def getpart():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM part_time")
        results = namedtuplefetchall(cur)
    return results

def getmanu():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM manu")
        results = namedtuplefetchall(cur)
    return results

def getactivity():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM activity")
        results = namedtuplefetchall(cur)
    return results

def getlost():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM lost")
        results = namedtuplefetchall(cur)
    return results


def getchild():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM child")
        results = namedtuplefetchall(cur)
    return results

def getride():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM ride")
        results = namedtuplefetchall(cur)
    return results

def getvolunteer():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM volunteer")
        results = namedtuplefetchall(cur)
    return results

def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def logout(request):
    if request.session.get('is_logged_in', True):
        request.session['is_logged_in'] = False
        return redirect('home')
    
def car_listing_detail(request, car_id):
    template = loader.get_template('car_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    cars = getCarsTrucks()
    context = {
        'is_logged_in': is_logged_in,
        'cars': cars,
        'carID' : car_id
    }
    return HttpResponse(template.render(context, request))

def motorcycle_listing_detail(request, motorcycle_id):
    template = loader.get_template('motorcycle_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    motorcycles = getmotorcycles()
    context = {
        'is_logged_in': is_logged_in,
        'motorcycles': motorcycles,
        'motorcycleID' : motorcycle_id
    }
    return HttpResponse(template.render(context, request))

def boat_listing_detail(request, boat_id):
    template = loader.get_template('boat_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    boats = getboats()  
    context = {
        'is_logged_in': is_logged_in,
        'boats': boats,
        'boatID': boat_id,
    }
    return HttpResponse(template.render(context, request))

def book_listing_detail(request, book_id):
    template = loader.get_template('book_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    books = getbooks()
    context = {
        'is_logged_in': is_logged_in,
        'books': books,
        'bookID': book_id
    }
    return HttpResponse(template.render(context, request))

def furniture_listing_detail(request, furniture_id):
    template = loader.get_template('furniture_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    furniture = getfurniture()
    context = {
        'is_logged_in': is_logged_in,
        'furnitures': furniture,
        'furnitureID': furniture_id
    }
    return HttpResponse(template.render(context, request))

def estate_listing_detail(request, estate_id):
    template = loader.get_template('estate_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    estate = getestate()
    context = {
        'is_logged_in': is_logged_in,
        'estates': estate,
        'estateID': estate_id
    }
    return HttpResponse(template.render(context, request))

def swap_listing_detail(request, swap_id):
    template = loader.get_template('swap_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    swap = getswap()
    context = {
        'is_logged_in': is_logged_in,
        'swaps': swap,
        'swapID': swap_id
    }
    return HttpResponse(template.render(context, request))


def apt_listing_detail(request, apt_id):
    template = loader.get_template('apt_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    apt = getapts()
    context = {
        'is_logged_in': is_logged_in,
        'apts': apt,
        'aptID': apt_id
    }
    return HttpResponse(template.render(context, request))


def parking_listing_detail(request, parking_id):
    template = loader.get_template('parking_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    parking = getparking()
    context = {
        'is_logged_in': is_logged_in,
        'parkings': parking,
        'parkingID': parking_id
    }
    return HttpResponse(template.render(context, request))


def vacay_listing_detail(request, vacay_id):
    template = loader.get_template('vacay_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    vacay = getvacay()
    context = {
        'is_logged_in': is_logged_in,
        'vacays': vacay,
        'vacayID': vacay_id
    }
    return HttpResponse(template.render(context, request))


def cleaning_listing_detail(request, cleaning_id):
    template = loader.get_template('cleaning_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    cleaning = getcleaning()
    context = {
        'is_logged_in': is_logged_in,
        'cleanings': cleaning,
        'cleaningID': cleaning_id
    }
    return HttpResponse(template.render(context, request))


def lawn_listing_detail(request, lawn_id):
    template = loader.get_template('lawn_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    lawn = getlawn()
    context = {
        'is_logged_in': is_logged_in,
        'lawns': lawn,
        'lawnID': lawn_id
    }
    return HttpResponse(template.render(context, request))

def cardetail_listing_detail(request, cardetail_id):
    template = loader.get_template('cardetail_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    cardetail = getcardetail()
    context = {
        'is_logged_in': is_logged_in,
        'cardetails': cardetail,
        'cardetailID': cardetail_id
    }
    return HttpResponse(template.render(context, request))

def pet_listing_detail(request, pet_id):
    template = loader.get_template('pet_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    pet = getpets()
    context = {
        'is_logged_in': is_logged_in,
        'pets': pet,
        'petID': pet_id
    }
    return HttpResponse(template.render(context, request))

def catering_listing_detail(request, catering_id):
    template = loader.get_template('catering_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    catering = getcatering()
    context = {
        'is_logged_in': is_logged_in,
        'caterings': catering,
        'cateringID': catering_id
    }
    return HttpResponse(template.render(context, request))

def contract_listing_detail(request, contract_id):
    template = loader.get_template('contract_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    contract = getcontract()
    context = {
        'is_logged_in': is_logged_in,
        'contracts': contract,
        'contractID': contract_id
    }
    return HttpResponse(template.render(context, request))

def odd_listing_detail(request, odd_id):
    template = loader.get_template('odd_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    odd = getodd()
    context = {
        'is_logged_in': is_logged_in,
        'odds': odd,
        'oddID': odd_id
    }
    return HttpResponse(template.render(context, request))

def full_listing_detail(request, full_id):
    template = loader.get_template('full_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    full = getfull()
    context = {
        'is_logged_in': is_logged_in,
        'fulls': full,
        'fullID': full_id
    }
    return HttpResponse(template.render(context, request))

def part_listing_detail(request, part_id):
    template = loader.get_template('part_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    part = getpart()
    context = {
        'is_logged_in': is_logged_in,
        'parts': part,
        'partID': part_id
    }
    return HttpResponse(template.render(context, request))

def manu_listing_detail(request, manu_id):
    template = loader.get_template('manu_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    manu = getmanu()
    context = {
        'is_logged_in': is_logged_in,
        'manus': manu,
        'manuID': manu_id
    }
    return HttpResponse(template.render(context, request))

def activity_listing_detail(request, activity_id):
    template = loader.get_template('activity_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    activity = getactivity()
    context = {
        'is_logged_in': is_logged_in,
        'activitys': activity,
        'activityID': activity_id
    }
    return HttpResponse(template.render(context, request))

def lost_listing_detail(request, lost_id):
    template = loader.get_template('lost_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    lost = getlost()
    context = {
        'is_logged_in': is_logged_in,
        'lost': lost,
        'lostID': lost_id
    }
    return HttpResponse(template.render(context, request))

def child_listing_detail(request, child_id):
    template = loader.get_template('child_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    child = getchild()
    context = {
        'is_logged_in': is_logged_in,
        'children': child,
        'childID': child_id
    }
    return HttpResponse(template.render(context, request))

def ride_listing_detail(request, ride_id):
    template = loader.get_template('ride_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    ride = getride()
    context = {
        'is_logged_in': is_logged_in,
        'rides': ride,
        'rideID': ride_id
    }
    return HttpResponse(template.render(context, request))


def volunteer_listing_detail(request, volunteer_id):
    template = loader.get_template('volunteer_listing_detail.html')
    is_logged_in = request.session.get('is_logged_in', False)
    volunteer = getvolunteer()
    context = {
        'is_logged_in': is_logged_in,
        'volunteers': volunteer,
        'volunteerID': volunteer_id
    }
    return HttpResponse(template.render(context, request))

def salecategory(request):
    template = loader.get_template('salecategory.html')
    is_logged_in = request.session.get('is_logged_in', False)
    context = {
        'is_logged_in': is_logged_in,
    }
    return HttpResponse(template.render(context, request))

def housingcategory(request):
    template = loader.get_template('housingcategory.html')
    is_logged_in = request.session.get('is_logged_in', False)
    context = {
        'is_logged_in': is_logged_in,
    }
    return HttpResponse(template.render(context, request))

def servicescategory(request):
    template = loader.get_template('servicescategory.html')
    is_logged_in = request.session.get('is_logged_in', False)
    context = {
        'is_logged_in': is_logged_in,
    }
    return HttpResponse(template.render(context, request))

def jobscategory(request):
    template = loader.get_template('jobscategory.html')
    is_logged_in = request.session.get('is_logged_in', False)
    context = {
        'is_logged_in': is_logged_in,
    }
    return HttpResponse(template.render(context, request))

def communitycategory(request):
    template = loader.get_template('communitycategory.html')
    is_logged_in = request.session.get('is_logged_in', False)
    context = {
        'is_logged_in': is_logged_in,
    }
    return HttpResponse(template.render(context, request))