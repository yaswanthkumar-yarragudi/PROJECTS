import string
import random

def password_strength():
    password = input("Enter the password:").strip()
    num = upp = low = sym = 0
    symbols = string.punctuation
    for c in password:
        if c.isdigit():
            num += 1
        elif c.isupper():
            upp += 1
        elif c.islower():
            low += 1
        elif c in symbols:
            sym += 1
    print(f"\n...Analysing Password...\n\nPassword_length -> {len(password)}\n\nDigits:{num}\nUpper_case:{upp}\nLower_case:{low}\nSymbols:{sym}\n")

    def has_common_pattern(password):
        common_weak_passwords = [
            "123456", "password", "12345678", "qwerty", "123456789",
            "12345", "1234", "111111", "1234567", "dragon", "123123",
            "admin", "welcome", "monkey", "letmein", "abc123", "football", "helloworld"
        ]
        return password.lower() in common_weak_passwords

    def has_sequential_numbers(password, seq_length=4):
        for i in range(len(password) - seq_length + 1):
            window = password[i:i+seq_length]
            if window.isdigit():
                if all(ord(window[j]) == ord(window[0]) + j for j in range(seq_length)):
                    return True
                if all(ord(window[j]) == ord(window[0]) - j for j in range(seq_length)):
                    return True
        return False

    def has_repeated_chars(password, repeat_limit=4):
        for i in range(len(password) - repeat_limit + 1):
            if len(set(password[i:i+repeat_limit])) == 1:
                return True
        return False

    def has_alphabet_sequence(password, seq_length=4):
        for i in range(len(password) - seq_length + 1):
            window = password[i:i+seq_length].lower()
            if all(ord(window[j]) == ord(window[0]) + j for j in range(seq_length)):
                return True
            if all(ord(window[j]) == ord(window[0]) - j for j in range(seq_length)):
                return True
        return False

    def is_password_weak(password):
        if len(password) < 8:
            return True
        if has_common_pattern(password):
            return True
        if has_sequential_numbers(password):
            return True
        if has_repeated_chars(password):
            return True
        if has_alphabet_sequence(password):
            return True
        return False

    
    if is_password_weak(password):
        print("Password Strength --> Weak password! Avoid simple patterns.\n")
    else:
        print("Password Strength --> Strong password!\n")

def generate_password(length):
    if(length<8):
        print("Please ! Choose length >= 8")
    else:
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        numbers = string.digits
        symbols = "!@#$%^&*"
        all_chars = lowercase + uppercase + numbers + symbols
        
        password = []
        password.append(random.choice(lowercase))
        password.append(random.choice(uppercase))
        password.append(random.choice(numbers))
        password.append(random.choice(symbols))
        
        for _ in range(length - 4):
            password.append(random.choice(all_chars))
        
        random.shuffle(password)
        passw=''.join(password)
        print("\nGenerated Password: ",passw,"\n")

while True:
    print("\n" + "_"*50)
    print("---- Password Tool ----")
    print("1. Check password strength (enter 1)")
    print("2. Generate password (enter 2)")
    print("3. Exit (enter 3)")
    print("_"*50)
    
    choice = input("\nEnter your choice (1/2/3): ").strip()
    
    if choice == "1":
        password_strength()
    elif choice == "2":
        while True:
            try:
                length = int(input("Enter the desired password length (minimum 8): "))
                if length >= 8:
                    generate_password(length)
                    break
                else:
                    print("Password length must be at least 8 characters!")
            except ValueError:
                print("Please enter a valid number!")
    elif choice == "3":
        print("\nThank you for using the Password Tool")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")