from selenium import webdriver
from selenium.webdriver.support.ui import Select
import json

driver=webdriver.Chrome(executable_path="G:\progs\chromedriver.exe")
driver.get("http://psleci.nic.in/")

State1=Select(driver.find_element_by_id("ddlState"))
print(len(State1.options))
state=State1.options
for i in State1.options:
print(i.text)
13 ={}
for i in range(1,len(State1.options)):
district = []
12 ={}
State1=Select(driver.find_element_by_id("ddlState"))
for a in District1.options:
 district.append(a.text)
    district=district[1:]
    for j in range(1,len(District1.options)):
        l1={}
        District1=Select(driver.find_element_by_id("ddlDistrict"))
        District1.options[j].click()
        ac1=Select(driver.find_element_by_id("ddlAC"))
        ac=[]
        for a in z.options:
            ac.append(a.text)
        ac=ac[1:]
        for k in range(1,len(ac1.options)):
            ac1=Select(driver.find_element_by_id("ddlAC"))
            ac1.options[k].click()
            l=Select(driver.find_element_by_id("ddlPS"))
            pollst=[]
            for a in l.options:
                pollst.append(a.text)
            pollst=pollst[1:]
            try:
                l1[ac[k]]=pollst
            except:
                print("AC Error")
        try:
            l2[district[j]]=l1
        except:
            print("District Error")
    try:
        l3[state[i].text]=l2
    except:
        print("State Error")    
