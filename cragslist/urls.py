"""
URL configuration for cragslist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'), #might want to include / in pattern but ill handle that later
    path('sale', views.sale, name='sale'),
    path('house', views.house, name='house'),
    path('service', views.service, name='service'),
    path('job', views.job, name='job'),
    path('community', views.community, name='community'),
    path('carsTrucks', views.carsTrucks, name='carsTrucks'),
    path('motorcycles', views.motorcycles, name='motorcycles'),
    path('boats', views.boats, name='boats'),
    path('books', views.books, name='books'),
    path('furniture', views.furniture, name='furniture'),
    path('realEstate', views.realEstate, name='realEstate'),
    path('swap', views.swap, name='swap'),
    path('apts', views.apts, name='apts'),
    path('parking', views.parking, name='parking'),
    path('vacay', views.vacay, name='vacay'),
    path('cleaning', views.cleaning, name='cleaning'),
    path('lawn', views.lawn, name='lawn'),
    path('cardetail', views.cardetail, name='cardetail'),
    path('pets', views.pets, name='pets'),
    path('catering', views.catering, name='catering'),
    path('contract', views.contract, name='contract'),
    path('odd', views.odd, name='odd'),
    path('full', views.full, name='full'),
    path('part', views.part, name='part'),
    path('manu', views.manu, name='manu'),
    path('activity', views.activity, name='activity'),
    path('lost', views.lost, name='lost'),
    path('child', views.child, name='child'),
    path('ride', views.ride, name='ride'),
    path('volunteer', views.volunteer, name='volunteer'),
    path('account', include('django.contrib.auth.urls')),
    path('account', views.account, name='account'),
    path('carssubmit', views.carssubmit, name='carssubmit'),
    path('motorcyclesubmit', views.motorcyclesubmit, name='motorcyclesubmit'),
    path('boatsubmit', views.boatsubmit, name='boatsubmit'),
    path('booksubmit', views.booksubmit, name='booksubmit'),
    path('furnituresubmit', views.furnituresubmit, name='furnituresubmit'),
    path('realEstatesubmit', views.realEstatesubmit, name='realEstatesubmit'),
    path('swapsubmit', views.swapsubmit, name='swapsubmit'),
    path('aptssubmit', views.aptssubmit, name='aptssubmit'),
    path('parkingsubmit', views.parkingsubmit, name='parkingsubmit'),
    path('vacaysubmit', views.vacaysubmit, name='vacaysubmit'),
    path('cleaningsubmit', views.cleaningsubmit, name='cleaningsubmit'),
    path('lawnsubmit', views.lawnsubmit, name='lawnsubmit'),
    path('cardetailsubmit', views.cardetailsubmit, name='cardetailsubmit'),
    path('petssubmit', views.petssubmit, name='petssubmit'),
    path('cateringsubmit', views.cateringsubmit, name='cateringsubmit'),
    path('contractsubmit', views.contractsubmit, name='contractsubmit'),
    path('oddsubmit', views.oddsubmit, name='oddsubmit'),
    path('fullsubmit', views.fullsubmit, name='fullsubmit'),
    path('partsubmit', views.partsubmit, name='partsubmit'),
    path('manusubmit', views.manusubmit, name='manusubmit'),
    path('activitysubmit', views.activitysubmit, name='activitysubmit'),
    path('lostsubmit', views.lostsubmit, name='lostsubmit'),
    path('childsubmit', views.childsubmit, name='childsubmit'),
    path('ridesubmit', views.ridesubmit, name='ridesubmit'),
    path('volunteersubmit', views.volunteersubmit, name='volunteersubmit'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('createpost',views.createpost,name='createpost'),
    path('logout',views.logout, name='logout'),
    path('createpostcarsTrucks', views.createpostcarsTrucks, name='createpostcarsTrucks'),
    path('car_listing_detail/<int:car_id>/', views.car_listing_detail, name='car_listing_detail'),
    path('createpostmotorcycles', views.createpostmotorcycles, name='createpostmotorcycles'),
    path('motorcycle_listing_detail/<int:motorcycle_id>/', views.motorcycle_listing_detail, name='motorcycle_listing_detail'),
    path('createpostboats', views.createpostboats, name='createpostboats'),
    path('boat_listing_detail/<int:boat_id>/', views.boat_listing_detail, name='boat_listing_detail'),
    path('createpostbooks', views.createpostbooks, name='createpostbooks'),
    path('book_listing_detail/<int:book_id>/', views.book_listing_detail, name='book_listing_detail'),
    path('createpostfurniture', views.createpostfurniture, name='createpostfurniture'),
    path('furniture_listing_detail/<int:furniture_id>/', views.furniture_listing_detail, name='furniture_listing_detail'),
    path('createpostrealEstate', views.createpostrealEstate, name='createpostrealEstate'),
    path('estate_listing_detail/<int:estate_id>/', views.estate_listing_detail, name='estate_listing_detail'),
    path('createpostswap', views.createpostswap, name='createpostswap'),
    path('createpostapts', views.createpostapts, name='createpostapts'),
    path('createpostparking', views.createpostparking, name='createpostparking'),
    path('createpostvacay', views.createpostvacay, name='createpostvacay'),
    path('createpostcleaning', views.createpostcleaning, name='createpostcleaning'),
    path('createpostlawncare', views.createpostlawn, name='createpostlawncare'),
    path('createpostcardetail', views.createpostcardetail, name='createpostcardetail'),
    path('createpostpets', views.createpostpets, name='createpostpets'),
    path('createpostcatering', views.createpostcatering, name='createpostcatering'),
    path('createpostcontract', views.createpostcontract, name='createpostcontract'),
    path('createpostodd', views.createpostodd, name='createpostodd'),
    path('createpostfull', views.createpostfull, name='createpostfull'),
    path('createpostpart', views.createpostpart, name='createpostpart'),
    path('createpostmanu', views.createpostmanu, name='createpostmanu'),
    path('createpostactivity', views.createpostactivity, name='createpostactivity'),
    path('createpostlost', views.createpostlost, name='createpostlost'),
    path('createpostchild', views.createpostchild, name='createpostchild'),
    path('createpostride', views.createpostride, name='createpostride'),
    path('createpostvolunteer', views.createpostvolunteer, name='createpostvolunteer'),
    path('swap_listing_detail/<int:swap_id>/', views.swap_listing_detail, name='swap_listing_detail'),
    path('apt_listing_detail/<int:apt_id>/', views.apt_listing_detail, name='apt_listing_detail'),
    path('parking_listing_detail/<int:parking_id>/', views.parking_listing_detail, name='parking_listing_detail'),
    path('vacay_listing_detail/<int:vacay_id>/', views.vacay_listing_detail, name='vacay_listing_detail'),
    path('cleaning_listing_detail/<int:cleaning_id>/', views.cleaning_listing_detail, name='cleaning_listing_detail'),
    path('lawn_listing_detail/<int:lawn_id>/', views.lawn_listing_detail, name='lawn_listing_detail'),
    path('cardetail_listing_detail/<int:cardetail_id>/', views.cardetail_listing_detail, name='cardetail_listing_detail'),
    path('pets_listing_detail/<int:pet_id>/', views.pet_listing_detail, name='pets_listing_detail'),
    path('catering_listing_detail/<int:catering_id>/', views.catering_listing_detail, name='catering_listing_detail'),
    path('contract_listing_detail/<int:contract_id>/', views.contract_listing_detail, name='contract_listing_detail'),
    path('odd_listing_detail/<int:odd_id>/', views.odd_listing_detail, name='odd_listing_detail'),
    path('full_listing_detail/<int:full_id>/', views.full_listing_detail, name='full_listing_detail'),
    path('part_listing_detail/<int:part_id>/', views.part_listing_detail, name='part_listing_detail'),
    path('manu_listing_detail/<int:manu_id>/', views.manu_listing_detail, name='manu_listing_detail'),
    path('activity_listing_detail/<int:activity_id>/', views.activity_listing_detail, name='activity_listing_detail'),
    path('lost_listing_detail/<int:lost_id>/', views.lost_listing_detail, name='lost_listing_detail'),
    path('child_listing_detail/<int:child_id>/', views.child_listing_detail, name='child_listing_detail'),
    path('ride_listing_detail/<int:ride_id>/', views.ride_listing_detail, name='ride_listing_detail'),
    path('volunteer_listing_detail/<int:volunteer_id>/', views.volunteer_listing_detail, name='volunteer_listing_detail'),
    path('salecategory' , views.salecategory, name='salecategory'),
    path('housingcategory' , views.housingcategory, name='housingcategory'),
    path('servicescategory', views.servicescategory, name='servicescategory'),
    path('jobscategory', views.jobscategory, name='jobscategory'),
    path('communitycategory', views.communitycategory, name='communitycategory'),
]
