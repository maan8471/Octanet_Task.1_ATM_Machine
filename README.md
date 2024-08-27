# Octanet_Task-1_ATM_Machine

### Project Description: ATM Machine GUI Application

#### Overview
The ATM Machine GUI Application is a simple, interactive program built using Python's Tkinter library and the Pillow library for image processing. The application simulates an ATM machine, allowing users to perform basic banking operations such as checking balance, crediting and debiting funds, and changing their PIN.

#### Features
1. **Login Screen**: 
   - Users must enter a PIN to access the main menu.
   - The default PIN is set to "1234".

2. **Main Menu**: 
   - After a successful login, users are presented with a menu offering four main options:
     - **Check Balance**: Displays the current balance.
     - **Credit Money**: Allows users to add funds to their account.
     - **Debit Money**: Allows users to withdraw funds from their account.
     - **Change PIN**: Allows users to change their PIN.
     - **Logout**: Returns users to the login screen.

3. **Credit Money**:
   - Users enter an amount to credit.
   - The application updates the balance and provides feedback.

4. **Debit Money**:
   - Users enter an amount to debit.
   - The application checks for sufficient funds before updating the balance and provides feedback.

5. **Change PIN**:
   - Users enter a new 4-digit PIN.
   - The application validates the PIN format and updates it if valid.

6. **Background Image**:
   - The application uses a background image for a more visually appealing interface.
   - The image is loaded using the Pillow library and displayed on all screens.

#### Implementation Details
- **Libraries**:
  - **Tkinter**: For creating the graphical user interface.
  - **Pillow**: For handling and displaying the background image.

- **Classes and Methods**:
  - **ATMApp**: The main class managing the application's functionality.
    - `__init__`: Initializes the application, sets up the initial balance and PIN, and loads the background image.
    - `create_login_screen`: Sets up the login screen with PIN entry.
    - `login`: Validates the entered PIN and transitions to the main menu.
    - `create_main_menu`: Sets up the main menu with available options.
    - `check_balance`: Displays the current balance.
    - `credit_money`: Allows the user to input an amount to credit and updates the balance.
    - `debit_money`: Allows the user to input an amount to debit, checking for sufficient funds before updating the balance.
    - `change_pin`: Allows the user to enter and submit a new PIN.
    - `clear_screen`: Clears the current screen of widgets.
    - `add_background`: Adds the background image to the current screen.

- **Error Handling**:
  - Ensures that entered amounts are valid numbers and handle errors such as insufficient funds or invalid PIN formats.

#### Usage
1. **Run the Application**: Execute the script to start the ATM application.
2. **Login**: Enter the default PIN "1234" or a previously set PIN to access the main menu.
3. **Navigate**: Choose options from the main menu to check balance, credit or debit money, change PIN, or logout.
4. **Background**: The application features a background image for enhanced visual appeal.

#### Dependencies
- Python 3.x
- Tkinter (usually included with Python standard library)
- Pillow (install via pip with `pip install pillow`)

This project demonstrates a basic yet functional ATM interface, showcasing core concepts in GUI programming, user interaction, and state management within a Python application.
