#  Password Generator

##  Description
This is a Python program that generates a random password based on user preferences.
The user can choose the password length and decide whether to include numbers and symbols.

## Technologies Used
- Python 3
- random module
- string module

##  How It Works
- The program asks the user to enter the desired password length.
- The user can choose whether to include:
  - Numbers
  - Symbols
- The password is generated using random characters from the selected character set.
- Error handling is implemented using try and except to handle invalid input.

##  Function Explanation
The function `password_generator()`:
- Takes three arguments:
  - Password length
  - Include numbers (True/False)
  - Include symbols (True/False)
- Generates a password using letters, digits, and/or symbols.
- Returns the generated password.

##  How to Run the Program
1. Make sure Python is installed.
2. Run the following command:
   ```bash
   python password_generator.py
   
##  Output Exampe 
- Password with numbers and symbols
   - Enter password length: 6
   - Include numbers? (y/n): y
   - Include symbols? (y/n): y
    
   - Generated Password: cn4YnW
  
- Password with letters only
   - Enter password length: 9
   - Include numbers? (y/n): n
   - Include symbols? (y/n): n
    
   - Generated Password: wrKizYRQZ
 
