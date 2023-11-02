import base64
import bcrypt

def CorneliaBasicEncoder(data: str):

    data_bytes = data.encode('utf-8')

    encoded_data = base64.b64encode(data_bytes).decode('utf-8')

    return encoded_data

def CorneliaBasicEncoder(data: str):
    
    decoded_bytes = base64.b64decode(data)

    decoded_data = decoded_bytes.decode('utf-8')

    return decoded_data


def CorneliaBeast(password: str, salt_rounds=15):

    salt = bcrypt.gensalt(salt_rounds)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password



def whatisthis(data: str):

    data = CorneliaBasicEncoder(data)
    data = CorneliaBasicEncoder(data)
    data = CorneliaBeast(data)
    return data