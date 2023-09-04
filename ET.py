import base64
import os
import sys
import time

# Define color codes as variables
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RESET = "\033[0m"

# Define more color options
COLOR_BLUE = "\033[94m"
COLOR_PURPLE = "\033[95m"
COLOR_CYAN = "\033[96m"
CUSTOM_COLOR = "\033[38;2;52;235;143m"
CUSTOM_COLOR2 = "\033[38;2;235;52;155m"  # #eb349b

# Additional hex color codes
CUSTOM_COLOR3 = "\033[38;2;255;94;0m"  # #ff5e00
CUSTOM_COLOR4 = "\033[38;2;238;255;0m"  # #eeff00
CUSTOM_COLOR5 = "\033[38;2;0;208;255m"  # #00d0ff

os.system("clear" if os.name == "posix" else "cls")  # Clear the screen


def charging_effect(repetitions=3):
    for _ in range(repetitions):
        sys.stdout.write(f"\r{COLOR_PURPLE}Loading please wait: |")
        sys.stdout.flush()
        time.sleep(0.2)

        sys.stdout.write(f"\r{COLOR_PURPLE}Loading please wait: /")
        sys.stdout.flush()
        time.sleep(0.3)

        sys.stdout.write(f"\r{COLOR_PURPLE}Loading please wait: -")
        sys.stdout.flush()
        time.sleep(0.2)

        sys.stdout.write(f"\r{COLOR_PURPLE}Loading please wait: \\")
        sys.stdout.flush()
        time.sleep(0.3)


charging_effect(3)  # Call the function with 3 repetitions

os.system("clear" if os.name == "posix" else "cls")  # Clear the screen

ascii_art = f"""
{COLOR_RED}$$$$$$$$\                                     $$\ $$\                          $$$$$$$$\                                $$\ {COLOR_RESET}                 
{CUSTOM_COLOR3}$$  _____|                                    $$ |\__|                         \__$$  __|                               $$ |   {COLOR_RESET}               
{COLOR_YELLOW}$$ |      $$$$$$$\   $$$$$$$\  $$$$$$\   $$$$$$$ |$$\ $$$$$$$\   $$$$$$\          $$ |$$\  $$\  $$\  $$$$$$\   $$$$$$\  $$ |  $$\  $$$$$$$\ {COLOR_RESET}  
{CUSTOM_COLOR4}$$$$$\    $$  __$$\ $$  _____|$$  __$$\ $$  __$$ |$$ |$$  __$$\ $$  __$$\ $$$$$$\ $$ |$$ | $$ | $$ |$$  __$$\  \____$$\ $$ | $$  |$$  _____| {COLOR_RESET}  
{COLOR_GREEN}$$  __|   $$ |  $$ |$$ /      $$ /  $$ |$$ /  $$ |$$ |$$ |  $$ |$$ /  $$ |\______|$$ |$$ | $$ | $$ |$$$$$$$$ | $$$$$$$ |$$$$$$  / \$$$$$$\  {COLOR_RESET}  
{COLOR_CYAN}$$ |      $$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |        $$ |$$ | $$ | $$ |$$   ____|$$  __$$ |$$  _$$<   \____$$\ {COLOR_RESET}  
{COLOR_BLUE}$$$$$$$$\ $$ |  $$ |\$$$$$$$\ \$$$$$$  |\$$$$$$$ |$$ |$$ |  $$ |\$$$$$$$ |        $$ |\$$$$$\$$$$  |\$$$$$$$\ \$$$$$$$ |$$ | \$$\ $$$$$$$  | {COLOR_RESET}  
{COLOR_PURPLE}\________|\__|  \__| \_______| \______/  \_______|\__|\__|  \__| \____$$ |        \__| \_____\____/  \_______| \_______|\__|  \__|\_______/ 
                                                                $$\   $$ |                                                                  
                                                                \$$$$$$  |                                                                  
                                                                 \______/                                                                   
"""


# Encoding function for Hex
def encode_hex(text):
    return text.encode().hex()


# Decoding function for Hex
def decode_hex(hex_text):
    try:
        decoded_text = bytes.fromhex(hex_text).decode()
        return decoded_text
    except ValueError:
        return "Invalid Hex input."


# Encoding function for Base64
def encode_base64(text):
    return base64.b64encode(text.encode()).decode()


# Decoding function for Base64
def decode_base64(base64_text):
    try:
        return base64.b64decode(base64_text).decode()
    except ValueError:
        return "Invalid Base64 input."


# Hex color viewer function
def display_colored_text(hex_color, text):
    r, g, b = hex_to_rgb(hex_color)
    colored_text = f"\x1b[38;2;{r};{g};{b}m{text}{COLOR_RESET}"
    print(colored_text)


# Hex to RGB conversion function
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return r, g, b


# Encoding function for UTF-8
def encode_text_to_utf8(text):
    encoded_text = text.encode("utf-8")
    return encoded_text.hex()


# Encoding function for UTF-16
def encode_text_to_utf16(text):
    encoded_text = text.encode("utf-16")
    return encoded_text.hex()


# Encoding function for UTF-32
def encode_text_to_utf32(text):
    encoded_text = text.encode("utf-32")
    return encoded_text.hex()


# Decoding function for UTF-8
def decode_utf8_to_text(hex_string):
    try:
        decoded_text = bytes.fromhex(hex_string).decode("utf-8")
        return decoded_text
    except UnicodeDecodeError:
        return "Error: Unable to decode."


# Decoding function for UTF-16
def decode_utf16_to_text(hex_string):
    try:
        decoded_text = bytes.fromhex(hex_string).decode("utf-16")
        return decoded_text
    except UnicodeDecodeError:
        return "Error: Unable to decode."


