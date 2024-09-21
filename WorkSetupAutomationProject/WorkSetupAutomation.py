import webbrowser as wb
import os

def workAuto():
    
    codepath = "C:\Program Files\Sublime Text 3\sublime_text.exe"
    os.startfile(codepath)
    Chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    URLS = (
        "google.com",
        "youtube.com",
        "x.com",
        "github.com"
    )
    
    for url in URLS:
        #url = input("Enter the name of the webite:-")
        wb.get(Chrome_path).open(url)
        
workAuto()        