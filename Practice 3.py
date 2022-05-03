[]###############    "Проверка 3 товара в корзине"   ######################
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://saucedemo.com/")
# login = driver.find_element_by_id("user-name")
# login.send_keys("performance_glitch_user")
# password = driver.find_element_by_id("password")
# password.send_keys("secret_sauce")
# login_btn = driver.find_element_by_id("login-button")
# login_btn.click()
# time.sleep(3)
# Backpack=driver.find_element_by_id("add-to-cart-sauce-labs-backpack")
# Backpack.click()
# time.sleep(1)
# BikeLight=driver.find_element_by_id("add-to-cart-sauce-labs-bike-light")
# BikeLight.click()
# time.sleep(1)
# TShirt=driver.find_element_by_id("add-to-cart-sauce-labs-bolt-t-shirt")
# TShirt.click()
# time.sleep(1)
# shoppingcart=driver.find_element_by_class_name("shopping_cart_link")
# shoppingcart.click()
# items_count = driver.find_elements_by_class_name("cart_item_label")
# if len(items_count) == 3:
#     print("В корзине 3 товара")
# else:
#     print("Ошибка. Количество товаров в корзине: " + str(len(items_count)))
# driver.quit()
[]###################### Модальные окна ####################################
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("http://demo.automationtesting.in/Alerts.html")
# button=driver.find_element_by_class_name("btn-danger")
# button.click()
# time.sleep(1)
# alert_script = driver.execute_script
# alert = driver.switch_to.alert
# alert_text = alert.text
# print(alert_text)
# if (alert_text) =="I am an alert box!":
#      print("Содержимое равно тексту I am an alert box!")
# else:
#      print("Ошибка. Тексты не совпадают")
# alert.accept()
# time.sleep(3)
# current_page = driver.current_url
# print(current_page)
# driver.execute_script("window.open();")
# window_after = driver.window_handles[1]
# driver.switch_to.window(window_after)
# driver.get(current_page)
# time.sleep(3)
# driver.find_element_by_partial_link_text("Alert with OK & Cancel").click()
# driver.find_element_by_class_name("btn-primary").click()
# confirm = driver.switch_to.alert
# confirm.dismiss()
# time.sleep(3)
# driver.execute_script("window.open();")
# window_after = driver.window_handles[2]
# driver.switch_to.window(window_after)
# driver.get(current_page)
# time.sleep(3)
# driver.find_element_by_partial_link_text("Alert with Textbox").click()
# driver.find_element_by_class_name("btn-info").click()
# prompt = driver.switch_to.alert
# prompt.send_keys("Ура! Задание выполнено!")
# prompt.accept()
# time.sleep(5)
# driver.quit()
[] ############## Регистрация пользователя #####################
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://opensource-demo.orangehrmlive.com/")
# login = driver.find_element_by_id("txtUsername")
# login.send_keys("Admin")
# password = driver.find_element_by_id("txtPassword")
# password.send_keys("admin123")
# login_btn = driver.find_element_by_id("btnLogin")
# login_btn.click()
# pim = driver.find_element_by_id("menu_pim_viewPimModule")
# pim.click()
# time.sleep(3)
# AddEmployee = driver.find_element_by_id("menu_pim_addEmployee")
# AddEmployee.click()
# firstname = driver.find_element_by_id("firstName")
# firstname.send_keys("Igor")
# lastName = driver.find_element_by_id("lastName")
# lastName.send_keys("Timofeev")
# Save = driver.find_element_by_id("btnSave")
# Save.click()
# driver.quit()  

[] ############### Удаление пользователя #######################
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://opensource-demo.orangehrmlive.com/")
# login = driver.find_element_by_id("txtUsername")
# login.send_keys("Admin")
# password = driver.find_element_by_id("txtPassword")
# password.send_keys("admin123")
# login_btn = driver.find_element_by_id("btnLogin")
# login_btn.click()
# pim = driver.find_element_by_id("menu_pim_viewPimModule")
# pim.click()
# time.sleep(3)
# EmployeeList = driver.find_element_by_id("menu_pim_viewEmployeeList")
# EmployeeList.click()
# time.sleep(3)
# EmployeeName = driver.find_element_by_name("empsearch[employee_name][empName]")
# EmployeeName.send_keys("Igor Timofeev")
# search = driver.find_element_by_id("searchBtn")
# search.click()
# time.sleep(3)
# checkbox = driver.find_element_by_name("chkSelectRow[]")
# checkbox.click()
# Delete= driver.find_element_by_class_name("delete")
# Delete.click()
# dialogDelete=driver.find_element_by_id("dialogDeleteBtn")
# dialogDelete.click()
# driver.quit()

