from lib2to3.pgen2 import driver
from re import A
from traceback import print_tb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime 
import time
import locale
import sqlite3
#---------------------Function-------------------------------
#Local Tarih bilgisini Türkiyeye göre ayarladık
locale.setlocale(locale.LC_ALL, 'tr_TR')

#---------------------Write Function-------------------------------

#Çekilen USD'yi ekrana yazdırma fonksiyonu
def screeWrite(usd):
    now1= datetime.datetime.now()
   # zaman=datetime.datetime.strftime(now1, '%X')
    zaman=datetime.datetime.strftime(now1, '%c')
    print("Usd Döviz Kuru")
    print("Date: " + usd[0])
    print("Usd Buy: " + usd[1])
    print("Usd Sell: " + usd[2] )
    print("Usd Max: " + usd[3] )
    print("Usd Min: " + usd[4] )
    print("Usd Change: " + usd[5] )
    print("-------------------------")

#Çekilen Euro'yu ekrana yazdırma fonksiyonu
def screeWrite(euro):
    now2= datetime.datetime.now()
   # zaman=datetime.datetime.strftime(now1, '%X')
    zaman=datetime.datetime.strftime(now2, '%c')
    print("Euro Döviz Kuru")
    
    print("Date: " + euro[0])
    print("Euro Buy: " + euro[1])
    print("Euro Sell: " + euro[2] )
    print("Euro Max: " + euro[3] )
    print("Euro Min: " + euro[4] )
    print("Euro Change: " + euro[5] )
    print("-------------------------")


#Çekilen Brent Petrolü ekrana yazdırma fonksiyonu
def screeWrite(petrol):
    now3= datetime.datetime.now()
   # zaman=datetime.datetime.strftime(now1, '%X')
    zaman=datetime.datetime.strftime(now3, '%c')
    print("Brent Petrol Döviz Kuru")
    print("Tarih: " + petrol[0])
    print("Brent Petrol : " + petrol[1] + " USD")
    print("Brent Petrol Min: " + petrol[2] )
    print("Brent Petrol Max: " + petrol[3] )
    print("Brent Petrol Change: " + petrol[4] )
    print("-------------------------")

#---------------------Take Function-------------------------------


#Web sitesinden Usd'yi çeker ve dizi return eder.
def takeit1(usd):
    now1= datetime.datetime.now()
    usd[0]= datetime.datetime.strftime(now1, '%c')
    usd[1]= driver.find_element(By.CSS_SELECTOR,"tr > td:nth-child(2)").text
    usd[2]=driver.find_element(By.CSS_SELECTOR,"tr > td:nth-child(3)").text
    usd[3]= driver.find_element(By.CSS_SELECTOR,"tr > td:nth-child(4)").text   
    usd[4]=driver.find_element(By.CSS_SELECTOR,"tr > td:nth-child(5)").text
    usd[5]=driver.find_element(By.CSS_SELECTOR,"tr > td:nth-child(6)").text
    
    screeWrite(usd)  #Ekrana çekilen veriyi yazar.
    return usd 


#Web sitesinden Euro'yu çeker ve dizi return eder.
def takeit2(euro):
    now1= datetime.datetime.now()
    euro[0]= datetime.datetime.strftime(now1, '%c')
    euro[1]= driver.find_element(By.CSS_SELECTOR , " tr:nth-child(2) > td:nth-child(2)").text
    euro[2]=driver.find_element(By.CSS_SELECTOR , " tr:nth-child(2) > td:nth-child(3)").text
    euro[3]= driver.find_element(By.CSS_SELECTOR , " tr:nth-child(2) > td:nth-child(4)").text
    euro[4]=driver.find_element(By.CSS_SELECTOR , " tr:nth-child(2) > td:nth-child(5)").text
    euro[5]=driver.find_element(By.CSS_SELECTOR , " tr:nth-child(2) > td:nth-child(6)").text
    
    screeWrite(euro)  #Ekrana çekilen veriyi yazar.
    return euro


