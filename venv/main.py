from modules.hash import hash_file,verify_integrity
from modules.encryption import aes_ed,rsa_ed
from modules.password import check_strength,hash_pw,verify_password
from getpass import getpass


def menu():
    print("\nSelect operation: ")
    print("1. Hash file")
    print("2. Check file integrity")
    print("3. AES Encrypt/Decrypt")
    print("4. RSA Encrypt/Decrypt")
    print("5. Password Manager")
    print("0. Exit")

print("""
============================================================
            🔐 CYBER SECURITY TOOLKIT v1.0 🔐
============================================================

Welcome to the Cyber Security Toolkit!

This toolkit provides essential cybersecurity utilities
for hashing, encryption, decryption, file integrity
and password management and verification.

⚠️  Use this toolkit responsibly and only on systems
    you own or have permission to test.

============================================================
""")

while True:
    menu()
    choice = input("Enter choice (0-5) : ")
    if choice == "0":
        break
    elif choice == "1":
        file_path = input("Enter file path: ")
        print("\nSHA Hash of file is : ", hash_file(file_path))
    elif choice == "2":
        file_path1 = input("Enter file path 1 :")
        file_path2= input("Enter file path 2 :")
        print(verify_integrity(file_path1,file_path2))

    elif choice == "3":
        message = input("Enter message: ")
        key, ciphertext,plaintext,= aes_ed(message)
        print("AES key: ",key)
        print("AES ciphertext: ",ciphertext)
        print("AES plaintext: ",plaintext)

    elif choice == "4":
        message = input("Enter message : ")
        ciphertext,plaintext = rsa_ed(message)
        print("RSA message , encrypt with a public key: ",ciphertext)
        print("RSA message, decrypt with private key: ",plaintext)

    elif choice == "5":
         while True:
            password1 =  getpass("Enter a password to check strength:")
            print(check_strength(password1))
            if check_strength(password1).startswith("Weak"):
                print("Please Choose a strong password.")
            else:
                break

            hashed_password = hash_pw(password1)
            print("Hashed password: ",hashed_password)
            attempt = getpass("Re-enter the password to verify : ")
            print(verify_password(attempt,hashed_password))
    else:
        print("Invalid choice.")



