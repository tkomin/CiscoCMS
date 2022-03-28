import requests

#Cisco Meeting Server API

#get status CMS
r1 = requests.get('https://cms:8443/api/v1/system/status', auth=('userapi', 'password'),
                 verify=False)

print(r1.text)


#get informations of conference (for example call_id ...)
r2 = requests.get('https://cms:8443/api/v1/calls', auth=('userapi', 'password'),
                 verify=False)

print(r2.text)

#get coSpaces
r3 = requests.get('https://cms:8443/api/v1/coSpaces', auth=('userapi', 'password'),
                 verify=False)
print(r3.text)

#add participant to conference
r4 = requests.post('https://cms:8443/api/v1/calls/call_id/'
               'participants',auth=('userapi', 'password'),
                   data = {'remoteParty': 'participants_number'},verify=False )

print(r4.text)
