import requests
import uuid


def appconfig():
    # appConfig
    # POST https://mcare.siriusxm.ca/authService/100000002/appconfig

    try:
        response = requests.post(
            url="https://mcare.siriusxm.ca/authService/100000002/appconfig",
            headers={
                "X-Kony-Integrity":
                "GWSUSEVMJK;FEC9AA232EC59BE8A39F0FAE1B71300216E906B85F40CA2B1C5C7A59F85B17A4",
                "X-HTTP-Method-Override": "GET",
                "X-Kony-App-Key": "85ee60a3c8f011baaeba01ff3a5ae2c9",
                "Accept": "*/*",
                "X-Kony-App-Secret": "e3048b73f2f7a6c069f7d8abf5864115",
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        #print('Response HTTP Response Body: {content}'.format(
        #    content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def login():
    # login
    # POST https://mcare.siriusxm.ca/authService/100000002/login

    try:
        response = requests.post(
            url="https://mcare.siriusxm.ca/authService/100000002/login",
            headers={
                "X-Kony-Platform-Type": "ios",
                "Accept": "application/json",
                "X-Kony-App-Secret": "e3048b73f2f7a6c069f7d8abf5864115",
                "Accept-Language": "en-us",
                "X-Kony-SDK-Type": "js",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-SDK-Version": "8.4.134",
                "X-Kony-App-Key": "85ee60a3c8f011baaeba01ff3a5ae2c9",
            },
        )
        return response.json().get('claims_token').get('value')
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        #print('Response HTTP Response Body: {content}'.format(
        #    content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def versionControl():
    # VersionControl
    # POST https://mcare.siriusxm.ca/services/DealerAppService7/VersionControl

    try:
        response = requests.post(
            url=
            "https://mcare.siriusxm.ca/services/DealerAppService7/VersionControl",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
            data={
                "deviceCategory": "iPhone",
                "appver": "2.7.0",
                "deviceLocale": "en_US",
                "deviceModel": "iPhone%206%20Plus",
                "deviceVersion": "12.5.7",
                "deviceType": "",
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        #print('Response HTTP Response Body: {content}'.format(
        #    content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def getProperties():
    # getProperties
    # POST https://mcare.siriusxm.ca/services/DealerAppService7/getProperties

    try:
        response = requests.post(
            url=
            "https://mcare.siriusxm.ca/services/DealerAppService7/getProperties",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        #print('Response HTTP Response Body: {content}'.format(
        #    content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def update_1():
    # 1-updateDeviceSATRefreshWithPriority
    # POST https://mcare.siriusxm.ca/services/USUpdateDeviceSATRefresh/updateDeviceSATRefreshWithPriority

    try:
        response = requests.post(
            url=
            "https://mcare.siriusxm.ca/services/USUpdateDeviceSATRefresh/updateDeviceSATRefreshWithPriority",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
            data={
                "deviceId": radio_id_input,
                "appVersion": "2.7.0",
                "lng": "-86.210313195",
                "deviceID": uuid4,
                "provisionPriority": "2",
                "provisionType": "activate",
                "lat": "32.37436705",
            },
        )
        return response.json().get('seqValue')
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def getCRM():
    # GetCRMAccountPlanInformation
    # POST https://mcare.siriusxm.ca/services/DemoConsumptionRules/GetCRMAccountPlanInformation

    try:
        response = requests.post(
            url=
            "https://mcare.siriusxm.ca/services/DemoConsumptionRules/GetCRMAccountPlanInformation",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
            data={
                "seqVal": seq,
                "deviceId": radio_id_input,
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def dbUpdate():
    # DBUpdateForGoogle
    # POST https://mcare.siriusxm.ca/services/DBSuccessUpdate/DBUpdateForGoogle

    try:
        response = requests.post(
            url=
            "https://mcare.siriusxm.ca/services/DBSuccessUpdate/DBUpdateForGoogle",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
            data={
                "OM_ELIGIBILITY_STATUS": "Eligible",
                "appVersion": "2.7.0",
                "flag": "failure",
                "Radio_ID": radio_id_input,
                "deviceID": uuid4,
                "G_PLACES_REQUEST": "",
                "OS_Version": "iPhone 12.5.7",
                "G_PLACES_RESPONSE": "",
                "Confirmation_Status": "SUCCESS",
                "seqVal": seq,
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def blocklist():
    # BlockListDevice
    # POST https://mcare.siriusxm.ca/services/USBlockListDevice/BlockListDevice

    try:
        response = requests.post(
            url=
            "https://mcare.siriusxm.ca/services/USBlockListDevice/BlockListDevice",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
            data={
                "deviceId": uuid4,
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def oracle():
    # Request (9)
    # POST https://oemremarketing.custhelp.com/cgi-bin/oemremarketing.cfg/php/custom/src/oracle/program_status.php

    try:
        response = requests.post(
            url=
            "https://oemremarketing.custhelp.com/cgi-bin/oemremarketing.cfg/php/custom/src/oracle/program_status.php",
            params={
                "google_addr": "395 EASTERN BLVD, MONTGOMERY, AL 36117, USA",
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "*/*",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def createAccount():
    # CreateAccount
    # POST https://mcare.siriusxm.ca/services/DealerAppService3/CreateAccount

    try:
        response = requests.post(
            url=
            "https://mcare.siriusxm.ca/services/DealerAppService3/CreateAccount",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SXM Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
            data={
                "seqVal": seq,
                "deviceId": radio_id_input,
                "oracleCXFailed": "1",
                "appVersion": "2.7.0",
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def update_2():
    # 2-updateDeviceSATRefreshWithPriority
    # POST https://mcare.siriusxm.ca/services/USUpdateDeviceRefreshForCC/updateDeviceSATRefreshWithPriority

    try:
        response = requests.post(
            url=
            "https://mcare.siriusxm.ca/services/USUpdateDeviceRefreshForCC/updateDeviceSATRefreshWithPriority",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
            data={
                "deviceId": radio_id_input,
                "provisionPriority": "2",
                "appVersion": "2.7.0",
                "device_Type": "iPhone iPhone 6 Plus",
                "deviceID": uuid4,
                "os_Version": "iPhone 12.5.7",
                "provisionType": "activate",
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


requests = requests.Session()
radio_id_input = input("Enter Radio ID: ")
radio_id_input = radio_id_input.upper()
uuid4 = str(uuid.uuid4())
auth_token = ""
seq = ""
print("appconfig")
appconfig()
print("login")
auth_token = login()
print("versionControl")
versionControl()
print("getProperties")
getProperties()
print("update_1")
seq = update_1()
print("getCRM")
getCRM()
print("dbUpdate")
dbUpdate()
print("blocklist")
blocklist()
# I don't really think the oracle call is neccessary
print("oracle")
oracle()
print("createAccount")
createAccount()
print("update_2")
update_2()