#Web sitesinden Petrolü çeker ve dizi return eder.
def takeit3(petrol):
    now1= datetime.datetime.now()
    petrol[0]= datetime.datetime.strftime(now1, '%c')
    petrol[1]= driver.find_element(By.CSS_SELECTOR,"tr > td:nth-child(2)").text
    petrol[2]=driver.find_element(By.CSS_SELECTOR,"tr > td:nth-child(3)").text
    petrol[3]= driver.find_element(By.CSS_SELECTOR,"tr > td:nth-child(4)").text   
    petrol[4]=driver.find_element(By.CSS_SELECTOR,"tr > td:nth-child(5)").text
    
    screeWrite(petrol)  #Ekrana çekilen veriyi yazar.
    return petrol 

#Web sitesinden Altını çeker ve dizi return eder.
def takeit4(altin):
    now1= datetime.datetime.now()
    altin[0]= datetime.datetime.strftime(now1, '%c')
    altin[1]= driver.find_element(By.CSS_SELECTOR,"tr:nth-child(2) > td:nth-child(2)").text
    altin[2]=driver.find_element(By.CSS_SELECTOR,"tr:nth-child(2) > td:nth-child(3)").text
    altin[3]= driver.find_element(By.CSS_SELECTOR,"tr:nth-child(2) > td:nth-child(4)").text   
    altin[4]=driver.find_element(By.CSS_SELECTOR,"tr:nth-child(2) > td:nth-child(5)").text
    
    
    screeWrite(altin)  #Ekrana çekilen veriyi yazar.
    return altin 

#---------------------Write to database with function-------------------------------

#Elde edilen veriyi dizi olarak alır ve sorgu ile veri tabanına yazar.
def insertVaribleIntoTable(data_tuple,dbName,sqlite_insert_with_param):
    try:
        
        con = sqlite3.connect(dbName)
        imlec = con.cursor()
        print("Connected to SQLite")
        imlec.execute(sqlite_insert_with_param, data_tuple)
        con.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")
        imlec.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if con:
            con.close()
            print("The SQLite connection is closed")

#---------------------Making necessary variable definitions-------------------------------

#For USD Cur.
dbName = "doviz.db"
usd_sqlite_insert_with_param = """INSERT INTO usd_try
                          (date, buy, sell, max, min, change) 
                          VALUES (?, ?, ?, ?, ?, ?);"""
#For EURO Cur.
euro_sqlite_insert_with_param = """INSERT INTO euro_try
                          (date, buy, sell, max, min, change) 
                          VALUES (?, ?, ?, ?, ?, ?);"""
#For Petrol Cur.
petrol_sqlite_insert_with_param = """INSERT INTO brent_petrol
                          (date, value, max, min, change) 
                          VALUES (?, ?, ?, ?, ?);"""
#For ALTIN Cur.                   
altin_sqlite_insert_with_param = """INSERT INTO altin
                          (date, value, max, min, change) 
                          VALUES (?, ?, ?, ?, ?);"""

usd =[0] * 6
euro =[0] * 6
petrol =[0] * 5
altin =[0] * 5
webLink1="https://kur.doviz.com/"
weblink2="https://www.doviz.com/emtialar"





#-------------------------------Main Process---------------------------------------------------------

driver = webdriver.Chrome('./chromedriver') 


driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[0])
driver.get(webLink1)
driver.switch_to.window(driver.window_handles[1])
driver.get(weblink2)

#-------------------------------While True-------------------------------------------------

while True: 
#-------------dövizler------------------

    
    driver.switch_to.window(driver.window_handles[0])
    usd = takeit1(usd)
    usd_data_tuple = (usd[0], usd[1], usd[2], usd[3], usd[4], usd[5])
    insertVaribleIntoTable(usd_data_tuple,dbName,usd_sqlite_insert_with_param)
    
    euro = takeit2(euro)
    euro_data_tuple = (euro[0], euro[1], euro[2], euro[3], euro[4], euro[5])
    insertVaribleIntoTable(euro_data_tuple,dbName,euro_sqlite_insert_with_param)

#-------------emitalar------------------
   
    
    driver.switch_to.window(driver.window_handles[1])
    petrol = takeit3(petrol)
    petrol_data_tuple = (petrol[0], petrol[1], petrol[2], petrol[3],petrol[4])
    insertVaribleIntoTable(petrol_data_tuple,dbName,petrol_sqlite_insert_with_param)

    altin = takeit4(altin)
    altin_data_tuple = (altin[0], altin[1], altin[2], altin[3], altin[4])
    insertVaribleIntoTable(altin_data_tuple,dbName,altin_sqlite_insert_with_param)
   
#-------------Delay------------------  
    time.sleep(10)