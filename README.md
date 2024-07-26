# PDF Locker Utility

**PDF Locker Utility** is a command-line tool written in Python that allows users to encrypt PDF files with a password. You can choose to lock selected PDF files or all PDF files within a specified directory.

## Features

- Encrypt individual or all PDF files in a directory with a password.
- User-friendly command-line interface with color-coded messages.
- Password protection for sensitive PDF files.

## Requirements

- Python 3.x
- PyPDF2
- colorama

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/pdf-locker-utility.git
    cd pdf-locker-utility
    ```

2. **Install the required packages**:

    You can install the required packages using pip. Run:

    ```bash
    pip install PyPDF2 colorama
    ```

## Usage

1. **Run the script**:

    ```bash
    python pdf_locker_utility.py
    ```

2. **Follow the prompts**:

    - Enter the path to the directory containing your PDF files.
    - Choose whether you want to lock selected PDFs or all PDFs in the directory.
    - If you choose to lock selected PDFs, enter the numbers corresponding to the files you wish to encrypt.
    - Enter a password to encrypt the selected PDFs.

## Example

```bash
Enter the full path to the directory containing PDF files (e.g., C:\\path\\to\\directory):
C:\Users\YourUsername\Documents\PDFs
Do you want to lock (1) selected PDFs or (2) all PDFs in this directory? Enter 1 or 2: 2
Enter the password to lock the selected PDFs: ********
```


