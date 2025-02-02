import requests
import uuid
import argparse

def appconfig():
    # appConfig
    # POST https://dealerapp.siriusxm.com/authService/100000002/appconfig

    try:
        response = requests.post(
            url="https://dealerapp.siriusxm.com/authService/100000002/appconfig",
            headers={
                "X-Kony-Integrity":
                "GWSUSEVMJK;FEC9AA232EC59BE8A39F0FAE1B71300216E906B85F40CA2B1C5C7A59F85B17A4",
                "X-HTTP-Method-Override": "GET",
                "X-Voltmx-App-Key": "67cfe0220c41a54cb4e768723ad56b41",
                "Accept": "*/*",
                "X-Voltmx-App-Secret": "c086fca8646a72cf391f8ae9f15e5331",
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "User-Agent": "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
            },
        )
        if verbose:
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def login():
    # login
    # POST https://dealerapp.siriusxm.com/authService/100000002/login

    try:
        response = requests.post(
            url="https://dealerapp.siriusxm.com/authService/100000002/login",
            headers={
                "X-Voltmx-Platform-Type": "ios",
                "Accept": "application/json",
                "X-Voltmx-App-Secret": "c086fca8646a72cf391f8ae9f15e5331",
                "Accept-Language": "en-us",
                "X-Voltmx-SDK-Type": "js",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-SDK-Version": "9.5.36",
                "X-Voltmx-App-Key": "67cfe0220c41a54cb4e768723ad56b41",
            },
        )
        return response.json().get('claims_token').get('value')
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def versionControl():
    # VersionControl
    # POST https://dealerapp.siriusxm.com/services/DealerAppService7/VersionControl

    try:
        response = requests.post(
            url=
            "https://dealerapp.siriusxm.com/services/DealerAppService7/VersionControl",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-Authorization": auth_token,
            },
            data={
                "deviceCategory": "iPhone",
                "appver": "3.1.0",
                "deviceLocale": "en_US",
                "deviceModel": "iPhone%206%20Plus",
                "deviceVersion": "12.5.7",
                "deviceType": "",
            },
        )
        if verbose:
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def getProperties():
    # getProperties
    # POST https://dealerapp.siriusxm.com/services/DealerAppService7/getProperties

    try:
        response = requests.post(
            url=
            "https://dealerapp.siriusxm.com/services/DealerAppService7/getProperties",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-Authorization": auth_token,
            },
        )
        if verbose:
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def update_1():
    # 1-updateDeviceSATRefreshWithPriority
    # POST https://dealerapp.siriusxm.com/services/USUpdateDeviceSATRefresh/updateDeviceSATRefreshWithPriority

    try:
        response = requests.post(
            url=
            "https://dealerapp.siriusxm.com/services/USUpdateDeviceSATRefresh/updateDeviceSATRefreshWithPriority",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-Authorization": auth_token,
            },
            data={
                "deviceId": radio_id_input,
                "appVersion": "3.1.0",
                "lng": "-86.210313195",
                "deviceID": uuid4,
                "provisionPriority": "2",
                "provisionType": "activate",
                "lat": "32.37436705",
            },
        )
        if verbose:
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
        return response.json().get('seqValue')
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def getCRM():
    # GetCRMAccountPlanInformation
    # POST https://dealerapp.siriusxm.com/services/DemoConsumptionRules/GetCRMAccountPlanInformation

    try:
        response = requests.post(
            url=
            "https://dealerapp.siriusxm.com/services/DemoConsumptionRules/GetCRMAccountPlanInformation",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-Authorization": auth_token,
            },
            data={
                "seqVal": seq,
                "deviceId": radio_id_input,
            },
        )
        if verbose:
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def dbUpdate():
    # DBUpdateForGoogle
    # POST https://dealerapp.siriusxm.com/services/DBSuccessUpdate/DBUpdateForGoogle

    try:
        response = requests.post(
            url=
            "https://dealerapp.siriusxm.com/services/DBSuccessUpdate/DBUpdateForGoogle",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-Authorization": auth_token,
            },
            data={
                "OM_ELIGIBILITY_STATUS": "Eligible",
                "appVersion": "3.1.0",
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
        if verbose:
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def blocklist():
    # BlockListDevice
    # POST https://dealerapp.siriusxm.com/services/USBlockListDevice/BlockListDevice

    try:
        response = requests.post(
            url=
            "https://dealerapp.siriusxm.com/services/USBlockListDevice/BlockListDevice",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-Authorization": auth_token,
            },
            data={
                "deviceId": uuid4,
            },
        )
        if verbose:
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
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
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
            },
        )
        if verbose:
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def createAccount():
    # CreateAccount
    # POST https://dealerapp.siriusxm.com/services/DealerAppService3/CreateAccount

    try:
        response = requests.post(
            url=
            "https://dealerapp.siriusxm.com/services/DealerAppService3/CreateAccount",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-Authorization": auth_token,
            },
            data={
                "seqVal": seq,
                "deviceId": radio_id_input,
                "oracleCXFailed": "1",
                "appVersion": "3.1.0",
            },
        )
        if verbose:
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def update_2():
    # 2-updateDeviceSATRefreshWithPriority
    # POST https://dealerapp.siriusxm.com/services/USUpdateDeviceRefreshForCC/updateDeviceSATRefreshWithPriority

    try:
        response = requests.post(
            url=
            "https://dealerapp.siriusxm.com/services/USUpdateDeviceRefreshForCC/updateDeviceSATRefreshWithPriority",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-Authorization": auth_token,
            },
            data={
                "deviceId": radio_id_input,
                "provisionPriority": "2",
                "appVersion": "3.1.0",
                "device_Type": "iPhone iPhone 6 Plus",
                "deviceID": uuid4,
                "os_Version": "iPhone 12.5.7",
                "provisionType": "activate",
            },
        )
        if verbose:
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument('-d', '--deviceid', type=str, help='Directly pass the device ID')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    args = parser.parse_args()

    verbose = args.verbose
    requests = requests.Session()

    if args.deviceid:
        radio_id_input = args.deviceid.upper()
    else:
        radio_id_input = input("Enter Radio ID: ")
        radio_id_input = radio_id_input.upper()

    uuid4 = str(uuid.uuid4())
    auth_token = ""
    seq = ""

    if verbose:
        print("appconfig")
    appconfig()
    if verbose:
        print("login")
    auth_token = login()
    if verbose:
        print("versionControl")
    versionControl()
    if verbose:
        print("getProperties")
    getProperties()
    if verbose:
        print("update_1")
    seq = update_1()
    if verbose:
        print("getCRM")
    getCRM()
    if verbose:
        print("dbUpdate")
    dbUpdate()
    if verbose:
        print("blocklist")
    blocklist()
    if verbose:
        print("oracle")
    oracle()
    if verbose:
        print("createAccount")
    createAccount()
    if verbose:
        print("update_2")
    update_2()
