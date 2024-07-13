from django.shortcuts import render
from .models import Country, ItemTest, Specification, CountryTestRequirement

def minstandardtest_view(request):
    countries = Country.objects.all()
    item_tests = ItemTest.objects.all()
    
    context = {
        'countries': countries,
        'item_tests': item_tests,
    }
    return render(request, 'app_standard/minstandardtest.html', context)
