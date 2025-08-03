import requests
import uuid
import json
import urllib.parse
from typing import Optional, Dict, Any, Generator, Tuple
import argparse

class SiriusXMActivator:

    def __init__(self, device_model: str = "iPhone 14 Pro", 
                 device_ios_version: str = "17.0", 
                 app_version: str = "3.1.0"):

        self.device_model = device_model
        self.device_ios_version = device_ios_version
        self.app_version = app_version
        self.user_agent = "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0"
        
        self.uuid4 = str(uuid.uuid4())
        self.session = requests.Session()
        self.auth_token = ""
        self.seq = ""
        self.radio_id = ""
        
    def _get_common_params(self, service_id: str, form_id: str = "frmHome") -> Dict[str, Any]:
        return {
            "os": self.device_ios_version,
            "dm": self.device_model,
            "did": self.uuid4,
            "ua": "iPhone",
            "aid": "DealerApp",
            "aname": "SiriusXM Dealer",
            "chnl": "mobile",
            "plat": "ios",
            "aver": self.app_version,
            "atype": "native",
            "stype": "b2c",
            "kuid": "",
            "mfaid": "df7be3dc-e278-436c-b2f8-4cfde321df0a",
            "mfbaseid": "efb9acb6-daea-4f2f-aeb3-b17832bdd47b",
            "mfaname": "DealerApp",
            "sdkversion": "9.5.36",
            "sdktype": "js",
            "fid": form_id,
            "sessiontype": "I",
            "clientUUID": "1742536405634-41a8-0de0-125c",
            "rsid": "1742536405654-b954-784f-38d2",
            "svcid": service_id
        }
    
    def _get_common_headers(self, auth_required: bool = True) -> Dict[str, str]:
        headers = {
            "Accept": "*/*",
            "X-Voltmx-API-Version": "1.0",
            "X-Voltmx-DeviceId": self.uuid4,
            "Accept-Language": "en-us",
            "Accept-Encoding": "br, gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": self.user_agent,
        }
        
        if auth_required and self.auth_token:
            headers["X-Voltmx-Authorization"] = self.auth_token
            
        return headers

    def login(self) -> Optional[str]:
        try:
            params = self._get_common_params("login_$anonymousProvider")
            params_str = json.dumps(params, separators=(',', ':'))
            
            response = self.session.post(
                url="https://dealerapp.siriusxm.com/authService/100000002/login",
                headers={
                    "X-Voltmx-Platform-Type": "ios",
                    "Accept": "application/json",
                    "X-Voltmx-App-Secret": "c086fca8646a72cf391f8ae9f15e5331",
                    "Accept-Language": "en-us",
                    "X-Voltmx-SDK-Type": "js",
                    "Accept-Encoding": "br, gzip, deflate",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": self.user_agent,
                    "X-Voltmx-SDK-Version": "9.5.36",
                    "X-Voltmx-App-Key": "67cfe0220c41a54cb4e768723ad56b41",
                    "X-Voltmx-ReportingParams": urllib.parse.quote(params_str, safe='$:,'),
                },
            )
            
            self.auth_token = response.json().get('claims_token', {}).get('value', '')
            return self.auth_token
            
        except Exception as e:
            raise Exception(f'Login failed: {e}')

    def version_control(self) -> bool:
        try:
            params = self._get_common_params("VersionControl")
            params_str = json.dumps(params, separators=(',', ':'))
            
            headers = self._get_common_headers()
            headers["X-Voltmx-ReportingParams"] = urllib.parse.quote(params_str, safe='$:,')
            
            response = self.session.post(
                url="https://dealerapp.siriusxm.com/services/DealerAppService7/VersionControl",
                headers=headers,
                data={
                    "deviceCategory": "iPhone",
                    "appver": self.app_version,
                    "deviceLocale": "en_US",
                    "deviceModel": self.device_model,
                    "deviceVersion": self.device_ios_version,
                    "deviceType": "",
                },
            )
            return response.status_code == 200
            
        except Exception as e:
            raise Exception(f'Version control failed: {e}')

    def get_properties(self) -> bool:
        try:
            params = self._get_common_params("getProperties")
            params_str = json.dumps(params, separators=(',', ':'))
            
            headers = self._get_common_headers()
            headers["X-Voltmx-ReportingParams"] = urllib.parse.quote(params_str, safe='$:,')
            
            response = self.session.post(
                url="https://dealerapp.siriusxm.com/services/DealerAppService7/getProperties",
                headers=headers,
            )
            return response.status_code == 200
            
        except Exception as e:
            raise Exception(f'Get properties failed: {e}')

    def update_device_sat_refresh(self, radio_id: str, use_vin: bool = False) -> Tuple[Optional[str], str]:
        try:
            params = self._get_common_params("updateDeviceSATRefreshWithPriority", "frmRadioRefresh")
            params_str = json.dumps(params, separators=(',', ':'))
            
            headers = self._get_common_headers()
            headers["X-Voltmx-ReportingParams"] = urllib.parse.quote(params_str, safe='$:,')
            
            data = {
                "appVersion": self.app_version,
                "deviceID": self.uuid4,
                "provisionPriority": "2",
                "provisionType": "activate",
            }
            
            if use_vin:
                data["deviceId"] = ""
                data["vin"] = radio_id
            else:
                data["deviceId"] = radio_id
            
            response = self.session.post(
                url="https://dealerapp.siriusxm.com/services/USUpdateDeviceSATRefresh/updateDeviceSATRefreshWithPriority",
                headers=headers,
                data=data,
            )
            
            response_content = f'Response HTTP Response Body: {response.content}'
            return response.json().get('seqValue'), response_content
            
        except Exception as e:
            raise Exception(f'Update device SAT refresh failed: {e}')

    def get_dealer_vehicle_data(self, vin: str) -> Tuple[Optional[str], str]:
        try:
            params = self._get_common_params("USDealerVehicleData", "frmRadioRefresh")
            params_str = json.dumps(params, separators=(',', ':'))
            
            headers = self._get_common_headers()
            headers["X-Voltmx-ReportingParams"] = urllib.parse.quote(params_str, safe='$:,')
            
            response = self.session.post(
                url="https://dealerapp.siriusxm.com/services/VehicleDataRestService/USDealerVehicleData",
                headers=headers,
                data={"vin": vin},
            )
            
            response_content = f'Response HTTP Response Body: {response.content}'
            
            result = response.json()
            if result.get('errorMessage', '') != "":
                error_msg = f"Error: {result.get('errorMessage')}\nYou will need to manually enter the Radio ID, not the VIN, sorry :("
                return None, f"{response_content}\n{error_msg}"
            else:
                return result.get('radioID'), response_content
                
        except Exception as e:
            raise Exception(f'Get dealer vehicle data failed: {e}')

    def get_crm_account_plan_information(self, seq_val: str, device_id: str) -> str:
        try:
            params = self._get_common_params("GetCRMAccountPlanInformation", "frmRadioRefresh")
            params_str = json.dumps(params, separators=(',', ':'))
            
            headers = self._get_common_headers()
            headers["X-Voltmx-ReportingParams"] = urllib.parse.quote(params_str, safe='$:,')
            
            response = self.session.post(
                url="https://dealerapp.siriusxm.com/services/DemoConsumptionRules/GetCRMAccountPlanInformation",
                headers=headers,
                data={
                    "seqVal": seq_val,
                    "deviceId": device_id,
                },
            )
            
            return f'Response HTTP Response Body: {response.content}'
            
        except Exception as e:
            raise Exception(f'Get CRM account plan information failed: {e}')

    def block_list_device(self) -> str:
        try:
            params = self._get_common_params("BlockListDevice", "frmRadioRefresh")
            params_str = json.dumps(params, separators=(',', ':'))
            
            headers = self._get_common_headers()
            headers["X-Voltmx-ReportingParams"] = urllib.parse.quote(params_str, safe='$:,')
            
            response = self.session.post(
                url="https://dealerapp.siriusxm.com/services/USBlockListDevice/BlockListDevice",
                headers=headers,
                data={"deviceId": self.uuid4},
            )
            
            return f'Response HTTP Response Body: {response.content}'
            
        except Exception as e:
            raise Exception(f'Block list device failed: {e}')

    def create_account(self, seq_val: str, device_id: str) -> str:
        try:
            params = self._get_common_params("CreateAccount", "frmRadioRefresh")
            params_str = json.dumps(params, separators=(',', ':'))
            
            headers = self._get_common_headers()
            headers["X-Voltmx-ReportingParams"] = urllib.parse.quote(params_str, safe='$:,')
            
            response = self.session.post(
                url="https://dealerapp.siriusxm.com/services/DealerAppService3/CreateAccount",
                headers=headers,
                data={
                    "seqVal": seq_val,
                    "deviceId": device_id,
                    "oracleCXFailed": "1",
                    "appVersion": self.app_version,
                },
            )
            
            return f'Response HTTP Response Body: {response.content}'
            
        except Exception as e:
            raise Exception(f'Create account failed: {e}')

    def update_device_refresh_for_cc(self, device_id: str) -> str:
        try:
            params = self._get_common_params("updateDeviceSATRefreshWithPriority", "frmRadioRefresh")
            params_str = json.dumps(params, separators=(',', ':'))
            
            headers = self._get_common_headers()
            headers["X-Voltmx-ReportingParams"] = urllib.parse.quote(params_str, safe='$:,')
            
            response = self.session.post(
                url="https://dealerapp.siriusxm.com/services/USUpdateDeviceRefreshForCC/updateDeviceSATRefreshWithPriority",
                headers=headers,
                data={
                    "deviceId": device_id,
                    "provisionPriority": "2",
                    "appVersion": self.app_version,
                    "device_Type": urllib.parse.quote("iPhone " + self.device_model, safe='$:,'),
                    "deviceID": self.uuid4,
                    "os_Version": urllib.parse.quote("iPhone " + self.device_ios_version, safe='$:,'),
                    "provisionType": "activate",
                },
            )
            
            return f'Response HTTP Response Body: {response.content}'
            
        except Exception as e:
            raise Exception(f'Update device refresh for CC failed: {e}')

    def activate_radio(self, radio_id_or_vin: str) -> Generator[Tuple[str, str, bool], None, bool]:
        radio_id_input = radio_id_or_vin.upper()
        
        # Validate input
        if len(radio_id_input) not in [8, 12, 17]:
            yield ("validation", "The VIN/Radio ID you entered is incorrect. Radio IDs are either 8 characters or 12 digits long and VINs are 17 characters long.", True)
            return False
        
        try:
            # Login
            yield ("login", "Starting login...", False)
            if not self.login():
                yield ("login", "Login failed - no auth token received", True)
                return False
            yield ("login", "Login successful", False)
            
            # Version control
            yield ("versionControl", "Checking version control...", False)
            if not self.version_control():
                yield ("versionControl", "Version control failed", True)
                return False
            yield ("versionControl", "Version control successful", False)
            
            # Get properties
            yield ("getProperties", "Getting properties...", False)
            if not self.get_properties():
                yield ("getProperties", "Get properties failed", True)
                return False
            yield ("getProperties", "Get properties successful", False)
            
            # Handle VIN vs Radio ID
            if len(radio_id_input) == 17:
                # VIN Activation
                yield ("update_1_vin", "Updating device SAT refresh with VIN...", False)
                seq, response_content = self.update_device_sat_refresh(radio_id_input, use_vin=True)
                yield ("update_1_vin", response_content, False)
                if not seq:
                    yield ("update_1_vin", "Update device SAT refresh failed - no sequence value", True)
                    return False
                
                yield ("USDealerVehicleData", "Getting vehicle data from VIN...", False)
                radio_id_result, response_content = self.get_dealer_vehicle_data(radio_id_input)
                yield ("USDealerVehicleData", response_content, False)
                if radio_id_result is None:
                    yield ("USDealerVehicleData", "Failed to get Radio ID from VIN", True)
                    return False
                radio_id_input = radio_id_result
            else:
                # Radio ID Activation
                yield ("update_1", "Updating device SAT refresh with Radio ID...", False)
                seq, response_content = self.update_device_sat_refresh(radio_id_input, use_vin=False)
                yield ("update_1", response_content, False)
                if not seq:
                    yield ("update_1", "Update device SAT refresh failed - no sequence value", True)
                    return False
            
            self.seq = seq
            self.radio_id = radio_id_input
            
            # Continue with common steps
            yield ("getCRM", "Getting CRM account plan information...", False)
            response_content = self.get_crm_account_plan_information(seq, radio_id_input)
            yield ("getCRM", response_content, False)
            
            yield ("blocklist", "Processing block list...", False)
            response_content = self.block_list_device()
            yield ("blocklist", response_content, False)
            
            yield ("createAccount", "Creating account...", False)
            response_content = self.create_account(seq, radio_id_input)
            yield ("createAccount", response_content, False)
            
            yield ("update_2", "Final device refresh update...", False)
            response_content = self.update_device_refresh_for_cc(radio_id_input)
            yield ("update_2", response_content, False)
            
            yield ("completion", "Activation process completed successfully!", False)
            return True
            
        except Exception as e:
            yield ("error", str(e), True)
            return False


def main():
    parser = argparse.ArgumentParser(description='Activate a SiriusXM radio using Radio ID or VIN.')
    parser.add_argument('-r', '--radio_id', help='Radio ID or VIN to activate')
    args = parser.parse_args()

    radio_id_input = args.radio_id if args.radio_id else input("Enter Radio ID or VIN: ")

    activator = SiriusXMActivator()

    for step_name, message, is_error in activator.activate_radio(radio_id_input):
        if is_error:
            print(f"ERROR: {message}")
        else:
            print(message)

if __name__ == "__main__":
    main()