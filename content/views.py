from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Property, City, Visits

@login_required(
    login_url="/auth/login"
)
def home(request):
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    city = request.GET.get('city')
    type = request.GET.getlist('type')
    cities = City.objects.all()

    if price_min or price_max or city or type:
        if not price_min:
            price_min = 0
        if not price_max:
            price_max = 9999999999
        if not type:
            type = ['A', 'H']
        property = Property.objects.filter(value__gte=price_min)\
        .filter(value__lte=price_max)\
        .filter(type_property__in=type).filter(city=city)
    else:
        property = Property.objects.all()

    return render(request, 'home.html', {'properties': property, 'cities':cities})


def property(request, id):
    property = get_object_or_404(Property, id=id)
    suggestions = Property.objects.filter(city=property.city).exclude(id=id)[:2]
    return render(request, 'property.html', {'property':property, 'suggestions':suggestions})

def schedule_visits(request):
    user = request.user
    day = request.POST.get('day')
    schedule = request.POST.get('schedule')
    id_property = request.POST.get('id_property')

    visits = Visits(
        property_id=id_property,
        user=user,
        day=day,
        schedule=schedule
    )

    visits.save()
    return redirect('/schedules')

def schedules(request):
    visits = Visits.objects.filter(user=request.user)
    return render(request, "schedules.html", {'visits': visits})

def cancel_schedule(request, id):
    visits = get_object_or_404(Visits, id=id)
    visits.status = "C"
    visits.save()
    return redirect('/schedules')
