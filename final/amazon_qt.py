
"""

Batuhan Ökmen


"""




"""import requests
import json
import base64

from getmac import get_mac_address as gma
print(gma())

"""







try:
        

    
    import sys
    
    from math import ceil
    from PyQt5 import QtWidgets,QtGui
    from PyQt5.QtWidgets import *
    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout, QProgressBar, QComboBox, QFileDialog
    from anasayfa_python import Ui_Widget
    from PyQt5.QtCore import QBasicTimer
    from PyQt5.QtGui import *
    from PyQt5.QtGui import QIcon
    from PyQt5.QtCore import *
    from PyQt5.QtCore import QRect
    #from PyQt5.uic import loadUi
    from bs4 import BeautifulSoup
    import urllib.request as urllib2
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import selenium
    from  selenium import webdriver

    import time
    
    
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_Widget()
            self.ui.setupUi(self) 
            
            #butonlar
            
            self.ui.dosya_yukle.clicked.connect(self.dosyasec)
            self.ui.baslat.clicked.connect(self.baslat)
    
            #self.ui.OtomatikOkuma.isChecked() ==True:
        def dosyasec(self):
            global fname
            
            fname=QFileDialog.getOpenFileName(self, 'Open file', 'D:\codefirst.io\PyQt5 tutorials\Browse Files')
            #dosya_yukle_label
            self.ui.dosya_yukle_label.setText(fname[0])
            
            
            
            
        def baslat(self):
            
            carpan_al=float(self.ui.katsayi.text())
    
                      
            driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
            Carpan=carpan_al
            
            
            driver.get("https://www.amazon.com")
            with open(fname[0],"r", encoding="utf8") as dosya:
                xml_dosyasi = dosya.read()  
                
                
            stok_icin=xml_dosyasi.split("<Urun>")
            stok_icin.pop(0)
            bolunmus=xml_dosyasi.split("<Kod>")
            bolunmus.pop(0)
            soup_sart=False
            soupl=False
            urun_kodlari=[]
            urun_stokta_mi=True
            farkli_bir_varyasyon_fiyat_icin=False
            sacma_1=0
            devam_mi=False
            
            time.sleep(0.2)
            for urun_kodlari_alma in range(0, len(bolunmus)):
                
                urun_kodu="https://www.amazon.com/dp/"+str(bolunmus[urun_kodlari_alma].split("<")[0])
                urun_kodlari.append(urun_kodu)
            
            
            # tl mi dolar mı onu ayarlayacağız
            
            if self.ui.usd.isChecked() == True:
                pass
            else:
                """
                driver.get("https://www.amazon.com/gp/customer-preferences/select-currency/ref=icp_cop_flyout_change?preferencesReturnUrl=%2F")
                time.sleep(5)
                #
                driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div[3]/div/p/span[2]/span/span/span').click()
                try:
                    
                    driver.find_element_by_xpath('//*[@id="a-popover-1"]/div/div/ul/li[3]').click()
                except:
                    
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/ul/li[3]/a').click()
                pass
           
                driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/span[2]/span/input').click()
                """
                
                pass
            for hayda in range(0,len(urun_kodlari)):
                
                
            
                try:
                    
                    print("%s veriden % i işlendi"%(len(urun_kodlari),hayda))
                except:pass
                print("###################################################################")
                
                
                
                
                
                
                
                
                driver.get(urun_kodlari[hayda])
                sacma_1=0
                
                #kontrol 1
                
                try:
                     element = WebDriverWait(driver, 10).until(
                         EC.visibility_of_element_located((By.XPATH, '//*[@id="a-page"]'))
                     )
                    
                except:
                     pass
                
                
                print("sayfa acildi")
                
                
                try:
                    time.sleep(0.2)    
                    html = driver.page_source
                    soup = BeautifulSoup(html)
                    
                    
                    
                    
                    
                    
                    Stok_durumuna_etki=False
                    
                    try:
                         element = WebDriverWait(driver, 0.2).until(
                             EC.visibility_of_element_located((By.XPATH, '//*[@id="exports_desktop_unqualifiedBuybox_all_buying_options_cta_feature_div"]/div[2]'))
                         )
                         Stok_durumuna_etki=True
                    except:
                         Stok_durumuna_etki=False
                         
                    #kontrol 2
                         
                    try:
                         element = WebDriverWait(driver, 0.1).until(
                             EC.visibility_of_element_located((By.XPATH, '//*[@id="buybox-see-all-buying-choices"]/span/a'))
                         )
                         Stok_durumuna_etki=True
                    except:
                         Stok_durumuna_etki=False
                         
                         
                    soup_sart=False     
                    
                    try:
                        try:
                            soupl=False
                            soupl=str(soup).split('"attach-base-product-price"')[1].split('"')[3]=="0.0"
                        except:
                            pass
                        yeni_gun_sart=True
                        try:
                            # gelince al bunu koy https://www.amazon.com/dp/B01FXC7JWQ    
                            soup_sart=str(soup).split('<span class="a-size-medium a-color-state">')[1].split("</span>")[0]
                            # for dongüsü at içinde varsa true falan yapsın
                            gun=float(self.ui.gun.text())
                            #hafta=float(self.ui.hafta.text())
                            #ay=float(self.ui.ay.text())
                            gun_sart=False
                            hafta_sart=False
                            ay_sart=False
                            yeni_gun_sart=False
                            try:

                                for gun_icin in range(0,50):
                                        if  (str(gun_icin) in str(soup_sart)) and (str("days") in str(soup_sart)):
                                            gun_sart=gun_icin <= int(gun)
                                            break
                                hafta_sart=(str("weeks") in str(soup_sart))
                                ay_sart=(str("months") in str(soup_sart))
                                hafta_ay_kontrol= hafta_sart or ay_sart
                            except:
                                pass
  
                            if gun_sart == True:
                                yeni_gun_sart=True
                                #Ürünü stokta var olarak işaretlemek zorundasınız.
                            else:
                                #Eğer gun şartımız True olmaz ise hafta ve aya bakılır
                                #hafta ve ay şartının ikisi de False olmak zorundadır eğer biri True olursa 
                                #Ürün stokta yok olarak belirtilmelidir.
                                
                                if hafta_ay_kontrol == False:
                                    
                                    yeni_gun_sart=False


                        except:
                            pass
                        try:
                            
                            currently_unavaible=(str(soup).split('<span class="a-color-price a-text-bold">')[1].split("</span>")[0]=="Currently unavailable." )
                        except:
                            currently_unavaible=False
                        
               
                        
                        soupa= (yeni_gun_sart== False) or (currently_unavaible==True) or (soupl==True) or ( Stok_durumuna_etki==True)
                        
                        print("ürün stokta yok:",str(soupa))
                

                        
                        
                        
                  
                        if soupa==True:

                                    
                                print("ürün stokta yok:",str(hayda))
                               
                                
                                stok_cektim=stok_icin[hayda].split("<Miktar>")[1].split("</Miktar>")[0]
                                stok_icin[hayda]=stok_icin[hayda].replace("<Miktar>"+str(stok_cektim)+"</Miktar>","<Miktar>0</Miktar>")
                                sacma_1=1
                                soupl=False
                                soup_sart=False
                    except:
                        pass
                    
                    try:
                        if sacma_1==0:
      
                            try:
                                
                         
    
                                                                   
                                    soup=str(soup).split("Total")
                                    fiyat_cekme=float((soup[1].split("</div>")[0].split("$")[1].split("<")[0][:-1]))*Carpan

                                    fiyat_cekme=ceil(fiyat_cekme)
                                    print("ürün stokta var:",str(hayda))
                                    print("çekilen fiyat:",str(fiyat_cekme))
                                    #stok değişti
                                    
                                    try:
                                            stok_cektim=stok_icin[hayda].split("<Miktar>")[1].split("</Miktar>")[0]
                                            stok_icin[hayda]=stok_icin[hayda].replace("<Miktar>"+str(stok_cektim)+"</Miktar>","<Miktar>10</Miktar>")
                                            
                                           #fiyat değişti
                                            try:    
                                               stok_icin[hayda]=stok_icin[hayda].replace("<Fiyat>"+str(stok_icin[hayda].split("<Fiyat>")[1].split("</Fiyat>")[0])+"</Fiyat>","<Fiyat>"+str(fiyat_cekme)+"</Fiyat>")
                                               print("Fiyat değişti")
                                            except:
                                                pass
                                           
                                    except:
                                        pass
                                    
                                    try:
                                        
                                        #kargo süresi burası eklenecek !
                                        termin_suresi=(self.ui.termin_suresi.text())
                                        HazirlamaSuresi_cektim=stok_icin[hayda].split("<HazirlamaSuresi>")[1].split("</HazirlamaSuresi>")[0]
                                        stok_icin[hayda]=stok_icin[hayda].replace("<HazirlamaSuresi>"+str(HazirlamaSuresi_cektim)+"</HazirlamaSuresi>","<HazirlamaSuresi>"+str(termin_suresi)+"</HazirlamaSuresi>")
                                        print("Termin süresi %s ayarlandı."%termin_suresi)
                                    except:
                                        pass
                                    
                                    
                                    try:
                                        #indirim burası eklenecek !
                                        indirim_suresi=str(self.ui.indirim.text())
                                        indirim_cektim=stok_icin[hayda].split("<IndirimTutari>")[1].split("</IndirimTutari>")[0]
                                        stok_icin[hayda]=stok_icin[hayda].replace("<IndirimTutari>"+str(indirim_cektim)+"</IndirimTutari>","<IndirimTutari>"+str(indirim_suresi)+"</IndirimTutari>")
                                        
                                    
                                    except:
                                        pass
                                    
                                  
                                    
                                    try:
                                        #teslimat Sablonu burası eklenecek !
                                        TeslimatSablonu=str(self.ui.teslimatsablon.text())
                                        TeslimatSablonu_cektim=stok_icin[hayda].split("<TeslimatSablonu>")[1].split("</TeslimatSablonu>")[0]
                                        stok_icin[hayda]=stok_icin[hayda].replace("<TeslimatSablonu>"+str(TeslimatSablonu_cektim)+"</TeslimatSablonu>","<TeslimatSablonu>"+str(TeslimatSablonu)+"</TeslimatSablonu>")
                                        
                                    
                                    except:
                                        pass
                                    
                                    try:
                                        #urun onayı burası eklenecek !
                                        UrunOnayi=str(self.ui.urunonay.text())
                                        UrunOnayi_cektim=stok_icin[hayda].split("<UrunOnayi>")[1].split("</UrunOnayi>")[0]
                                        stok_icin[hayda]=stok_icin[hayda].replace("<UrunOnayi>"+str(UrunOnayi_cektim)+"</UrunOnayi>","<UrunOnayi>"+str(UrunOnayi)+"</UrunOnayi>")
                                        
                                    
                                    except:
                                        pass
                                    
                                    try:
                                        
                                        #tl dolar burası eklenecek !
                                        #CHECK BOXTAN VERİ AL YERLEŞTRİ İŞTE
                                        if self.ui.usd.isChecked() == True:
                                            
                                            ParaBirimi="USD"
                                        ParaBirimi="USD"
                                        #tamir olana kadar
                               
                                        ParaBirimi_cektim=stok_icin[hayda].split("<ParaBirimi>")[1].split("</ParaBirimi>")[0]
                                        stok_icin[hayda]=stok_icin[hayda].replace("<ParaBirimi>"+str(ParaBirimi_cektim)+"</ParaBirimi>","<ParaBirimi>"+str(ParaBirimi)+"</ParaBirimi>")
                                        
                                        pass
                                    
                                    except:
                                        pass
                            except:
                                #stok sıfırla
                                print("ürün stokta yok:",str(hayda))
                               
                                
                                stok_cektim=stok_icin[hayda].split("<Miktar>")[1].split("</Miktar>")[0]
                                stok_icin[hayda]=stok_icin[hayda].replace("<Miktar>"+str(stok_cektim)+"</Miktar>","<Miktar>0</Miktar>")
                                sacma_1=1
                                soupl=False
                                soup_sart=False
                                pass
                    except: 
                        pass 
                    
                 

                    
                except:
                    pass
                
                   
            
            
            
            
            
            #birleştirme
            
            xlm_birleştirme=""
            hataGiderme=len(stok_icin)
            sayac=1
            for ekle_bakalim in stok_icin:
                if sayac==hataGiderme-1:
                    xlm_birleştirme=xlm_birleştirme+ekle_bakalim+"</Urunler>"
                    break
                else:
                    
                    xlm_birleştirme=xlm_birleştirme+ekle_bakalim+"<Urun>"
                sayac=sayac+1
            
            xlm_birleştirme="<Urunler><Urun>"+xlm_birleştirme
            with open("model_cikti.xml","w", encoding="utf8") as dosya:
                xml_dosyasi = dosya.write(xlm_birleştirme)  
                
            try:
                    
                if self.ui.kapat.isChecked() == True:
                    self.ui.close()
            except:
                pass
        
    
    
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        mainWin = MainWindow()
        mainWin.show()
        sys.exit( app.exec_() )
except Exception as e:
    print("hata",e)
    input("enter")

