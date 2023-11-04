import dns.resolver as dns
 
res = dns.Resolver()

resultado = res.resolve("vitima")
for info in resultado:
    print(info)