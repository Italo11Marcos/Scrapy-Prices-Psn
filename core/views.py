from django.shortcuts import render
from .scrapy import *
from .models import *

# Create your views here.
def index(request):

    if request.method == "POST":
        urlGreedFall = 'https://store.playstation.com/pt-br/product/UP4133-CUSA14211_00-GREEDFALL0000000'
        urlUntilDawn = 'https://store.playstation.com/pt-br/product/UP9000-CUSA00359_00-UNTILDAWN0000001'
        urlWitcher3 = 'https://store.playstation.com/pt-br/product/UP4497-CUSA05725_00-00000000000GOTY5'
        urlImmortals = 'https://store.playstation.com/pt-br/product/UP0001-PPSA01507_00-GAME000000000000'
        urlACValhalla = 'https://store.playstation.com/pt-br/product/UP0001-PPSA01491_00-GAME000000000000'
        urlDaysGone = 'https://store.playstation.com/pt-br/product/UP9000-CUSA08966_00-DAYSGONECOMPLETE'
        urlGodofWar = 'https://store.playstation.com/pt-br/product/UP9000-CUSA07408_00-00000000GODOFWAR'
        
        scrapyGreedFall(urlGreedFall)
        scrapyUntildawn(urlUntilDawn)
        scrapyWitcher(urlWitcher3)
        scrapyImmortals(urlImmortals)
        scrapyAcvalhalla(urlACValhalla)
        scrapyDaysgone(urlDaysGone)
        scrapyGodofwar(urlGodofWar)

        u = Update.objects.create()
        u.save()

    greedfall = Greedfall.objects.all().order_by('-price')
    untildawn = Untildawn.objects.all().order_by('-price')
    witcher = Witcher.objects.all().order_by('-price')
    immortals = Immortals.objects.all().order_by('-price')
    acvalhalla = Acvalhalla.objects.all().order_by('-price')
    daysgone = Daysgone.objects.all().order_by('-price')
    godofwar = Godofwar.objects.all().order_by('-price')
    
    lastUpdate = Update.objects.order_by('-date')[0]

    context = {
            'greedfall': greedfall,
            'untildawn': untildawn,
            'witcher': witcher,
            'immortals': immortals,
            'acvalhalla': acvalhalla,
            'daysgone': daysgone,
            'godofwar': godofwar,
            'lastUpdate': lastUpdate
        }

    return render(request, 'index.html', context)
