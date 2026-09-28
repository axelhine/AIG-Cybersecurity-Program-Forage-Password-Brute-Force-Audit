'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile

# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    # Handle correct password extract versus incorrect password attempt
    try:
        # Attempt to extract the zip file using each password
        zf_handle.extractall(pwd=password)
        print(f"[+] Found password: {password.decode()}")
        exit(0) # Stop execution once the correct password is found
    except:
        # If wrong, catch the error and keep going smoothly
        pass

def main():
    print("[+] Beginning bruteforce")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            
            # Iterate through password entries in rockyou.txt
            for line in f:
                # Clean the invisible newline characters from the line
                password = line.strip()
                
                # Attempt to extract the zip file using each password
                attempt_extract(zf, password)

    #print("[+] Password not found in list")

# This checks if the script is being run directly. If it is, it automatically kicks off the main() function.
if __name__ == "__main__":
    main()