def defang_ip_address(ip_address):
    return ip_address.replace('.', '[.]')
ip_address = input("enter your ip address")
print("Original IP address :",ip_address)
defanged_ip_address = defang_ip_address(ip_address)
print(defanged_ip_address)  
