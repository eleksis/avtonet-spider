# -*- coding: utf-8 -*-
from newcar import NewCarSpider


class Spider(NewCarSpider):
    name = "330d"
    mail_to = "vito.t@outlook.com"
    start_urls = ['https://www.avto.net/Ads/results.asp?znamka=BMW&model=serija%203:&letnikMin=1999&letnikMax=2005&bencin=202&starost2=999&oblika=0&ccmMin=2500&ccmMax=99999&kmMin=0&kmMax=9999999&kwMin=0&kwMax=999&motortakt=0&motorvalji=0&lokacija=0&sirina=0&dolzina=&dolzinaMIN=0&dolzinaMAX=100&nosilnostMIN=0&nosilnostMAX=999999&lezisc=&presek=0&premer=0&col=0&vijakov=0&vozilo=&airbag=&barva=&barvaint=&EQ1=1000000000&EQ2=1000000000&EQ3=1000000000&EQ4=1000000000&EQ5=1000000000&EQ6=1000000000&EQ7=1110100120&EQ8=1010000001&EQ9=1000000000&KAT=1010000000&PIA=&PSLO=&akcija=0&paketgarancije=&broker=0&prikazkategorije=0&kategorija=0&zaloga=10&arhiv=0&presort=3&tipsort=DESC&stran=1&subSORT=2&subTIPSORT=DESC']
