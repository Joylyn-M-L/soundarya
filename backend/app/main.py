from fastapi import FastAPI
from pydantic import BaseModel
from .crypt import encrypt_aes, decrypt_aes, encrypt_des, decrypt_des
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend access (important!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    plaintext: str


@app.post("/encrypt_aes/")
def encrypt_aes_api(input: TextInput):
    ciphertext = encrypt_aes(input.plaintext)
    decrypted = decrypt_aes(ciphertext)
    return {"ciphertext": ciphertext.hex(), "decrypted": decrypted}

@app.post("/encrypt_des/")
def encrypt_des_api(input: TextInput):
    ciphertext = encrypt_des(input.plaintext)
    decrypted = decrypt_des(ciphertext)
    return {"ciphertext": ciphertext.hex(), "decrypted": decrypted}



# from fastapi import FastAPI
# from .crypt import encrypt_aes, decrypt_aes, encrypt_des, decrypt_des
# import time

# app = FastAPI()

# @app.get("/encrypt_aes")
# def encrypt_aes_route(data: str):
#     start_time = time.time()
#     encrypted_data = encrypt_aes(data)
#     end_time = time.time()
#     time_taken = end_time - start_time
#     return {"encrypted_data": encrypted_data, "time_taken": time_taken}

# @app.get("/decrypt_aes")
# def decrypt_aes_route(data: str):
#     start_time = time.time()
#     decrypted_data = decrypt_aes(data)
#     end_time = time.time()
#     time_taken = end_time - start_time
#     return {"decrypted_data": decrypted_data, "time_taken": time_taken}

# @app.get("/encrypt_des")
# def encrypt_des_route(data: str):
#     start_time = time.time()
#     encrypted_data = encrypt_des(data)
#     end_time = time.time()
#     time_taken = end_time - start_time
#     return {"encrypted_data": encrypted_data, "time_taken": time_taken}

# @app.get("/decrypt_des")
# def decrypt_des_route(data: str):
#     start_time = time.time()
#     decrypted_data = decrypt_des(data)
#     end_time = time.time()
#     time_taken = end_time - start_time
#     return {"decrypted_data": decrypted_data, "time_taken": time_taken}
