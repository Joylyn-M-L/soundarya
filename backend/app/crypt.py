from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import time

# AES (key 16 bytes)
AES_KEY = get_random_bytes(16)
AES_IV = get_random_bytes(16)

# DES (key 8 bytes)
DES_KEY = get_random_bytes(8)
DES_IV = get_random_bytes(8)

def encrypt_aes(data: str) -> bytes:
    cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    return AES_IV + ct_bytes  # include IV with ciphertext

def decrypt_aes(data: bytes) -> str:
    iv = data[:16]
    ct = data[16:]
    cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()

def encrypt_des(data: str) -> bytes:
    cipher = DES.new(DES_KEY, DES.MODE_CBC, DES_IV)
    ct_bytes = cipher.encrypt(pad(data.encode(), DES.block_size))
    return DES_IV + ct_bytes  # include IV with ciphertext

def decrypt_des(data: bytes) -> str:
    iv = data[:8]
    ct = data[8:]
    cipher = DES.new(DES_KEY, DES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), DES.block_size)
    return pt.decode()


# from Crypto.Cipher import AES, DES
# from Crypto.Util.Padding import pad, unpad
# from Crypto.Random import get_random_bytes

# # AES Encryption
# def encrypt_aes(data: str):
#     key = get_random_bytes(16)  # AES key of 16 bytes
#     cipher = AES.new(key, AES.MODE_CBC)
#     ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
#     return cipher.iv.hex() + ct_bytes.hex()

# def decrypt_aes(data: str):
#     iv = bytes.fromhex(data[:32])  # Extract the IV from the input
#     ct = bytes.fromhex(data[32:])  # Extract the ciphertext
#     key = get_random_bytes(16)  # AES key of 16 bytes (should be managed securely)
#     cipher = AES.new(key, AES.MODE_CBC, iv=iv)
#     decrypted = unpad(cipher.decrypt(ct), AES.block_size)
#     return decrypted.decode()

# # DES Encryption
# def encrypt_des(data: str):
#     key = get_random_bytes(8)  # DES key of 8 bytes
#     cipher = DES.new(key, DES.MODE_CBC)
#     ct_bytes = cipher.encrypt(pad(data.encode(), DES.block_size))
#     return cipher.iv.hex() + ct_bytes.hex()

# def decrypt_des(data: str):
#     iv = bytes.fromhex(data[:32])  # Extract the IV from the input
#     ct = bytes.fromhex(data[32:])  # Extract the ciphertext
#     key = get_random_bytes(8)  # DES key of 8 bytes (should be managed securely)
#     cipher = DES.new(key, DES.MODE_CBC, iv=iv)
#     decrypted = unpad(cipher.decrypt(ct), DES.block_size)
#     return decrypted.decode()
