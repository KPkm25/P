def calculate_length(number): 
    length = 0 
    while number != 0: 
        length = length + 1 
        number = number // 10 
    return length 

def sum_of_digits(number): 
    remainder = result = 0 
    length = calculate_length(number) 
    while number > 0: 
        remainder = number % 10 
        result = result + (remainder ** length) 
        number = number // 10 
        length = length - 1 
    return result 
def print_disarium(): 
    result = 0 
    print("Disarium numbers between 1 and 100 are \n") 
    for each_number in range(1, 101): 
        result = sum_of_digits(each_number) 
        if result == each_number: 
             print(each_number) 
 
def encrypt_text(input_text, shift_pattern): 
    cipher_result = "" 
    for each_char in input_text: 
        if each_char == " ": 
            cipher_result = cipher_result + each_char 
        elif each_char.isupper(): 
            cipher_result = cipher_result + chr( (ord(each_char) + shift_pattern - 65) % 26 + 65  ) 
        else: 
            cipher_result = cipher_result + chr( (ord(each_char) + shift_pattern - 97) % 26 + 97  )
    return cipher_result 
def user_input(): 
    while True: 
        print("Enter 1 to Print all the Disarium number between 1 and 100  \n") 
        print("Enter 2 to Encrypt the text using Caesar Cipher technique \n") 
        print("Enter 3 to Exit the program \n") 
        choice = int(input()) 
        print("") 
        if choice == 1: 
            print_disarium() 
        elif choice == 2: 
            input_text = input("Enter a text: \n") 
            shift_pattern = int(input("Enter Shift Pattern for encryption:  \n")) 
            encrypted_text = encrypt_text(input_text, shift_pattern) 
            print(f"The encrypted text is {encrypted_text} \n") 
        else: 
            break 
if __name__ == "__main__": 
 user_input()
