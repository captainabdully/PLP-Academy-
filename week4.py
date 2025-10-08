# Read and write a modified version to a new file

filename = input("Enter the filename to read: ")

try:
    # Open and read the file
    with open(filename, 'r') as file:
        content = file.read()

    # Modification: convert content to uppercase
    modified_content = content.upper()

    # Ask for the new filename
    new_filename = input("Enter the new filename: ")

    # Write the modified content to the new file
    with open(new_filename, 'w') as file:
        file.write(modified_content)

    print(f"File has been read successfully and modified to '{new_filename}'.")

# Error handling
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"Something went wrong: {e}")

