import requests
import uuid
import json
import urllib.parse
import sys

def login():
    # login
    # POST https://dealerapp.siriusxm.com/authService/100000002/login

    try:
        params = {"os":deviceiOSVersion,"dm":deviceModel,"did":uuid4,"ua":"iPhone","aid":"DealerApp","aname":"SiriusXM Dealer","chnl":"mobile","plat":"ios","aver":appVer,"atype":"native","stype":"b2c","kuid":"","mfaid":"df7be3dc-e278-436c-b2f8-4cfde321df0a","mfbaseid":"efb9acb6-daea-4f2f-aeb3-b17832bdd47b","mfaname":"DealerApp","sdkversion":"9.5.36","sdktype":"js","sessiontype":"I","clientUUID":"1742536405634-41a8-0de0-125c","rsid":"1742536405654-b954-784f-38d2","svcid":"login_$anonymousProvider"}
        paramsStr = json.dumps(params, separators=(',', ':'))
        response = session.post(
            url="https://dealerapp.siriusxm.com/authService/100000002/login",
            headers={
                "X-Voltmx-Platform-Type": "ios",
                "Accept": "application/json",
                "X-Voltmx-App-Secret": "c086fca8646a72cf391f8ae9f15e5331",
                "Accept-Language": "en-us",
                "X-Voltmx-SDK-Type": "js",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": userAgent,
                "X-Voltmx-SDK-Version": "9.5.36",
                "X-Voltmx-App-Key": "67cfe0220c41a54cb4e768723ad56b41",
                "X-Voltmx-ReportingParams": urllib.parse.quote(paramsStr, safe='$:,'),
            },
        )
        return response.json().get('claims_token').get('value')
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        #print('Response HTTP Response Body: {content}'.format(
        #    content=response.content))
    except Exception:
        print('HTTP Request failed')


