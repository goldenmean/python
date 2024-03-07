#requisites: ip2geotools , geopy
#C:\Python\Python39\Scripts>pip3.9.exe install ip2geotools
#C:\Python\Python39\Scripts>pip3.9.exe install geopy

import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance

def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")
	
#Getting location from a given IP Address
ip_add = input("Enter IP: ")  # 198.35.26.96
printDetails(ip_add)

#Getting location from a given URL
url = input("Enter URL: ")  # www.youtube.com
ip_add = socket.gethostbyname(url)
printDetails(ip_add)

"""
def is_country_blocked(ip_address):
    blocked_countries = ["China", "Canada", "India"]
    location = DbIpCity.get(ip_address)
    if location.country in blocked_countries:
        return True
    else:
        return False


ip_add = input("Enter IP: ")  # 198.35.26.96
if is_country_blocked(ip_add) is True:
    print(f"IP Address: {ip_add} is blocked")
else:
    print(f"IP Address: {ip_add} is allowed")
	
def calculate_distance(ip1, ip2):
    res1 = DbIpCity.get(ip1)
    res2 = DbIpCity.get(ip2)
    lat1, lon1 = res1.latitude, res1.longitude
    lat2, lon2 = res2.latitude, res2.longitude
    return distance((lat1, lon1), (lat2, lon2)).km


# Input two IP addresses
ip_add_1 = input("1st IP: ")  # 198.35.26.96
ip_add_2 = input("2nd IP: ")  # 220.158.144.59
dist = calculate_distance(ip_add_1, ip_add_2)
print(f"Distance between them is {str(dist)}km")

def get_distance_from_location(ip, lat, lon):
    res = DbIpCity.get(ip)
    ip_lat, ip_lon = res.latitude, res.longitude
    return distance((ip_lat, ip_lon), (lat, lon)).km

server_ip = input("Server's IP: ")
lat = float(input("Your Latitude: "))
lng = float(input("Your Longitude: "))

dist = get_distance_from_location(server_ip, lat, lng)
print(f"Distance between the server and your location is {str(dist)}km")

"""