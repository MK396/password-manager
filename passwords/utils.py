from cryptography.fernet import Fernet
from django.conf import settings
import base64

# W prawdziwym projekcie klucz generuje się raz i trzyma w .env
# Na potrzeby prezentacji użyjemy klucza opartego na SECRET_KEY z Django
def get_cipher():
    key = base64.urlsafe_b64encode(settings.SECRET_KEY[:32].encode())
    return Fernet(key)

def encrypt_password(plain_text):
    cipher = get_cipher()
    return cipher.encrypt(plain_text.encode()).decode()

def decrypt_password(cipher_text):
    cipher = get_cipher()
    try:
        return cipher.decrypt(cipher_text.encode()).decode()
    except:
        return cipher_text # Jeśli nie zaszyfrowane, zwróć oryginał