from django import forms
from django.db import models
from django.urls import reverse


class Meta:
    app_label = 'cragslist'


class CreatePostFormCars(forms.Form):
    year_built = forms.IntegerField(label="Year Built")
    make_model = forms.CharField(label="Make/Model")
    color = forms.CharField(label="Color")
    type = forms.CharField(label="Type")
    condition = forms.CharField(label="Condition")
    price = forms.DecimalField(label="Price")
    description = forms.CharField(label="Description")
    city = forms.CharField(label="City")
    phone_number = forms.IntegerField(label="Phone Number")

class CreatePostFormMotorcycles(forms.Form):
    year_built = forms.IntegerField(label="Year Built")
    make_model = forms.CharField(label="Make/Model")
    color = forms.CharField(label="Color")
    type = forms.CharField(label="Type")
    condition = forms.CharField(label="Condition")
    price = forms.DecimalField(label="Price")
    description = forms.CharField(label="Description")
    city = forms.CharField(label="City")
    phone_number = forms.IntegerField(label="Phone Number")


class CreatePostFormBoats(forms.Form):
    year_built = forms.IntegerField(label="Year Built")
    make_model = forms.CharField(label="Make/Model")
    color = forms.CharField(label="Color")
    type = forms.CharField(label="Type")
    condition = forms.CharField(label="Condition")
    price = forms.DecimalField(label="Price")
    description = forms.CharField(label="Description")
    city = forms.CharField(label="City")
    phone_number = forms.IntegerField(label="Phone Number")

class CreatePostFormBooks(forms.Form):
    year_published = forms.IntegerField(label="Year Published")
    author = forms.CharField(label="Author")
    title = forms.CharField(label="Title")
    genre = forms.CharField(label="Genre")
    condition = forms.CharField(label="Condition")
    price = forms.DecimalField(label="Price")
    description = forms.CharField(label="Description")
    city = forms.CharField(label="City")
    phone_number = forms.IntegerField(label="Phone Number")

    
