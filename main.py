import PyPDF2
import getpass
from colorama import Fore, Style, init
import os

# Initialize colorama for colored output with auto-reset for color codes
init(autoreset=True)

# Function to lock a PDF file with a password
def lock_pdf(input_file, password):
    """
    Encrypts a PDF file with a given password and saves it.
    
    Args:
        input_file (str): Path to the PDF file to be encrypted.
        password (str): Password to encrypt the PDF.
    
    Returns:
        bool: True if the PDF was successfully encrypted, False otherwise.
    """
    try:
        # Open the input PDF file in binary read mode
        with open(input_file, 'rb') as file:
            # Create a PdfReader object to read the PDF
            pdf_reader = PyPDF2.PdfReader(file)

            # Create a PdfWriter object to write the encrypted PDF
            pdf_writer = PyPDF2.PdfWriter()

            # Iterate over all the pages in the original PDF
            for page_num in range(len(pdf_reader.pages)):
                # Add each page to the PdfWriter object
                pdf_writer.add_page(pdf_reader.pages[page_num])

            # Encrypt the PDF with the provided password
            pdf_writer.encrypt(password)

            # Write the encrypted PDF back to the file
            with open(input_file, 'wb') as output_file:
                pdf_writer.write(output_file)
        
        # Return True if encryption and writing were successful
        return True
    except FileNotFoundError:
        # Handle the case where the input file is not found
        print(f"{Fore.RED}[-] Error: The file '{input_file}' was not found.")
        return False
    except Exception as e:
        # Handle any other unexpected errors
        print(f"{Fore.RED}[-] An unexpected error occurred: {e}")
        return False

# Function to list PDF files in the given directory
def list_pdf_files(directory):
    """
    Lists all PDF files in a given directory.
    
    Args:
        directory (str): Path to the directory to search.
    
    Returns:
        list: List of PDF file paths in the directory.
    """
    pdf_files = [f for f in os.listdir(directory) if f.lower().endswith('.pdf')]
    return [os.path.join(directory, f) for f in pdf_files]

# Main function to interact with the user
def main():
    """
    Main function to handle user interactions for encrypting PDFs.
    """
    # Display the header for the utility
    print(f"{Fore.CYAN}{Style.BRIGHT}PDF Locker Utility")
    print(f"{Fore.CYAN}{'=' * 20}")

    while True:
        # Prompt the user to enter the path of the directory containing PDFs
        directory = input(f"{Fore.YELLOW}Enter the full path to the directory containing PDF files (e.g., C:\\path\\to\\directory): ").strip()

        # Check if the directory exists
        if not os.path.isdir(directory):
            print(f"{Fore.RED}[-] Error: The directory '{directory}' does not exist. Please check the path and try again.")
            continue  # Ask for the input again

        # List all PDF files in the directory
        pdf_files = list_pdf_files(directory)

        # Check if there are PDF files in the directory
        if not pdf_files:
            print(f"{Fore.RED}[-] No PDF files found in the directory '{directory}'.")
            continue  # Ask for the input again

        # Display the list of PDF files to the user
        print(f"{Fore.GREEN}[i] Found the following PDF files:")
        for idx, pdf_file in enumerate(pdf_files, start=1):
            print(f"{Fore.YELLOW}{idx}. {os.path.basename(pdf_file)}")

        # Prompt the user to select an option
        while True:
            try:
                choice = input(f"{Fore.YELLOW}Do you want to lock (1) selected PDFs or (2) all PDFs in this directory? Enter 1 or 2: ").strip()
                
                if choice == '1':
                    # Prompt the user to select multiple PDF files
                    while True:
                        try:
                            # Get user input and split by comma to allow multiple selections
                            selections = input(f"{Fore.YELLOW}Enter the numbers of the PDF files to lock, separated by commas (e.g., 1,3,5): ").strip()
                            selected_indices = [int(x) for x in selections.split(',')]

                            # Validate the selections
                            if all(1 <= idx <= len(pdf_files) for idx in selected_indices):
                                selected_pdfs = [pdf_files[idx - 1] for idx in selected_indices]
                                break
                            else:
                                print(f"{Fore.RED}[-] Invalid numbers. Please enter numbers between 1 and {len(pdf_files)}.")
                        except ValueError:
                            print(f"{Fore.RED}[-] Invalid input. Please enter valid numbers separated by commas.")

                    # Encrypt selected PDFs
                    pdf_files_to_lock = selected_pdfs
                
                elif choice == '2':
                    # Encrypt all PDFs in the directory
                    pdf_files_to_lock = pdf_files
                
                else:
                    print(f"{Fore.RED}[-] Invalid choice. Please enter 1 or 2.")
                    continue
                
                break

            except ValueError:
                print(f"{Fore.RED}[-] Invalid input. Please enter 1 or 2.")

        # Prompt the user to enter the password for encryption
        password = getpass.getpass(f"{Fore.YELLOW}Enter the password to lock the selected PDFs: ").strip()

        # Inform the user that the process is ongoing
        print(f'{Fore.GREEN}[!] Please hold on for a few seconds...')
        
        # Encrypt all selected PDFs or all PDFs in the directory
        successes = 0
        failures = 0
        for pdf in pdf_files_to_lock:
            if lock_pdf(pdf, password):
                successes += 1
            else:
                failures += 1

        # Provide feedback on the result of the operation
        if successes > 0:
            print(f"{Fore.GREEN}[+] Successfully locked {successes} PDF(s).")
        if failures > 0:
            print(f"{Fore.RED}[-] Failed to lock {failures} PDF(s).")

        # Print the current working directory for user reference
        print(f"{Fore.YELLOW}[i] Current working directory: {os.getcwd()}")
        print(f"{Fore.CYAN}{'=' * 20}")

        # Ask the user if they want to lock another set of PDFs or exit
        while True:
            # Accept 'y', 'yes', 'n', or 'no' for simplicity
            choice = input(f"{Fore.YELLOW}Do you want to lock another set of PDFs? (y/n): ").strip().lower()
            if choice in {'y', 'yes'}:
                # Continue the loop to process another set of PDFs
                break
            elif choice in {'n', 'no'}:
                # Exit the program and thank the user
                print(f"{Fore.CYAN}{Style.BRIGHT}Thank you for using PDF Locker Utility")
                return
            else:
                # Handle invalid input
                print(f"{Fore.RED}[-] Invalid input. Please enter 'y' for yes or 'n' for no.")

# Entry point of the script
if __name__ == "__main__":
    main()
