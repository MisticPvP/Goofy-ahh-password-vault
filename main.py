import os
import shutil
import random

path = 'Passwords'

def delete_password_line(file_path, line_number):
    # Deletes a specific line from a file at the given line number.
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if line_number < 1 or line_number > len(lines):
        print("Invalid line number.")
        return

    lines.pop(line_number - 1)

    with open(file_path, 'w') as file:
        file.writelines(lines)

def list_passwords():
    # Lists all the passwords in a selected folder.
    print("In which folder are your passwords?")
    folder = input()
    if os.path.exists('./Passwords/' + folder + '/passwords.txt'):
        with open(('./Passwords/' + folder + '/passwords.txt'), 'r') as f:
            print("\nPasswords:\n")
            lines = f.readlines()
            for i, line in enumerate(lines, start=1):
                print(f"{i}. {line.strip()}")
    else:
        print('Folder does not exist.')

def list_folders():
    # Lists all the folders in the Passwords directory.
    dirs = os.listdir("./Passwords/")
    print("\nFolders:\n")
    print(*dirs, sep='\n')

def create_folder():
    # Creates a new folder in the Passwords directory.
    folder_name = ''
    while len(folder_name) == 0:
        print('Enter the name for your new folder:')
        folder_name = input()
        path = 'Passwords/' + folder_name
        try:
            os.makedirs(path)
            print('Successfully created a new folder.')
            return folder_name
        except FileExistsError:
            print('Folder already exists.')
            folder_name = ''
    return None

def store_password():
    # stores a new password in the selected folder.
    print('In which folder do you want to store a password?')
    folder = input()
    print('Enter the password:')
    password = input()
    file_path = 'Passwords/' + folder + '/passwords.txt'
    with open(file_path, 'a') as f:
        f.write(password + '\n')
    print("Successfully added password.")

def delete_folder():
    # Deletes a folder from the Passwords directory.
    print("Enter the folder name to delete:")
    folder = input()
    path = "./Passwords/" + folder
    shutil.rmtree(path)
    print("Folder deleted.")

def delete_password():
    # Deletes a password from the selected folder.
    print("Enter the folder name where the password is located:")
    folder = input()
    folder_path = "./Passwords/" + folder + "/passwords.txt"
    print("Enter the line number of the password to delete:")
    line_number = int(input())
    delete_password_line(folder_path, line_number)
    print("Password deleted.")

def rename_folder():
    # Renames a folder in the Passwords directory.
    print("Enter the folder name you want to rename:")
    old_name = input()
    old_path = "./Passwords/" + old_name
    print("Enter the new folder name:")
    new_name = input()
    new_path = "./Passwords/" + new_name
    try:
        os.rename(old_path, new_path)
        print("Folder renamed successfully.")
    except FileNotFoundError:
        print("Folder does not exist.")

# Create the 'Passwords' directory if it doesn't exist
try:
  os.makedirs(path)
  print('Successfully created a new folder.')
except FileExistsError:
  print('Folder already exists.')
  

    
    
      
  
  





def generate():
    # Generate the password
    password = main1()

    print("Generated password:", password)
    print(
        "Do you want to save the password? (yes/no) (no will close the program) (doing nothing will make it so you can access the storage)"
    )
    answer = input()
    if answer == "yes":
        list_folders()
        print("In which folder do you want to save the password")
        folder = input()
        file_path = 'Passwords/' + folder + '/passwords.txt'
        with open(file_path, 'a') as f:
            f.write(password + '\n')
        print("Successfully added password.")
        main2() 
    elif answer == "no":
        quit()
    else:
        main2()
      
