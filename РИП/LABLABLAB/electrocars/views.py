from django.shortcuts import render

from django.http import HttpRequest

stations = list()
station = {'id':0,'photo':'http://localhost:9000/bucket1/1.png','shortName':'Энергия Москвы',
            'fullName':'Зарядная станция "Энергия Москвы"',
            'adress':'115054, г.Москва, ул. Бахрушина, 20','description':
            "Типы подключения зарядного устройства: type 2. Станция рассчитана на подключение до 2-х автомобилей одновременно.",
            'work_time':"круглосуточно"}
stations.append(station)
station = {'id':1,'photo':'http://localhost:9000/bucket1/2.png','shortName':'Фора Charging Station',
            'fullName':'Зарядная станция "Фора"',
            'adress':'142770, г.Москва, Коммунарка, стоянка гипермаркета "Глобус"','description':
            "Типы подключения зарядного устройства: type 2 - 22.0 кВт, розетка - 3.6 кВт. Станция рассчитана на подключение одного автомобиля.",
            'work_time':"круглосуточно"}
stations.append(station)
station = {'id':2,'photo':'http://localhost:9000/bucket1/3.png','shortName':'EV-Time Charging Station',
            'fullName':'Зарядная станция "EV-Time"',
            'adress':'121353, г.Москва, МКАД, 51-й километр','description':
            "Типы подключения зарядного устройства: type 2 - 43.0 кВт, CHAdeMO - 50.0 кВт, CCS - 50.0 кВт. Станция рассчитана на подключение до 3-х автомобилей одновременно.",
            'work_time':"07:00-22:00"}
stations.append(station)
station = {'id':3,'photo':'http://localhost:9000/bucket1/4.png','shortName':'"МосЭнерго" Charging Station',
            'fullName':'Зарядная станция "МосЭнерго"',
            'adress':'119048, Москва, ул. Савельева','description':
            "Типы подключения зарядного устройства: type 2 - 22.0 кВт. Станция рассчитана на подключение одного автомобииля.",
            'work_time':"круглосуточно"}
stations.append(station)


reports = list()
reports.append({'id':0, 'stations':[{'station': stations[0],'power':'1200'},
                                    {'station': stations[1],'power':'800'}],
                        'report_date':'13.09.2024'})
reports.append({'id':1, 'stations':[{'station': stations[0],'power':'1500'},
                                    {'station': stations[2],'power':'1100'}],
                        'report_date':'21.09.2024'})
currentReport = reports[1]

def electrocars_view(request):
    station_name = request.GET.get("station_name")
    filteredStations = list()
    if(not station_name):
        return render(request, 'main_page.html', {'stations':stations,'filter':"Название станции",'currentReport':currentReport,'count':len(currentReport['stations'])})

    for station in stations:
        if station_name.lower() in station['shortName'].lower():
            filteredStations.append(station)
    
    return render(request, 'main_page.html', {'stations':filteredStations,'filter':station_name,'currentReport':currentReport,'count':len(currentReport['stations'])})
    


def description(request,id):
    return render(request,'description.html',stations[id])


def reportInfo(request,id):
    return render(request,'report_page.html', reports[id])