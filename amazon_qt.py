
"""

Batuhan Ökmen


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
            
            
            for hayda in range(0,len(urun_kodlari)):
                
                
            
                try:
                    
                    print("%s veriden % i işlendi"%(len(urun_kodlari),hayda))
                except:pass
                print("###################################################################")
                print("sayfa acildi")
                driver.get(urun_kodlari[hayda])
                sacma_1=0
                
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
                         
                    try:
                        try:
                            
                            soupl=str(soup).split('"attach-base-product-price"')[1].split('"')[3]=="0.0"
                        except:
                            pass
                        
                        try:
                            # gelince al bunu koy https://www.amazon.com/dp/B01FXC7JWQ    
                            soup_sart=str(soup).split('<span class="a-size-medium a-color-state">')[1].split("</span>")[0]
                            # for dongüsü at içinde varsa true falan yapsın
                            gun=float(self.ui.gun.text())
                            hafta=float(self.ui.hafta.text())
                            ay=float(self.ui.ay.text())
                            gun_sart=""
                            hafta_sart=""
                            ay_sart=""
                            
                            
                            if gun=="":
                                gun_sart=True
                            else:
                                    
                                for gun_icin in range(0,50):
                                    if  (str(gun_icin) in str(soup_sart)) and (str("days") in str(soup_sart)):
                                        gun_sart=gun_icin <= int(gun)
                                        break
                            
                            if hafta=="":
                                hafta_sart=True
                            else:
                                    
                                for hafta_icin in range(0,50):
                                    if  (str(hafta_icin) in str(soup_sart)) and (str("weeks") in str(soup_sart)):
                                        hafta_sart=hafta_icin <= int(hafta)
                                        break
                            
                            if ay=="":
                                ay_sart=True
                                
                            else:
                                    
                                for ay_icin in range(0,50):
                                    if  (str(ay_icin) in str(soup_sart)) and (str("months") in str(soup_sart)):
                                        ay_sart=ay_icin <= int(ay)
                                        break
                                
                                    
                            
                            
                            
                            
                            
                            
                            
                            soup_sart=gun_sart and hafta_sart and ay_sart
                        except:
                            pass
                        currently_unavaible=(str(soup).split('<span class="a-color-price a-text-bold">')[1].split("</span>")[0]=="Currently unavailable." )
                        soupa= (currently_unavaible or soupl or soup_sart) and Stok_durumuna_etki==False
                        print("1 stokta var mi yok mu: ",str(soupa))
                        if soupa==True:
                                print("ürün stokta yok:",str(hayda))
                                urun_stokta_mi=True
                                
                                stok_cektim=stok_icin[hayda].split("<Miktar>")[1].split("</Miktar>")[0]
                                stok_icin[hayda]=stok_icin[hayda].replace("<Miktar>"+str(stok_cektim)+"</Miktar>","<Miktar>0</Miktar>")
                                sacma_1=1
                                soupl=False
                                soup_sart=False
                    except:
                        pass
                    
                    try:
                        if sacma_1==0:
                            # /html/body/div[1]/div[2]/div[9]/div[3]/div[1]/div[6]/div/div/div/div/div/form/div/div/div[2]/div[2]/span/span/span/a
                            
                            """
                            try:
                                #burası da işe yarayabilir ama yeni eklediğim yöntem daha kullanışlı olacak
                                
                                farkli_bir_varyasyon_fiyat_icin=str(soup).split('<td class="comparison_baseitem_column"> <span class="a-color-price a-text-bold">')[1].split("</span>")[0].split("$")[1][:-1]
                            except:pass
                            
                            if farkli_bir_varyasyon_fiyat_icin != False:
                                fiyat_cekme=ceil(float(farkli_bir_varyasyon_fiyat_icin))*Carpan
                                farkli_bir_varyasyon_fiyat_icin=False
                            else:                                
                                soup=str(soup).split("Total")
                                fiyat_cekme=float((soup[1].split("</div>")[0].split("$")[1].split("<")[0][:-1]))*Carpan
                                fiyat_cekme=ceil(fiyat_cekme)
                            """
                            
                            devam_mi=False
                            try:
                                 element = WebDriverWait(driver, 0.2).until(
                                     EC.visibility_of_element_located((By.XPATH, '//*[@id="exports_desktop_unqualifiedBuybox_all_buying_options_cta_feature_div"]/div[2]'))
                                 )
                                 devam_mi=True
                            except:
                                 devam_mi=False

                            
                            if devam_mi==True:
                                print("Değişimli Ürün sayfasına gidilecek")
                                devam_mi=False
                                #stokta var mı yok mu bak bakalım
                                
                                try:
                                    
                                    
                                    buying_options = driver.find_element_by_xpath('//*[@id="exports_desktop_unqualifiedBuybox_all_buying_options_cta_feature_div"]/div[2]')
                                    buying_options.click()
                                    time.sleep(3)
                                    add_cart = driver.find_element_by_xpath('//*[@id="a-autoid-2-offer-1"]/span')
                                    add_cart.click()
                                    print("sepette")
                                    time.sleep(3)
                                    
                                    
                                    #go_to_cart
                                    
                                    driver.get("https://www.amazon.com/gp/cart/view.html?ref_=nav_cart")
                                    
                                    go_to_product=driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div[3]/div/div[2]/div[4]/div/form/div[2]/div[3]/div[4]/div/div[1]/div/div/div[2]/ul/li[1]/span/a/span[1]/span')
                                    go_to_product.click()
                                    driver.switch_to.window(driver.window_handles[1])
                                    print("ürün bulundu ürüne gidildi")
                                    time.sleep(3)
                                    html = driver.page_source
                                    soup = BeautifulSoup(html)
                                    
                                    soup=str(soup).split("Total")
                                    fiyat_cekme=float((soup[1].split("</div>")[0].split("$")[1].split("<")[0][:-1]))*Carpan
                                    fiyat_cekme=ceil(fiyat_cekme)
                                    print("ürün stokta var:",str(hayda))
                                    print("çekilen fiyat:",str(fiyat_cekme))
                                    driver.close()
                                    driver.switch_to.window(driver.window_handles[0])
                                    time.sleep(2)
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
                                except:
                                    pass
                                
                                
                                # carta geri gidiliyor
                                driver.get("https://www.amazon.com/gp/cart/view.html?ref_=nav_cart")
                                time.sleep(0.5)
                                delete_cart = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div[3]/div/div[2]/div[4]/div/form/div[2]/div[3]/div[4]/div/div[1]/div/div/div[2]/div[1]/span[2]/span/input')
                                delete_cart.click()
                                #silindi
                            
                            
                            else:
                                
                                
                                                               
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
                
                
        
        
        
    
    
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        mainWin = MainWindow()
        mainWin.show()
        sys.exit( app.exec_() )
except Exception as e:
    print("hata",e)
    input("enter")