def main1():
    password_length = int(input("Enter the password length: \n"))
    include_symbols = bool(input("Include symbols? (True/False): \n"))
    include_numbers = bool(input("Include numbers? (True/False): \n"))
    include_lowercase = bool(input("Include lowercase letters? (True/False): \n"))
    include_uppercase = bool(input("Include uppercase letters? (True/False): \n"))
    exclude_similar = bool(input("Exclude similar characters? ( e.g. i, l, 1, L, o, 0, O ) (True/False): \n"))
    exclude_ambiguous = bool(input("Exclude ambiguous characters? ( e.g. /[{}()\[\]\/\\'\"`~,;:.<>]/g, ) (True/False): \n"))
    no_duplicate_chars = bool(input("Disallow duplicate characters? (True/False): \n"))
    no_sequential_chars = bool(input("Disallow sequential characters? ( don't use sequential characters, e.g. abc, 789 ) (True/False): \n"))

    characters = ''
    
    if include_symbols:
        characters += '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    if include_numbers:
        characters += '0123456789'
    if include_lowercase:
        characters += 'abcdefghijklmnopqrstuvwxyz'
    if include_uppercase:
        characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if exclude_similar:
        characters = characters.replace('i', '').replace('l', '').replace('1', '').replace('L', '').replace('o', '').replace('0', '')
    if exclude_ambiguous:
        characters = characters.replace('{', '').replace('}', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace('/', '').replace('\\', '').replace('\'', '').replace('\"', '').replace('`', '').replace('~', '').replace(',', '').replace(';', '').replace(':', '').replace('.', '').replace('<', '').replace('>', '')
    
    password = ''
    
    if no_duplicate_chars:
        if password_length > len(characters):
            # Error: Not enough characters to generate password without duplicates
            return None
        
        for _ in range(password_length):
            random_index = random.randint(0, len(characters) - 1)
            password += characters[random_index]
            characters = characters[:random_index] + characters[random_index + 1:]
    elif no_sequential_chars:
        prev_char = ''
        
        for _ in range(password_length):
            random_index = random.randint(0, len(characters) - 1)
            current_char = characters[random_index]
            
            if current_char != prev_char:
                password += current_char
                prev_char = current_char
            else:
                password_length -= 1
    else:
        for _ in range(password_length):
            random_index = random.randint(0, len(characters) - 1)
            password += characters[random_index]
    
    return password
    print(password)
def main2():
    # The main function to run the password vault program.
    while True:
        action = None
        while action not in ['see', 'store', 'change', 'create', 'generate']:
            print(
                'Do you want to see your passwords (or folders(type "see")), store a password (or create a folder(type "store" or "create")), change a password (or folder(type "change")) or generate a password (type "generate")?'
            )
            action = input()

        if action == 'see':
            print("Do you want to see your passwords (enter 'passwords') or folders (enter 'folders')?")
            p_or_f = input()
            if p_or_f == "passwords":
                list_passwords()
            elif p_or_f == "folders":
                list_folders()
            else:
                print("\nInvalid option\n")

        elif action == 'store' or action == 'create':  # Fixed condition check
            F_P = None
            while F_P not in ['folder', 'password']:
                print('Do you want to store a folder or password?')
                F_P = input()
            if F_P == 'folder':
                folder_name = create_folder()
                if folder_name:
                    print('Do you want to put a password in this folder?')
                    answer = input()
                    if answer == 'yes':
                        print('What is the password?')
                        password = input()
                        file_path = 'Passwords/' + folder_name + '/passwords.txt'
                        with open(file_path, 'w') as f:
                            f.write(password + "\n")
                        print('Password added to the folder')
            else:
                store_password()

        elif action == 'change':
            DM = None
            while DM not in ['delete', 'change']:
                print('Do you want to delete or change?')
                DM = input()
            if DM == 'delete':
                print("Do you want to delete a folder or a password?")
                F_P_D = input()
                if F_P_D == "folder":
                    list_folders()
                    delete_folder()
                elif F_P_D == "password":
                    list_folders()
                    delete_password()
            else:
                F_P = None
                while F_P not in ['folder', 'password']:
                    print('Do you want to rename a folder or a password?')
                    F_P = input()
                if F_P == 'folder':
                    rename_folder()

        elif action == 'generate':
            main1()  # Call main1() instead of main2()


print('Hello, what is your name?')
name = input()
print('Good to meet you, ' + name)
print("This is a fork of badozoki's HORRIBLE password vault")


main2()
