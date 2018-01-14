# -*- coding: utf-8 -*-
from newcar import NewCarSpider


class Spider(NewCarSpider):
    name = "oldtimer"
    mail_to = "vito.t@outlook.com"
    start_urls = ['https://www.avto.net/Ads/results.asp?znamka=BMW&model=&modelID=&tip=katerikoli%20tip&znamka2=&model2=&tip2=katerikoli%20tip&znamka3=&model3=&tip3=katerikoli%20tip&cenaMin=0&cenaMax=999999&letnikMin=0&letnikMax=1990&bencin=0&starost2=999&oblika=0&ccmMin=0&ccmMax=99999&mocMin=&mocMax=&kmMin=0&kmMax=9999999&kwMin=0&kwMax=999&motortakt=&motorvalji=&lokacija=0&sirina=&dolzina=&dolzinaMIN=&dolzinaMAX=&nosilnostMIN=&nosilnostMAX=&lezisc=&presek=&premer=&col=&vijakov=&vozilo=&airbag=&barva=&barvaint=&EQ1=1000000000&EQ2=1000000000&EQ3=1000000000&EQ4=1000000000&EQ5=1000000000&EQ6=1000000000&EQ7=1110100120&EQ8=1010000001&EQ9=1000000000&KAT=1010000000&PIA=&PSLO=&akcija=&paketgarancije=&broker=&prikazkategorije=&kategorija=&zaloga=&arhiv=&presort=2&tipsort=DESC&stran=']
