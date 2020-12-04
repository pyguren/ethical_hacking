import nmap3

nm = nmap3.Nmap()
r = nm.scan_top_ports("192.168.1.1")
print(r)

#print("\nPuertos abiertos:")
#for d in r.get("192.168.1.115"):
#   if d["state"] == "open":
#       print(d["portid"] + "/"+ d["protocol"] + " ... open")

#print("\nSistema Operativo:")
#r = nm.nmap_os_detection("192.168.1.115")
#print(r)
#print(r[0]["name"])

#print("\nVersiones:")
#r = nm.nmap_version_detection("192.168.1.115")
#print(r)
#for d in r:
    #s = d["port"] + "/"+ d["protocol"] + " ... "
    #if "service" in d.keys():
    #    s = s + d["service"]["name"] + " ... " + d["service"]["product"] + " " + d["service"]["version"]
    #print(s)

#print("\nHost Discovery")
#nmhd = nmap3.NmapHostDiscovery()
#r = nmhd.nmap_no_portscan("", args="192.168.1.0/24")
#print(r)
#print("Activos: " + r["status"]["up"])
#for h in r["hosts"]:
#    print(h["addr"] + " ... " + h["state"])

#print("\nEspecificando argumentos")
#nmst = nmap3.NmapScanTechniques()
#r = nmst.nmap_tcp_scan("192.168.1.115", args="-p 21,22,80,443")
#print(r)
#for d in r.get("192.168.1.115"):
#    print(d["portid"] + "/" + d["protocol"] + " ... " + d["state"] + " ... " + d["service"]["name"])
