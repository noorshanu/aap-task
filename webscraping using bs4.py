import bs4
 from urllib.request import urlopen as ureq
 from bs4 import BeautifulSoup as soup
 my_url ='http://psleci.nic.in/'
 #opening up connection,grabbing,uclient
uClient=ureq(my_url)
page_html = uclient.read()
uclient.close()
page_soup =soup(page_html,"html.parser")
#grabing list of all states
 containers=page_soup.findAll("div",{"class":"style1"})
 