# Decoding function for UTF-32
def decode_utf32_to_text(hex_string):
    try:
        decoded_text = bytes.fromhex(hex_string).decode("utf-32")
        return decoded_text
    except UnicodeDecodeError:
        return "Error: Unable to decode."


# About function
def about():
    os.system("clear" if os.name == "posix" else "cls")  # Clear the screen
    print(f"{CUSTOM_COLOR}EncodingTweaks - About{COLOR_RESET}")
    print("This is EncodingTweaks, a simple text encoding and color display tool.")
    print("It allows you to encode and decode text in various formats, such as Hex and Base64.")
    print("You can also display text in custom colors using hex color codes.")
    print("Additionally, EncodingTweaks supports encoding and decoding text in different UTF formats.")
    print(f"This project is LICENSED MIT BY {COLOR_CYAN}Independent-coder{COLOR_RESET} on Github")
    input("Press Enter to return to the main menu.")


# Main menu function
def main_menu():
    while True:
        os.system("clear" if os.name == "posix" else "cls")  # Clear the screen

        print(ascii_art)
        print(f"{CUSTOM_COLOR}EncodingTweaks - Main Menu{COLOR_RESET}")
        print(f"{COLOR_CYAN}1. Encode Text to Hex{COLOR_RESET}")
        print(f"{COLOR_BLUE}2. Decode Hex to Text{COLOR_RESET}")
        print(f"{COLOR_PURPLE}3. Encode Text to Base64{COLOR_RESET}")
        print(f"{COLOR_YELLOW}4. Decode Base64 to Text{COLOR_RESET}")
        print(f"{CUSTOM_COLOR2}5. Display Text in Hex Color{COLOR_RESET}")
        print(f"{CUSTOM_COLOR3}6. Encode/Decode UTF-8, UTF-16, UTF-32{COLOR_RESET}")
        print(f"{COLOR_GREEN}7. About{COLOR_RESET}")  # Add the "About" option
        print(f"{COLOR_RED}8. Exit{COLOR_RESET}")  # Adjust the exit option
        choice = input(f"{CUSTOM_COLOR2}Enter your choice: {COLOR_RESET}")

        if choice == "1":
            text = input("Enter text to encode: ")
            encoded_text = encode_hex(text)
            print(f"Encoded: {encoded_text}")
            time.sleep(2)  # Pause for 2 seconds
        elif choice == "2":
            hex_text = input("Enter hex to decode: ")
            decoded_text = decode_hex(hex_text)
            print(f"Decoded: {decoded_text}")
            time.sleep(2)  # Pause for 2 seconds
        elif choice == "3":
            text = input("Enter text to encode to Base64: ")
            encoded_text = encode_base64(text)
            print(f"Encoded to Base64: {encoded_text}")
            time.sleep(2)  # Pause for 2 seconds
        elif choice == "4":
            base64_text = input("Enter Base64 to decode to Text: ")
            decoded_text = decode_base64(base64_text)
            print(f"Decoded from Base64: {decoded_text}")
            time.sleep(2)  # Pause for 2 seconds
        elif choice == "5":
            hex_color = input("Enter a hex color (e.g., #FF0000 for red): ")
            text_to_display = input("Enter text to display in the specified color: ")
            display_colored_text(hex_color, text_to_display)
            time.sleep(2)  # Pause for 2 seconds
        elif choice == "6":
            utf_choice = input("Choose UTF (1 for encoding, 2 for decoding): ")
            text = input("Enter text: ")
            if utf_choice == "1":
                utf_encoding_choice = input(
                    "Choose UTF Encoding (1 for UTF-8, 2 for UTF-16, 3 for UTF-32): "
                )
                if utf_encoding_choice == "1":
                    print("UTF-8 encoded:", encode_text_to_utf8(text))
                    time.sleep(5)
                elif utf_encoding_choice == "2":
                    print("UTF-16 encoded:", encode_text_to_utf16(text))
                    time.sleep(5)

                elif utf_encoding_choice == "3":
                    print("UTF-32 encoded:", encode_text_to_utf32(text))
                    time.sleep(5)
                else:
                    print(f"{COLOR_RED}Invalid UTF encoding choice.{COLOR_RESET}")
                    time.sleep(2)
            elif utf_choice == "2":
                utf_decoding_choice = input(
                    "Choose UTF Decoding (1 for UTF-8, 2 for UTF-16, 3 for UTF-32): "
                )
                hex_text = input("Enter UTF hex to decode: ")
                if utf_decoding_choice == "1":
                    decoded_text = decode_utf8_to_text(hex_text)
                    print(f"Decoded from UTF-8: {decoded_text}")
                    time.sleep(5)
                elif utf_decoding_choice == "2":
                    decoded_text = decode_utf16_to_text(hex_text)
                    print(f"Decoded from UTF-16: {decoded_text}")
                    time.sleep(5)
                elif utf_decoding_choice == "3":
                    decoded_text = decode_utf32_to_text(hex_text)
                    print(f"Decoded from UTF-32: {decoded_text}")
                    time.sleep(5)
                else:
                    print(f"{COLOR_RED}Invalid UTF decoding choice.{COLOR_RESET}")
                    time.sleep(2)
            else:
                print(f"{COLOR_RED}Invalid UTF choice.{COLOR_RESET}")
                time.sleep(2)
        elif choice == "7":
            about()  # Call the "About" function
        elif choice == "8":
            os.system("clear" if os.name == "posix" else "cls")  # Clear the screen
            print("Exiting EncodingTweaks. Goodbye!")
            time.sleep(2)
            os.system("clear" if os.name == "posix" else "cls")  # Clear the screen
            break
        else:
            print(
                f"{COLOR_RED}Invalid choice. Please select a valid option.{COLOR_RESET}"
            )
            time.sleep(2)


if __name__ == "__main__":
    main_menu()