[]#######################  Linda Jein  ###################################
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# login = driver.find_element_by_id("txtUsername")
# login.send_keys("Admin")
# password = driver.find_element_by_id("txtPassword")
# password.send_keys("admin123")
# login_btn = driver.find_element_by_id("btnLogin")
# login_btn.click()
# pim = driver.find_element_by_id("menu_pim_viewPimModule")
# pim.click()
# time.sleep(3)
# Employee_List = driver.find_element_by_id("menu_pim_viewEmployeeList")
# Employee_List.click()
# time.sleep(3)
# Linda = driver.find_element_by_link_text("0016")
# Linda.click()
# personal_optGender_1= driver.find_element_by_id("personal_optGender_1")
# personal_optGender_1_disabled = personal_optGender_1.get_attribute("disabled")
# print("value of personal_optGender_1 radio: ", personal_optGender_1_disabled)
# if personal_optGender_1_disabled is None:
#     print("Кнопка доступна")
# else:
#     print("Кнопка НЕ доступна")
# time.sleep(3)
# select= driver.find_element_by_id("personal_cmbNation")
# select_disabled = select.get_attribute("disabled")
# print("value of select: ", select_disabled)
# if select_disabled is None:
#     print("Селектор доступен")
# else:
#     print("Селектор НЕ доступен")
# btnSave=driver.find_element_by_id("btnSave")
# btnSave.click()
# Male=driver.find_element_by_id("personal_optGender_1")
# Male.click()
# Male = driver.find_element_by_id("personal_optGender_1")
# Male_checked =Male.get_attribute("checked")
# print("Male_checked radio: ", Male_checked)
# if Male_checked is None:
#     print("Атрибута нет")
# else:
#     print("Атрибут есть")
# time.sleep(3)
# from selenium.webdriver.support.select import Select
# element = driver.find_element_by_id("personal_cmbNation")
# select=Select(element)
# select.select_by_value("193")
# time.sleep(3)
# Zimbabwean= driver.find_element_by_id("personal_cmbNation")
# Zimbabwean_selected = Zimbabwean.get_attribute("selected")
# print("Zimbabwean_selected")
# if Zimbabwean is None:
#     print("Атрибута нет")
# else:
#     print("Атрибут есть")
# time.sleep(3)
# driver.find_element_by_id("personal_optGender_2").click()
# driver.find_element_by_id("personal_cmbNation").click()
# driver.find_element_by_css_selector("#personal_cmbNation>option:nth-child(1)").click()
# driver.find_element_by_id("personal_cmbNation").click()
# driver.find_element_by_css_selector("input#btnSave").click()
# driver.quit()

[] ######################### Регистрация ##################################
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("http://demo.automationtesting.in/Register.html")
# time.sleep(1)
# FirstName= driver.find_element_by_css_selector("[ng-model=FirstName]")
# FirstName.send_keys("Samuil")
# LastName=driver.find_element_by_css_selector("[ng-model=LastName]")
# LastName.send_keys("Ivanov")
# EmailAdress=driver.find_element_by_css_selector("[ng-model=EmailAdress]")
# EmailAdress.send_keys("SamIvan@mail.ru")
# Phone=driver.find_element_by_css_selector("[ng-model=Phone]")
# Phone.send_keys("1233214567")
# Male=driver.find_element_by_css_selector("input[value=Male]")
# Male.click()
# time.sleep(1)
# from selenium.webdriver.support.select import Select
# element = driver.find_element_by_id("country")
# select = Select(element)
# select.select_by_value("United States of America")
# time.sleep(1)
# from selenium.webdriver.support.select import Select
# element = driver.find_element_by_id("yearbox")
# select = Select(element)
# select.select_by_value("2000")
# time.sleep(1)
# from selenium.webdriver.support.select import Select
# element = driver.find_element_by_css_selector("[ng-model=monthbox]")
# select = Select(element)
# select.select_by_value("August")
# time.sleep(1)
# from selenium.webdriver.support.select import Select
# element = driver.find_element_by_id("daybox")
# select = Select(element)
# select.select_by_value("25")
# password= driver.find_element_by_id("firstpassword")
# password.send_keys("Samuil21")
# secondpassword= driver.find_element_by_id("secondpassword")
# secondpassword.send_keys("Samuil21")
# time.sleep(1)
# file=("C:/Users/Public/Pictures/images.jpg")
# upload = driver.find_element_by_id("imagesrc")
# upload.send_keys(file)
# time.sleep(1)
# driver.execute_script("window.scrollBy(0, 300);")
# submit=driver.find_element_by_id("submitbtn")
# submit.click()

