from cryptography.fernet import Fernet

# we will be encrypting the below string.

# message = "hello_geeks!@#$%^&*()_+"

# generate a key for encryption and decryption
# You can use fernet to generate
# the key or use random key generator
# here I'm using fernet to generate key
secret_key = Fernet.generate_key()

# Instance the Fernet class with the key
fernet = Fernet(secret_key)


class EncDecr:
    def __init__(self, message):
        self.message = message

    def encrypt(self):
        # then use the Fernet class instance
        # to encrypt the string string must
        # be encoded to byte string before encryption
        enc_message = fernet.encrypt(self.message.encode())
        return enc_message

    # print("original string: ", message)
    # print("encrypted string: ", encMessage)


    def decrypt(self):
        # decrypt the encrypted string with the
        # Fernet instance of the key,
        # that was used for encrypting the string
        # encoded byte string is returned by decrypt method,
        # so decode it to string with decode methods
        dec_message = fernet.decrypt(self.message).decode()
        return dec_message

#print("decrypted string: ", decMessage)

#testing above methods
# message = "hello_geeks!@#$%^&*()_+"
# print(message)
# cl = EncDecr(message)
# encr_message = cl.encrypt()
# print(encr_message)
#
# cl2 = EncDecr(encr_message)
# decr_message = cl2.decrypt()
# print(decr_message)
# if message == decr_message:
#     print("Yes")
# else:
#     print("NO")
