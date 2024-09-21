import pyshorteners

url = input("Please enter an Url: ")

print("URL after shortening:- ",pyshorteners.Shortener().tinyurl.short(url))