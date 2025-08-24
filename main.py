#This file belongs to Gaurav Mathpal

#!/usr/bin/env python3

def menu():
    """Main menu loop for the program"""
    print("\n\n--- SECRET CODE GENERATOR ---\n")

    while True:
        # Ask user what they want to do
        inp = str(input("\nPress: en to ENCODE, de to DECODE, ex to EXIT\n> "))

        if inp in ["en", "En", "EN"]:
            encode()
        elif inp in ["de", "De", "DE"]:
            decode()
        elif inp in ["ex", "Ex", "EX"]:
            print("\nClosing SECRET CODE GENERATOR... Goodbye!\n")
            break
        else:
            print("\n[!] Please read the instructions carefully.\n")


def encode():
    """Encodes a given message by shifting letters forward"""
    while True:
        choice1 = str(input("Large data encryption [L] or just a text? [S]: "))
        if(choice1=='s' or choice1=='S'):

            print("\n--- ENCODE MODE ---\n")
            str1 = str(input("Enter the message you want to encode:\n> ")) 
            shift = int(input("Enter a shift number: ")) % 26
            str2 = ""
            
            # Loop through every character
            for i in str1:
                if i.islower():   # lowercase letters
                    if i.isalpha():
                        str2 += chr((ord(i)-ord('a')+shift) % 26 + ord('a'))
                    else:
                        str2 += i
                else:             # uppercase letters
                    if i.isalpha():
                        str2 += chr((ord(i)-ord('A')+shift) % 26 + ord('A'))
                    else:
                        str2 += i

            # Print encoded message
            print("\nEncoded Message:\n" + str2 + "\n")
            
            # Ask user if they want to go back
            choice = str(input("Go back to menu? [Y/N]: "))
            if choice in ['y', 'Y']:
                break
        
        elif(choice1=='l' or choice1=='L'):
            shift = int(input("Enter a shift number: ")) % 26
            str2=""

            try:
                with open("decryptfile.txt", "r") as file:
                    str1=file.read()
            except FileNotFoundError:
                print("file not found")

            for i in str1:
                if i.islower():   # lowercase letters
                    if i.isalpha():
                        str2 += chr((ord(i)-ord('a')+shift) % 26 + ord('a'))
                    else:
                        str2 += i
                else:             # uppercase letters
                    if i.isalpha():
                        str2 += chr((ord(i)-ord('A')+shift) % 26 + ord('A'))
                    else:
                        str2 += i
            try:
                with open("encryptfile.txt", "w") as file:
                    file.write(str2)
            except FileNotFoundError:
                print("file not found")

            print("Check the encrypt file, it has the encrypted text.")
            
            # Ask user if they want to go back
            choice = str(input("Go back to menu? [Y/N]: "))
            if choice in ['y', 'Y']:
                break


def decode():
    """Decodes a given message by shifting letters backwards"""
    while True:
        choice1 = str(input("Large data decryption [L] or just a text? [S]: "))
        if(choice1=='s' or choice1=='S'):

            print("\n--- DECODE MODE ---\n")
            str1 = str(input("Enter the message you want to decode:\n> ")) 
            shift = int(input("Enter a shift number: ")) % 26
            str2 = ""
            
            # Loop through every character
            for i in str1:
                if i.islower():   # lowercase letters
                    if i.isalpha():
                        str2 += chr(ord('z') - ((ord('z')-ord(i)+shift) % 26))
                    else:
                        str2 += i
                else:             # uppercase letters
                    if i.isalpha():
                        str2 += chr(ord('Z') - ((ord('Z')-ord(i)+shift) % 26))

                    else:
                        str2 += i

            # Print encoded message
            print("\n Decoded Message:\n" + str2 + "\n")
            
            # Ask user if they want to go back
            choice = str(input("Go back to menu? [Y/N]: "))
            if choice in ['y', 'Y']:
                break
        
        elif(choice1=='l' or choice1=='L'):
            shift = int(input("Enter a shift number: ")) % 26
            str2 = ""

            try:
                with open("encryptfile.txt", "r") as file:
                    str1=file.read()
            except FileNotFoundError:
                print("file not found")

            for i in str1:
                if i.islower():   # lowercase letters
                    if i.isalpha():
                        str2 += chr(ord('z') - ((ord('z')-ord(i)+shift) % 26))
                    else:
                        str2 += i
                else:             # uppercase letters
                    if i.isalpha():
                        str2 += chr(ord('Z') - ((ord('Z')-ord(i)+shift) % 26))
                    else:
                        str2 += i
            try:
                with open("decryptfile.txt", "w") as file:
                    file.write(str2)
            except FileNotFoundError:
                print("file not found")

            print("Check the decrypted file, it has the decrypted text.")
            
            # Ask user if they want to go back
            choice = str(input("Go back to menu? [Y/N]: "))
            if choice in ['y', 'Y']:
                break

menu()