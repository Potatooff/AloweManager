import requests
import subprocess


PORT: int = 5438 # api port

def _launch_api() -> None:
    """Launches the C# script"""

    global process
    process = subprocess.Popen([r'C:\Users\Hi\Desktop\Alowe\src\Corelia\bin\Debug\net7.0\Corelia.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def _close_api() -> None:
    """Closes the C# script"""

    process.terminate()
    process.wait() 

class Corely():

    def SentinelEn(ports: int, unlocking: str, secret: str) -> str:
        ports = PORT

        try:
            url = f'http://localhost:{ports}/SentinelEn'  

            data = {
                "Key": unlocking,
                "Security": secret
            }

            response = requests.post(url, json=data)  
            response.raise_for_status() 
            if response.status_code == 200:
                return response.text
            else:
                print(f"An error occurred while generating the password, {response.status_code}")

        except requests.exceptions.RequestException as e:
            print("An error occurred while generating the password # API!\n", e)

    
    def SentinelDe(ports: int, unlocking: str, secret: str) -> str: 
        ports = PORT

        try:
            url = f'http://localhost:{ports}/SentinelDe'  

            data = {
                "Key": unlocking,
                "Security": secret
            }

            response = requests.post(url, json=data)  
            response.raise_for_status() 
            if response.status_code == 200:
                return response.text
            else:
                print(f"An error occurred while generating the password, {response.status_code}")

        except requests.exceptions.RequestException as e:
            print("An error occurred while generating the password # API!\n", e)

    

    def CryoSecureCreatorDefault(ports: int, length: int) -> str:
        ports = PORT

        try:
            url = f'http://localhost:{ports}/Cryotling/Default'  

            data = {
                "Length": length,
            }

            response = requests.post(url, json=data)  
            response.raise_for_status() 
            if response.status_code == 200:
                return response.text
            else:
                print(f"An error occurred while generating the password, {response.status_code}")

        except requests.exceptions.RequestException as e:
            print("An error occurred while generating the password # API!\n", e)

    def CryoSecureCreatorCustom(ports: int, length: int, uppercase: bool, lowercase: bool, digits: bool, punctuations: bool) -> str:
        ports = PORT

        try:
            url = f'http://localhost:{ports}/Cryotling/Creator'  

            data = {
                "Length": length,
                "Numbers": digits,
                "Specials": punctuations,
                "Upper": uppercase,
                "Lower": lowercase
            }

            response = requests.post(url, json=data)  
            response.raise_for_status() 
            if response.status_code == 200:
                return response.text
            else:
                print(f"An error occurred while generating the password, {response.status_code}")

        except requests.exceptions.RequestException as e:
            print("An error occurred while generating the password # API!\n", e)

    def CryoSecureEncrypt(ports: int, secret: str, shifting: int) -> str:
        ports = PORT

        try:
            url = f'http://localhost:{ports}/Cryotling/Encryption'  

            data = {
                "Secret": secret,
                "Shifts": shifting
            }

            response = requests.post(url, json=data)  
            response.raise_for_status() 
            if response.status_code == 200:
                return response.text
            else:
                print(f"An error occurred while generating the password, {response.status_code}")

        except requests.exceptions.RequestException as e:
            print("An error occurred while generating the password # API!\n", e)

    
    def CryoSecureDecrypt(ports: int, secret: str, shifting: int) -> str:
        ports = PORT

        try:
            url = f'http://localhost:{ports}/Cryotling/Decryption'  

            data = {
                "Secret": secret,
                "Shifts": shifting
            }

            response = requests.post(url, json=data)  
            response.raise_for_status() 
            if response.status_code == 200:
                return response.text
            else:
                print(f"An error occurred while generating the password, {response.status_code}")

        except requests.exceptions.RequestException as e:
            print("An error occurred while generating the password # API!\n", e)



    def CryoSecureCrusher(ports: int, secret: str, workfactor: int) -> str:
        ports = PORT

        try:
            url = f'http://localhost:{ports}/Cryotling/CandyCrusher'  

            data = {
                "Secret": secret,
                "WorkFactor": workfactor
            }

            response = requests.post(url, json=data)  
            response.raise_for_status() 
            if response.status_code == 200:
                return response.text
            else:
                print(f"An error occurred while generating the password, {response.status_code}")

        except requests.exceptions.RequestException as e:
            print("An error occurred while generating the password # API!\n", e)

    def CryoSecureCrusherChecker(ports: int, secret: str, securely: int) -> str:
        ports = PORT

        try:
            url = f'http://localhost:{ports}/Cryotling/CandyCrusherChecker'  

            data = {
                "Secret": secret,
                "Securely": securely
            }

            response = requests.post(url, json=data)  
            response.raise_for_status() 
            if response.status_code == 200:
                return response.text
            else:
                print(f"An error occurred while generating the password, {response.status_code}")

        except requests.exceptions.RequestException as e:
            print("An error occurred while generating the password # API!\n", e)


try:
    _launch_api()

except KeyboardInterrupt:
    pass
finally:
    _close_api
