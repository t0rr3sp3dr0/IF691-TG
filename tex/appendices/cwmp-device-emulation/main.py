import requests
import time
import xml.etree.ElementTree

def main():
    url = 'http://acs.telesp.net.br:7005/cwmpWeb/WGCPEMgt'

    s = requests.Session()
    s.auth = ('acsclient', 'telefonica')

    with open('inform.xml', 'rb') as f:
        s.post(url, data=f.read())
    
    time.sleep(1)

    r = s.post(url)
    print(r.text)
    
    with open('response.xml', 'rb') as f:
        s.post(url, data=f.read())
    
    with open('get.xml', 'rb') as f:
        s.post(url, data=f.read())
    
    with open('inform2.xml', 'rb') as f:
        s.post(url, data=f.read())
    
    time.sleep(1)

    r = s.post(url)
    print(r.text)
    
    with open('response.xml', 'rb') as f:
        s.post(url, data=f.read())

    spv = xml.etree.ElementTree.fromstring(r.content)
    for pvs in spv.findall("./{http://schemas.xmlsoap.org/soap/envelope/}Body/{urn:dslforum-org:cwmp-1-0}SetParameterValues/ParameterList/ParameterValueStruct"):
        if pvs.find('Name').text == 'InternetGatewayDevice.ManagementServer.URL':
            url = pvs.find('Value').text
        elif pvs.find('Name').text == 'InternetGatewayDevice.ManagementServer.Username':
            username = pvs.find('Value').text
        elif pvs.find('Name').text == 'InternetGatewayDevice.ManagementServer.Password':
            password = pvs.find('Value').text

    s = requests.Session()
    s.auth = (username, password)

    with open('inform3.xml', 'rb') as f:
        s.post(url, data=f.read())
    
    time.sleep(4)

    r = s.post(url)
    print(r.text)
    
    with open('response.xml', 'rb') as f:
        s.post(url, data=f.read())

if __name__ == '__main__':
    main()