class CreatePostFormFurniture(forms.Form):
    item_name = forms.CharField(label="Item Name")
    brand = forms.CharField(label="Brand")
    material = forms.CharField(label="Material")
    furniture_condition = forms.CharField(label="Condition")
    price = forms.DecimalField(label="Price")
    description = forms.CharField(label="Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormRealEstate(forms.Form):
    address = forms.CharField(label="Address")
    bedrooms = forms.IntegerField(label="Bedrooms")
    bathrooms = forms.IntegerField(label="Bathrooms")
    features = forms.CharField(label="Features")
    price = forms.DecimalField(label="Price")
    estate_description = forms.CharField(label="Estate Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormSwap(forms.Form):
    address = forms.CharField(label="Address")
    bedrooms = forms.IntegerField(label="Bedrooms")
    bathrooms = forms.IntegerField(label="Bathrooms")
    features = forms.CharField(label="Features")
    swap_reason = forms.CharField(label="Swap Reason")
    estate_description = forms.CharField(label="Estate Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormApts(forms.Form):
    address = forms.CharField(label="Address")
    bedrooms = forms.IntegerField(label="Bedrooms")
    bathrooms = forms.IntegerField(label="Bathrooms")
    features = forms.CharField(label="Features")
    rent = forms.DecimalField(label="Rent")
    apt_description = forms.CharField(label="Apt Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormParking(forms.Form):
    parking_name = forms.CharField(label="Parking Name")
    address = forms.CharField(label="Address")
    parking_type = forms.CharField(label="Parking Type")
    size = forms.CharField(label="Size")
    price = forms.DecimalField(label="Price")
    parking_description = forms.CharField(label="Parking Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormVacay(forms.Form):
    vacay_name = forms.CharField(label="Vacay Name")
    address = forms.CharField(label="Address")
    vacay_type = forms.CharField(label="Vacay Type")
    amenities = forms.CharField(label="Amenities")
    price = forms.DecimalField(label="Price")
    vacay_description = forms.CharField(label="Vacay Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormCleaning(forms.Form):
    cleaning_name = forms.CharField(label="Cleaning Name")
    address = forms.CharField(label="Address")
    cleaning_type = forms.CharField(label="Cleaning Type")
    cleaning_hours = forms.CharField(label="Cleaning Hours")
    price = forms.DecimalField(label="Price")
    cleaning_description = forms.CharField(label="Cleaning Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormLawn(forms.Form):
    lawn_name = forms.CharField(label="Lawn Name")
    address = forms.CharField(label="Address")
    lawn_type = forms.CharField(label="Lawn Type")
    lawn_hours = forms.CharField(label="Lawn Hours")
    price = forms.DecimalField(label="Price")
    lawn_description = forms.CharField(label="Lawn Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormCarDetail(forms.Form):
    cardetail_name = forms.CharField(label="Car Detail Name")
    address = forms.CharField(label="Address")
    cardetail_type = forms.CharField(label="Car Detail Type")
    cardetail_hours = forms.CharField(label="Car Detail Hours")
    price = forms.DecimalField(label="Price")
    cardetail_description = forms.CharField(label="Car Detail Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormPets(forms.Form):
    pets_name = forms.CharField(label="Pets Name")
    address = forms.CharField(label="Address")
    pets_type = forms.CharField(label="Pets Type")
    pets_hours = forms.CharField(label="Pets Hours")
    price = forms.DecimalField(label="Price")
    pets_description = forms.CharField(label="Pets Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormCatering(forms.Form):
    catering_name = forms.CharField(label="Catering Name")
    address = forms.CharField(label="Address")
    catering_type = forms.CharField(label="Catering Type")
    catering_hours = forms.CharField(label="Catering Hours")
    price = forms.DecimalField(label="Price")
    catering_description = forms.CharField(label="Catering Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormContract(forms.Form):
    contract_name = forms.CharField(label="Contract Name")
    address = forms.CharField(label="Address")
    contract_type = forms.CharField(label="Contract Type")
    contract_hours = forms.CharField(label="Contract Hours")
    wage = forms.DecimalField(label="Wage")
    contract_description = forms.CharField(label="Contract Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormOdd(forms.Form):
    odd_name = forms.CharField(label="Odd Name")
    address = forms.CharField(label="Address")
    odd_type = forms.CharField(label="Odd Type")
    odd_duration = forms.CharField(label="Odd Duration")
    pay = forms.DecimalField(label="Pay")
    odd_description = forms.CharField(label="Odd Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormFull(forms.Form):
    full_name = forms.CharField(label="Full Name")
    address = forms.CharField(label="Address")
    full_type = forms.CharField(label="Full Type")
    full_hours = forms.CharField(label="Full Hours")
    pay = forms.DecimalField(label="Pay")
    full_description = forms.CharField(label="Full Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormPart(forms.Form):
    part_name = forms.CharField(label="Part Name")
    address = forms.CharField(label="Address")
    part_type = forms.CharField(label="Part Type")
    part_hours = forms.CharField(label="Part Hours")
    pay = forms.DecimalField(label="Pay")
    part_description = forms.CharField(label="Part Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormManu(forms.Form):
    manu_name = forms.CharField(label="Manu Name")
    address = forms.CharField(label="Address")
    manu_type = forms.CharField(label="Manu Type")
    manu_hours = forms.CharField(label="Manu Hours")
    pay = forms.DecimalField(label="Pay")
    manu_description = forms.CharField(label="Manu Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormActivity(forms.Form):
    activity_name = forms.CharField(label="Activity Name")
    address = forms.CharField(label="Address")
    activity_type = forms.CharField(label="Activity Type")
    needed_items = forms.CharField(label="Needed Items")
    price = forms.DecimalField(label="Price")
    activity_description = forms.CharField(label="Activity Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormLost(forms.Form):
    lost_name = forms.CharField(label="Lost Name")
    address = forms.CharField(label="Address")
    lost_type = forms.CharField(label="Lost Type")
    lost_found = forms.CharField(label="Lost/Found")
    contact_info = forms.CharField(label="Contact Info")
    lost_description = forms.CharField(label="Lost Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormChild(forms.Form):
    child_name = forms.CharField(label="Child Name")
    address = forms.CharField(label="Address")
    child_type = forms.CharField(label="Child Type")
    child_hours = forms.CharField(label="Child Hours")
    price = forms.DecimalField(label="Price")
    child_description = forms.CharField(label="Child Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormRide(forms.Form):
    ride_name = forms.CharField(label="Ride Name")
    address = forms.CharField(label="Address")
    ride_type = forms.CharField(label="Ride Type")
    ride_hours = forms.CharField(label="Ride Hours")
    price = forms.DecimalField(label="Price")
    ride_description = forms.CharField(label="Ride Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)

class CreatePostFormVolunteer(forms.Form):
    volunteer_name = forms.CharField(label="Volunteer Name")
    address = forms.CharField(label="Address")
    volunteer_type = forms.CharField(label="Volunteer Type")
    volunteer_hours = forms.CharField(label="Volunteer Hours")
    contact_info = forms.CharField(label="Contact Info")
    volunteer_description = forms.CharField(label="Volunteer Description")
    city = forms.CharField(label="City")
    phone_number = forms.CharField(label="Phone Number", max_length=10)