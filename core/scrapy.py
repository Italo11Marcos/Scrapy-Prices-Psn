import requests
from bs4 import BeautifulSoup
from .models import *

def clear_price(priceWB):
    priceWB = priceWB.strip('R')
    priceWB = priceWB.strip('$')
    priceWB = priceWB.strip('')
    priceWB = priceWB.replace(',', '.')
    priceWB = priceWB.replace(' ', '')
    priceWB = float(priceWB)
    return priceWB


def scrapyGreedFall(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    priceWB = soup.find('span', attrs={"psw-h3"}).text
    priceWB = str(priceWB)
    priceWB = clear_price(priceWB)
    obj = Greedfall.objects.create(price=priceWB)
    obj.save()

def scrapyWitcher(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    priceWB = soup.find('span', attrs={"psw-h3"}).text
    priceWB = str(priceWB)
    priceWB = clear_price(priceWB)
    obj = Witcher.objects.create(price=priceWB)
    obj.save()
    
def scrapyUntildawn(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    priceWB = soup.find('span', attrs={"psw-h3"}).text
    priceWB = str(priceWB)
    priceWB = clear_price(priceWB)
    obj = Untildawn.objects.create(price=priceWB)
    obj.save()

def scrapyAcvalhalla(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    priceWB = soup.find('span', attrs={"psw-h3"}).text
    priceWB = str(priceWB)
    priceWB = clear_price(priceWB)
    obj = Acvalhalla.objects.create(price=priceWB)
    obj.save()

def scrapyGodofwar(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    priceWB = soup.find('span', attrs={"psw-h3"}).text
    priceWB = str(priceWB)
    priceWB = clear_price(priceWB)
    obj = Godofwar.objects.create(price=priceWB)
    obj.save()

def scrapyDaysgone(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    priceWB = soup.find('span', attrs={"psw-h3"}).text
    priceWB = str(priceWB)
    priceWB = clear_price(priceWB)
    obj = Daysgone.objects.create(price=priceWB)
    obj.save()

def scrapyImmortals(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    priceWB = soup.find('span', attrs={"psw-h3"}).text
    priceWB = str(priceWB)
    priceWB = clear_price(priceWB)
    obj = Immortals.objects.create(price=priceWB)
    obj.save()