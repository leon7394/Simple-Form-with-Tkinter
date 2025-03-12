# User Information Form

## Introduction

This is a simple GUI-based application built with `Tkinter` and `CustomTkinter` in Python. The application allows users to input their personal information and save it to an Excel file. Additionally, users can search for their stored information using their National ID.

## Features

- **User-friendly interface** with `CustomTkinter`
- **Save user information** to an Excel file
- **Validate inputs** such as email, phone number, and age
- **Search for stored data** using National ID
- **Dark mode interface** for a modern look

## Technologies Used

- `Python`
- `Tkinter` & `CustomTkinter`
- `pandas` (for handling Excel data)
- `openpyxl` (for working with Excel files)
- `Pillow` (for image handling)
- `re` (for input validation)

## Installation

To run this application, install the required dependencies:

```sh
pip install customtkinter pandas openpyxl pillow
```

## How to Use

1. Run the script:
   ```sh
   python script.py
   ```
2. Enter user details in the provided fields.
3. Click the **Save** button to store the information in an Excel file (`user_info.xlsx`).
4. Click the **Search** button to open a new window and search for data using National ID.

## File Structure

```
.
├── script.py          # Main application file
├── user_info.xlsx     # Generated Excel file storing user data
└── README.md          # Project documentation
```

## Screenshots

(You can add screenshots here)

## License

This project is open-source and available under the MIT License.

---

Happy Coding! 😊

