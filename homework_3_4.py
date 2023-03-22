from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
from selenium.webdriver.common.by import By

class Test_Class:
    def case1(self):
        driver= webdriver.Chrome (ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
    
        login = driver.find_element(By.ID,"login-button")
        login.click()
        errorMessage =driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"SONUÇ : {testResult}")

        
    

    def case2(self):
        drive = webdriver.Chrome(ChromeDriverManager().install())
        drive.maximize_window()
        drive.get("https://www.saucedemo.com/")
        
        nicknameInput= drive.find_element(By.ID,"user-name")
        nicknameInput.send_keys("3")
        login =drive.find_element(By.ID,"login-button")
        login.click()

        errorMassege = drive.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMassege.text == "Epic sadface: Password is required"
        print(f"SONUÇ2 : {testResult}")  
    
    
             
    



    def case3(self):
        drive = webdriver.Chrome(ChromeDriverManager().install())
        drive.maximize_window()
        drive.get("https://www.saucedemo.com/")

        usernameInput = drive.find_element(By.ID,"user-name")
        passwordInput = drive.find_element(By.ID,"password")

        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")

        login =drive.find_element(By.CLASS_NAME,"login-button")
        login.click()

        errorMassege=drive.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/input")
        testResult = errorMassege == "Epic sadface: Sorry, this user has been locked out"
        print(f"SONUÇ3 : {testResult}")
    
    
    
                                

    def case4(self):
        draver = webdriver.Chrome(ChromeDriverManager().install())
        draver.maximize_window()
        draver.get("https://www.saucedemo.com/")
        sleep(1)

        login = draver.find_element(By.ID,"login-button")(By.)
        login.click()
        kirmiziX_iconu = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2) > svg")
        print(f"Kirmizi X ikonu görünürlüğü kontrolü = {kirmiziX_iconu.is_displayed()}") 
        error_mesaj_X=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        error_mesaj_X.click()
        try:
            print(f"Uyari mesajinin kapatma butonuna tiklandi , X ikonu görünürlüğü kontrolü = {kirmiziX_iconu.is_displayed()}  NOK")
        except:
            print(f"Uyari mesajinin kapatma butonuna tiklandi , X ikonu Bulunamadi - OK") 

                             
    def case5(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(5)
        login =driver.find_element(By.ID,"login-button")
        login.click()
        driver.get("/inventory.html")
        sleep(50)
    
    def case6(self):
        drive = webdriver.Chrome(ChromeDriverManager().install())
        drive.maximize_window()
        drive.get("https://www.saucedemo.com/")
       

        nameInput = drive.find_element(By.ID,"user-name")
        nameInput.send_keys("standard_user")
        password = drive.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        login =drive.find_element(By.ID,"login-button")
        login.click()
        sleep(2)

        listOfCourses = drive.find_element(By.CLASS_NAME,"inventory_item")
        print(f"Sayfadaki ürün sayisi {len(listOfCourses)} adet")

         
                                      



testClass =Test_Class()
testClass.case1()
testClass.case2()
testClass.case3()
testClass.case4()
testClass.case5()
testClass.case6()

while True:
    continue    