[]########################## Урок 3 практическое 1 ##############################
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# wait=WebDriverWait(driver, 15)
# driver.get("http://demo.automationtesting.in/WebTable.html")
# More=driver.find_element_by_link_text("More").click()
# Loader=driver.find_element_by_link_text("Loader").click()
# Run= wait.until(EC.text_to_be_present_in_element((By.ID, "loader"), "Run"))
# Run1=driver.find_element_by_css_selector("#loader.btn").click()
# Lorem = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "modal-body"), "Lorem"))
# save_changes = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer :nth-child(2)")))
# save_changes.click()

[] ######################### Урок 3 практическое 2 ##############################
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://demo.automationtesting.in/WebTable.html")
# More=driver.find_element_by_link_text("More").click()
# Dynamic_Data=driver.find_element_by_link_text("Dynamic Data").click()
# modal_window = driver.find_element_by_class_name("cont_box_center")
# modal_window_text = modal_window.text
# assert "Loading the data Dynamically" in  modal_window_text
# Get_Dynamic_Data=driver.find_element_by_id("save").click()

[]########################## Урок 3 практическое 3 ##############################
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://demo.automationtesting.in/WebTable.html")
# More=driver.find_element_by_link_text("More").click()
# File_Upload=driver.find_element_by_link_text("File Upload").click()
# file=("C:/Users/Public/Pictures/images.jpg")
# upload = driver.find_element_by_id("input-4")
# upload.send_keys(file)
# time.sleep(3)
# Remove=driver.find_element_by_class_name("glyphicon-trash").click()
# file=("C:/Users/Public/Pictures/Пустой.txt")
# upload = driver.find_element_by_id("input-4")
# upload.send_keys(file)
# close=driver.find_element_by_class_name("kv-error-close").click()
# time.sleep(1)
# upload_button= driver.find_element_by_css_selector(".btn.btn-default.fileinput-upload.fileinput-upload-button")
# upload_button_disabled = upload_button .get_attribute("disabled")
# if upload_button_disabled is None:
#     print("Кнопка доступна")
# else:
#     print("Кнопка НЕ доступна")
# driver.quit()

[]########################## Урок 3 практическое 4 ##############################
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait=WebDriverWait(driver, 10)
# driver.get("http://demo.automationtesting.in/WebTable.html")
# More=driver.find_element_by_link_text("More").click()
# JQuery=driver.find_element_by_link_text("JQuery ProgressBar").click()
# Close_btn = wait.until
# (EC.invisibility_of_element_located ((By.CSS_SELECTOR, ".ui-dialog-buttonset>[type=button]")) )
# downloadButton=driver.find_element_by_id("downloadButton").click()
# Cancel=wait.until
# (EC.text_to_be_present_in_element_value((By.CLASS_NAME,"ui-dialog-buttonpane"), "Cancel Download"))
# Cancel_Download=driver.find_element_by_css_selector(".ui-dialog-buttonset>[type=button]").click()
# downloadButton2=driver.find_element_by_id("downloadButton").click()
# Complete=wait.until
# (EC.text_to_be_present_in_element_value((By.CLASS_NAME,"progress-label"), "Complete!"))

[]##########################  Урок 3 практическое 5 #############################
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# weit = WebDriverWait(driver, 10)
# driver.get("http://demo.automationtesting.in/WebTable.html")
# SwitchTo=driver.find_element_by_css_selector(":nth-child(4)>[data-toggle=dropdown]").click()
# Windows=driver.find_element_by_link_text("Windows").click()
# current_window = driver.current_window_handle
# Click=driver.find_element_by_css_selector("[target=_blank]> .btn.btn-info").click()
# window_after = driver.window_handles[1]
# driver.switch_to.window(window_after)
# time.sleep(3)
# driver.close()
# driver.switch_to.window(current_window)
# Multiple=driver.find_element_by_link_text("Open Seperate Multiple Windows").click()
# Click1=driver.find_element_by_css_selector("#Multiple>.btn.btn-info").click()
# window_do = driver.window_handles[2]
# driver.switch_to.window(window_do)
# Web= weit.until(EC.url_to_be("http://demo.automationtesting.in/Index.html"))
# print(Web)
# Vkladki=weit.until(EC.number_of_windows_to_be(3))
# print(Vkladki)
# email= driver.find_element_by_id("email")
# email.send_keys("sam@mail.ru")
# enter= driver.find_element_by_id("enterimg").click()
# Web1= weit.until(EC.url_to_be("http://demo.automationtesting.in/Register.html"))
# print(Web1)
# driver.quit()