def versionControl():
    # VersionControl
    # POST https://dealerapp.siriusxm.com/services/DealerAppService7/VersionControl

    try:
        params = {"os":deviceiOSVersion,"dm":deviceModel,"did":uuid4,"ua":"iPhone","aid":"DealerApp","aname":"SiriusXM Dealer","chnl":"mobile","plat":"ios","aver":appVer,"atype":"native","stype":"b2c","kuid":"","mfaid":"df7be3dc-e278-436c-b2f8-4cfde321df0a","mfbaseid":"efb9acb6-daea-4f2f-aeb3-b17832bdd47b","mfaname":"DealerApp","sdkversion":"9.5.36","sdktype":"js","fid":"frmHome","sessiontype":"I","clientUUID":"1742536405634-41a8-0de0-125c","rsid":"1742536405654-b954-784f-38d2","svcid":"VersionControl"}
        paramsStr = json.dumps(params, separators=(',', ':'))
        response = session.post(
            url=
            "https://dealerapp.siriusxm.com/services/DealerAppService7/VersionControl",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": userAgent,
                "X-Voltmx-Authorization": auth_token,
                "X-Voltmx-ReportingParams": urllib.parse.quote(paramsStr, safe='$:,'),
            },
            data={
                "deviceCategory": "iPhone",
                "appver": appVer,
                "deviceLocale": "en_US",
                "deviceModel": deviceModel,
                "deviceVersion": deviceiOSVersion,
                "deviceType": "",
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        #print('Response HTTP Response Body: {content}'.format(
        #    content=response.content))
    except Exception:
        print('HTTP Request failed')


def getProperties():
    # getProperties
    # POST https://dealerapp.siriusxm.com/services/DealerAppService7/getProperties

    try:
        params = {"os":deviceiOSVersion,"dm":deviceModel,"did":uuid4,"ua":"iPhone","aid":"DealerApp","aname":"SiriusXM Dealer","chnl":"mobile","plat":"ios","aver":appVer,"atype":"native","stype":"b2c","kuid":"","mfaid":"df7be3dc-e278-436c-b2f8-4cfde321df0a","mfbaseid":"efb9acb6-daea-4f2f-aeb3-b17832bdd47b","mfaname":"DealerApp","sdkversion":"9.5.36","sdktype":"js","fid":"frmHome","sessiontype":"I","clientUUID":"1742536405634-41a8-0de0-125c","rsid":"1742536405654-b954-784f-38d2","svcid":"getProperties"}
        paramsStr = json.dumps(params, separators=(',', ':'))
        response = session.post(
            url=
            "https://dealerapp.siriusxm.com/services/DealerAppService7/getProperties",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": userAgent,
                "X-Voltmx-Authorization": auth_token,
                "X-Voltmx-ReportingParams": urllib.parse.quote(paramsStr, safe='$:,'),
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        #print('Response HTTP Response Body: {content}'.format(
        #    content=response.content))
    except Exception:
        print('HTTP Request failed')


def update_1():
    # 1-updateDeviceSATRefreshWithPriority
    # POST https://dealerapp.siriusxm.com/services/USUpdateDeviceSATRefresh/updateDeviceSATRefreshWithPriority

    try:
        params = {"os":deviceiOSVersion,"dm":deviceModel,"did":uuid4,"ua":"iPhone","aid":"DealerApp","aname":"SiriusXM Dealer","chnl":"mobile","plat":"ios","aver":appVer,"atype":"native","stype":"b2c","kuid":"","mfaid":"df7be3dc-e278-436c-b2f8-4cfde321df0a","mfbaseid":"efb9acb6-daea-4f2f-aeb3-b17832bdd47b","mfaname":"DealerApp","sdkversion":"9.5.36","sdktype":"js","fid":"frmRadioRefresh","sessiontype":"I","clientUUID":"1742536405634-41a8-0de0-125c","rsid":"1742536405654-b954-784f-38d2","svcid":"updateDeviceSATRefreshWithPriority"}
        paramsStr = json.dumps(params, separators=(',', ':'))
        response = session.post(
            url=
            "https://dealerapp.siriusxm.com/services/USUpdateDeviceSATRefresh/updateDeviceSATRefreshWithPriority",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": userAgent,
                "X-Voltmx-Authorization": auth_token,
                "X-Voltmx-ReportingParams": urllib.parse.quote(paramsStr, safe='$:,'),
            },
            data={
                "deviceId": radio_id_input,
                "appVersion": appVer,
                # "lng": "-86.210313195",
                "deviceID": uuid4,
                "provisionPriority": "2",
                "provisionType": "activate",
                # "lat": "32.37436705",
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        return response.json().get('seqValue')
    except Exception:
        print('HTTP Request failed')

def update_1_vin():
    # 1-updateDeviceSATRefreshWithPriority
    # POST https://dealerapp.siriusxm.com/services/USUpdateDeviceSATRefresh/updateDeviceSATRefreshWithPriority

    try:
        params = {"os":deviceiOSVersion,"dm":deviceModel,"did":uuid4,"ua":"iPhone","aid":"DealerApp","aname":"SiriusXM Dealer","chnl":"mobile","plat":"ios","aver":appVer,"atype":"native","stype":"b2c","kuid":"","mfaid":"df7be3dc-e278-436c-b2f8-4cfde321df0a","mfbaseid":"efb9acb6-daea-4f2f-aeb3-b17832bdd47b","mfaname":"DealerApp","sdkversion":"9.5.36","sdktype":"js","fid":"frmRadioRefresh","sessiontype":"I","clientUUID":"1742536405634-41a8-0de0-125c","rsid":"1742536405654-b954-784f-38d2","svcid":"updateDeviceSATRefreshWithPriority"}
        paramsStr = json.dumps(params, separators=(',', ':'))
        response = session.post(
            url=
            "https://dealerapp.siriusxm.com/services/USUpdateDeviceSATRefresh/updateDeviceSATRefreshWithPriority",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": userAgent,
                "X-Voltmx-Authorization": auth_token,
                "X-Voltmx-ReportingParams": urllib.parse.quote(paramsStr, safe='$:,'),
            },
            data={
                "deviceId": "",
                "appVersion": appVer,
                # "lng": "-86.210313195",
                "deviceID": uuid4,
                "provisionPriority": "2",
                "provisionType": "activate",
                # "lat": "32.37436705",
                "vin": radio_id_input,
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        return response.json().get('seqValue')
    except Exception:
        print('HTTP Request failed')


def USDealerVehicleData():
    # USDealerVehicleData
    # POST https://dealerapp.siriusxm.com/services/VehicleDataRestService/USDealerVehicleData
    
    try:
        params = {"os":deviceiOSVersion,"dm":deviceModel,"did":uuid4,"ua":"iPhone","aid":"DealerApp","aname":"SiriusXM Dealer","chnl":"mobile","plat":"ios","aver":appVer,"atype":"native","stype":"b2c","kuid":"","mfaid":"df7be3dc-e278-436c-b2f8-4cfde321df0a","mfbaseid":"efb9acb6-daea-4f2f-aeb3-b17832bdd47b","mfaname":"DealerApp","sdkversion":"9.5.36","sdktype":"js","fid":"frmRadioRefresh","sessiontype":"I","clientUUID":"1753153898694-ee1d-fe60-6c20","rsid":"1753153898749-a0f9-fa31-090b","svcid":"USDealerVehicleData"}
        paramsStr = json.dumps(params, separators=(',', ':'))
        response = session.post(
            url=
            "https://dealerapp.siriusxm.com/services/VehicleDataRestService/USDealerVehicleData",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": userAgent,
                "X-Voltmx-Authorization": auth_token,
                "X-Voltmx-ReportingParams": urllib.parse.quote(paramsStr, safe='$:,'),
            },
            data={
                "vin": radio_id_input,
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        if response.json().get('errorMessage') != "":
            print("Error: " + response.json().get('errorMessage'))
            print("You will need to manually enter the Radio ID, not the VIN, sorry :(")
            return None
        else:
            return response.json().get('radioID')
    except Exception:
        print('HTTP Request failed')
        return None

def getCRM():
    # GetCRMAccountPlanInformation
    # POST https://dealerapp.siriusxm.com/services/DemoConsumptionRules/GetCRMAccountPlanInformation

    try:
        params = {"os":deviceiOSVersion,"dm":deviceModel,"did":uuid4,"ua":"iPhone","aid":"DealerApp","aname":"SiriusXM Dealer","chnl":"mobile","plat":"ios","aver":appVer,"atype":"native","stype":"b2c","kuid":"","mfaid":"df7be3dc-e278-436c-b2f8-4cfde321df0a","mfbaseid":"efb9acb6-daea-4f2f-aeb3-b17832bdd47b","mfaname":"DealerApp","sdkversion":"9.5.36","sdktype":"js","fid":"frmRadioRefresh","sessiontype":"I","clientUUID":"1742536405634-41a8-0de0-125c","rsid":"1742536405654-b954-784f-38d2","svcid":"GetCRMAccountPlanInformation"}
        paramsStr = json.dumps(params, separators=(',', ':'))
        response = session.post(
            url=
            "https://dealerapp.siriusxm.com/services/DemoConsumptionRules/GetCRMAccountPlanInformation",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": userAgent,
                "X-Voltmx-Authorization": auth_token,
                "X-Voltmx-ReportingParams": urllib.parse.quote(paramsStr, safe='$:,'),
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
    except Exception:
        print('HTTP Request failed')


def dbUpdate():
    # DBUpdateForGoogle
    # POST https://dealerapp.siriusxm.com/services/DBSuccessUpdate/DBUpdateForGoogle

    try:
        params = {"os":deviceiOSVersion,"dm":deviceModel,"did":uuid4,"ua":"iPhone","aid":"DealerApp","aname":"SiriusXM Dealer","chnl":"mobile","plat":"ios","aver":appVer,"atype":"native","stype":"b2c","kuid":"","mfaid":"df7be3dc-e278-436c-b2f8-4cfde321df0a","mfbaseid":"efb9acb6-daea-4f2f-aeb3-b17832bdd47b","mfaname":"DealerApp","sdkversion":"9.5.36","sdktype":"js","fid":"frmRadioRefresh","sessiontype":"I","clientUUID":"1742536405634-41a8-0de0-125c","rsid":"1742536405654-b954-784f-38d2","svcid":"DBUpdateForGoogle"}
        paramsStr = json.dumps(params, separators=(',', ':'))
        response = session.post(
            url=
            "https://dealerapp.siriusxm.com/services/DBSuccessUpdate/DBUpdateForGoogle",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": userAgent,
                "X-Voltmx-Authorization": auth_token,
                "X-Voltmx-ReportingParams": urllib.parse.quote(paramsStr, safe='$:,'),
            },
            data={
                "OM_ELIGIBILITY_STATUS": "Eligible",
                "appVersion": appVer,
                "flag": "failure",
                "Radio_ID": radio_id_input,
                "deviceID": uuid4,
                "G_PLACES_REQUEST": "",
                "OS_Version": urllib.parse.quote("iPhone " + deviceiOSVersion, safe='$:,'),
                "G_PLACES_RESPONSE": "",
                "Confirmation_Status": "SUCCESS",
                "seqVal": seq,
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except Exception:
        print('HTTP Request failed')


def blocklist():
    # BlockListDevice
    # POST https://dealerapp.siriusxm.com/services/USBlockListDevice/BlockListDevice

    try:
        params = {"os":deviceiOSVersion,"dm":deviceModel,"did":uuid4,"ua":"iPhone","aid":"DealerApp","aname":"SiriusXM Dealer","chnl":"mobile","plat":"ios","aver":appVer,"atype":"native","stype":"b2c","kuid":"","mfaid":"df7be3dc-e278-436c-b2f8-4cfde321df0a","mfbaseid":"efb9acb6-daea-4f2f-aeb3-b17832bdd47b","mfaname":"DealerApp","sdkversion":"9.5.36","sdktype":"js","fid":"frmRadioRefresh","sessiontype":"I","clientUUID":"1742536405634-41a8-0de0-125c","rsid":"1742536405654-b954-784f-38d2","svcid":"BlockListDevice"}
        paramsStr = json.dumps(params, separators=(',', ':'))
        response = session.post(
            url=
            "https://dealerapp.siriusxm.com/services/USBlockListDevice/BlockListDevice",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": userAgent,
                "X-Voltmx-Authorization": auth_token,
                "X-Voltmx-ReportingParams": urllib.parse.quote(paramsStr, safe='$:,'),
            },
            data={
                "deviceId": uuid4,
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except Exception:
        print('HTTP Request failed')


def oracle():
    # Request (9)
    # POST https://oemremarketing.custhelp.com/cgi-bin/oemremarketing.cfg/php/custom/src/oracle/program_status.php

    try:
        response = session.post(
            url=
            "https://oemremarketing.custhelp.com/cgi-bin/oemremarketing.cfg/php/custom/src/oracle/program_status.php",
            params={
                "google_addr": "395 EASTERN BLVD, MONTGOMERY, AL 36117, USA",
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "*/*",
                "User-Agent": userAgent,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "X-Voltmx-ReportingParams": "",
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except Exception:
        print('HTTP Request failed')


def createAccount():
    # CreateAccount
    # POST https://dealerapp.siriusxm.com/services/DealerAppService3/CreateAccount

    try:
        params = {"os":deviceiOSVersion,"dm":deviceModel,"did":uuid4,"ua":"iPhone","aid":"DealerApp","aname":"SiriusXM Dealer","chnl":"mobile","plat":"ios","aver":appVer,"atype":"native","stype":"b2c","kuid":"","mfaid":"df7be3dc-e278-436c-b2f8-4cfde321df0a","mfbaseid":"efb9acb6-daea-4f2f-aeb3-b17832bdd47b","mfaname":"DealerApp","sdkversion":"9.5.36","sdktype":"js","fid":"frmRadioRefresh","sessiontype":"I","clientUUID":"1742536405634-41a8-0de0-125c","rsid":"1742536405654-b954-784f-38d2","svcid":"CreateAccount"}
        paramsStr = json.dumps(params, separators=(',', ':'))
        response = session.post(
            url=
            "https://dealerapp.siriusxm.com/services/DealerAppService3/CreateAccount",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": userAgent,
                "X-Voltmx-Authorization": auth_token,
                "X-Voltmx-ReportingParams": urllib.parse.quote(paramsStr, safe='$:,'),
            },
            data={
                "seqVal": seq,
                "deviceId": radio_id_input,
                "oracleCXFailed": "1",
                "appVersion": appVer,
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except Exception:
        print('HTTP Request failed')


def update_2():
    # 2-updateDeviceSATRefreshWithPriority
    # POST https://dealerapp.siriusxm.com/services/USUpdateDeviceRefreshForCC/updateDeviceSATRefreshWithPriority

    try:
        params = {"os":deviceiOSVersion,"dm":deviceModel,"did":uuid4,"ua":"iPhone","aid":"DealerApp","aname":"SiriusXM Dealer","chnl":"mobile","plat":"ios","aver":appVer,"atype":"native","stype":"b2c","kuid":"","mfaid":"df7be3dc-e278-436c-b2f8-4cfde321df0a","mfbaseid":"efb9acb6-daea-4f2f-aeb3-b17832bdd47b","mfaname":"DealerApp","sdkversion":"9.5.36","sdktype":"js","fid":"frmRadioRefresh","sessiontype":"I","clientUUID":"1742536405634-41a8-0de0-125c","rsid":"1742536405654-b954-784f-38d2","svcid":"updateDeviceSATRefreshWithPriority"}
        paramsStr = json.dumps(params, separators=(',', ':'))
        response = session.post(
            url=
            "https://dealerapp.siriusxm.com/services/USUpdateDeviceRefreshForCC/updateDeviceSATRefreshWithPriority",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": userAgent,
                "X-Voltmx-Authorization": auth_token,
                "X-Voltmx-ReportingParams": urllib.parse.quote(paramsStr, safe='$:,'),
            },
            data={
                "deviceId": radio_id_input,
                "provisionPriority": "2",
                "appVersion": appVer,
                "device_Type": urllib.parse.quote("iPhone " + deviceModel, safe='$:,'),
                "deviceID": uuid4,
                "os_Version": urllib.parse.quote("iPhone " + deviceiOSVersion, safe='$:,'),
                "provisionType": "activate",
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except Exception:
        print('HTTP Request failed')

# Global variables used for requests
radio_id_input = input("Enter Radio ID or VIN: ").upper()
uuid4 = str(uuid.uuid4())
auth_token = ""
seq = ""
deviceModel = "iPhone 14 Pro"
deviceiOSVersion = "17.0"
appVer = "3.1.0"
userAgent = "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0"

session = requests.Session()

if len(radio_id_input) == 17:
    # VIN Activiation
    print("login")
    auth_token = login()
    print("versionControl")
    versionControl()
    print("getProperties")
    getProperties()
    print("update_1_vin")
    seq = update_1_vin()
    print("USDealerVehicleData")
    radio_id_result = USDealerVehicleData()
    if radio_id_result is None:
        sys.exit(1)
    radio_id_input = radio_id_result
    print("getCRM")
    getCRM()
    print("blocklist")
    blocklist()
    print("createAccount")
    createAccount()
    print("update_2")
    update_2()
elif len(radio_id_input) == 8 or len(radio_id_input) == 12:
    # Radio ID Activation
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
    print("blocklist")
    blocklist()
    print("createAccount")
    createAccount()
    print("update_2")
    update_2()
else:
    print("The VIN/Radio ID you entered is incorrect. Radio IDs are either 8 characters or 12 digits long and VINs are 17 characters long.")