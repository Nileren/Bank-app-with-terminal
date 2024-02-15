import os
import time
class banka :
    dictt={ 
    "ad":"",
    "soyad":"",
    "bakiye":0,
    "ekbakiye":0
    }
    def __init__(self,isim,soyad,bakiye=0,ekbakiye=2000):
        self.dictt["ad"]=isim
        self.dictt["soyad"]=soyad
        self.dictt["bakiye"]=bakiye
        self.dictt["ekbakiye"]=ekbakiye
        
    def returndictt(self):
        return self.dictt

isim=input("müşteri ismi:")
soyad=input("müşteri soyad:")
try:
    bakiye=int(input("müşteri bakiye:"))
except:
    print("girilen değer int değere dönüştürülemiyor tekrar gir")
    bakiye=int(input("müşteri bakiye:"))
try:
    ekbakiye=(int(input("müşteri ekbakiye:")))
except:
    print("girilen değer int değere dönüştürülemiyor tekrar gir")
    ekbakiye=(int(input("müşteri ekbakiye:")))
global person
personini=banka(isim,soyad,bakiye,ekbakiye)
person=personini.returndictt()
#bana dönen bir dict liste müsteri bilgileri şekline 
def sleep():
    time.sleep(3)
def parayatır(v_person):
    amount=int(input("yatırmak istediğiniz miktar:"))
    if amount>=0:
        v_person["bakiye"] +=amount
    else:
        print("yatırmak istediğiniz miktar negatif olamaz..")

def paracek(v_person):
    amount=int(input("çekmek istediğiniz para tutarı:"))
    if amount>v_person["bakiye"]:
        print("yetersiz bakiye...\nek bakiye kullanmak ister misiniz?")
        request=int(input("kullanmak için 1\nişlemi sonlandırmak için 0 tuşlayın"))
        if request==1:
            if v_person["bakiye"]+v_person["ekbakiye"]>=amount:
                print("para çekme işlemi başarılı")
                v_person["bakiye"]=0
                v_person["ekbakiye"]:(amount-bakiye)*(-1)
                return
            else:
                print("miktarı küçültmeyi deneyin")
                return
        else:
            print("işlem iptal")
            return            
    else:

        v_person["bakiye"]=v_person["bakiye"]-amount
        return

def showBalance(v_person):
    bakiye=v_person["bakiye"]
    print(f"hesap bakiyesi:{bakiye}")
    ekbakiye=v_person["ekbakiye"]
    print(f"ek bakiye:{ekbakiye}")
    print("\n")

    return
def uptadename(v_person):
        name=input("enter name to rename:")
        v_person["ad"]=name
        return
def uptadelastname(v_person):
    lastname=input("enter the true last name to update last name:")
    v_person["soyad"]=lastname
    return

def updateAdditionalBalance(person):
    newB=input("enter the amount of new additional balance:")
    person["ekbakiye"]=newB
    return
def showperson(person):
    ad=person["ad"]
    print(f"ad:{ad}\n")
    soyad=person["soyad"]
    print(f"soyad:{soyad}\n")

def pressmenu():
    print("1-para yatır")
    print("2-para çek")
    print("3-bakiye görüntüle")
    print("4-isim yenile")
    print("5-soyisim yenile")
    print("6-ek bakiye güncelle")
    print("7-kullanıcı ad soy-ad gör")

    print("8 çıkıs için or anything")
def clearTerminal():
    os.system('cls')
    return

def npmstart(person):
    while True:
        pressmenu()
        try:
            islem=int(input("yapmak istediğiniz işlemiz numarasını giriniz:"))
        except:
            print("girilen değer int değere dönüştürülemiyor (break)")
            break   
        clearTerminal()
        if islem==1:
            parayatır(person)
            sleep()
           
            continue
        elif islem==2:
            paracek(person)
            sleep()
            
            continue
        elif islem==3:
            showBalance(person)
            sleep()
            
            continue
        elif islem==4:
            uptadename(person)
            sleep()
            
            continue
        elif islem==5:
            uptadename(person)
            sleep()
            
            continue
        elif islem==6:
            uptadelastname(person)
            sleep()
          
            continue
        elif islem==6:
            updateAdditionalBalance(person)
            sleep()
           
            continue
        elif islem==7:
            showperson(person)
            sleep()
            
            continue
        else:
            print("kod bitti....")
            sleep()
            
            break
        
npmstart(person)