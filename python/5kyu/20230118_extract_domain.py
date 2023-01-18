# 5kyu Write a function that when given a URL as a string, 
# parses out just the domain name and returns it as a string. 
# For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                 -> domain name = cnet"

# My ideas:
#  Look for www. or //
#  Split on // then .com
# Then if www present, slice of www.

def domain_name(url):
    if "//" in url:
        parts = url.split("//")
        if "www." in parts[1]:
            smol = parts[1].split("www.")
            end = smol[1].split(".")
        else:
            end = parts[1].split(".")
    elif "www." in url:
            smol = url.split("www.")
            end = smol[1].split(".")
    else:
        end = url.split(".")
    return end[0]

print(domain_name("www.xakep.ru"))

# Refactored:
def domain_name(url):
    if "//" in url:
        parts = url.split("//")
        if "www." in parts[1]:
            end = parts[1].split("www.")[1].split(".")
        else:
            end = parts[1].split(".")
    elif "www." in url:
            end = url.split("www.")[1].split(".")
    else:
        end = url.split(".")
    return end[0]

# Best solution from Codewars
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

