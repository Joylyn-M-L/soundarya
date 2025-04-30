# backend/app.py

from fastapi import FastAPI
from pydantic import BaseModel
from Crypto.Cipher import AES, DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import time

app = FastAPI()

# AES Encryption
def aes_encrypt(message: str, key: bytes):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ct_bytes

def aes_decrypt(ciphertext: bytes, key: bytes):
    iv = ciphertext[:16]
    ct = ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()

# DES Encryption
def des_encrypt(message: str, key: bytes):
    cipher = DES.new(key, DES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), DES.block_size))
    return cipher.iv + ct_bytes

def des_decrypt(ciphertext: bytes, key: bytes):
    iv = ciphertext[:8]
    ct = ciphertext[8:]
    cipher = DES.new(key, DES.MODE_CBC, iv=iv)
    pt = unpad(cipher.decrypt(ct), DES.block_size)
    return pt.decode()

# Model for input validation
class Message(BaseModel):
    text: str
    key: str

# AES encryption endpoint
@app.post("/encrypt")
def encrypt(message: Message, algorithm: str):
    start_time = time.time()
    key = bytes.fromhex(message.key)

    if algorithm == "aes":
        encrypted_message = aes_encrypt(message.text, key)
    elif algorithm == "des":
        encrypted_message = des_encrypt(message.text, key)
    
    end_time = time.time()
    encryption_time = end_time - start_time

    return {"encrypted_message": encrypted_message.hex(), "time": encryption_time}

# AES decryption endpoint
@app.post("/decrypt")
def decrypt(message: Message, algorithm: str):
    start_time = time.time()
    key = bytes.fromhex(message.key)
    ciphertext = bytes.fromhex(message.text)

    if algorithm == "aes":
        decrypted_message = aes_decrypt(ciphertext, key)
    elif algorithm == "des":
        decrypted_message = des_decrypt(ciphertext, key)

    end_time = time.time()
    decryption_time = end_time - start_time

    return {"decrypted_message": decrypted_message, "time": decryption_time}
