import os
import webbrowser
sites = ['instagram','facebook','wikipedia','google','flipkart','gmail','amazon']
apps = ['chrome','freetube','vs code','vlc','notion']
os.system(f"echo {"Hello World"}")
a = input("Give command : ")
if any(element in a for element in sites):
    link = "www.",a,".com"
    print(f"opening {a}.")
    webbrowser.open(link)
elif any(element in a for element in apps):
    os.system(f"cd {"D:\Phoenix\Projects\Python Projects\Sam\apps_shorcut"}")
    os.system("d:")
    os.system("Google Chrome.ink")
else:
    print("Not found.")
