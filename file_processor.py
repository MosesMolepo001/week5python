def main():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
        return
    except PermissionError:
        print(f"❌ Error: Permission denied for file '{filename}'.")
        return
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return

    modified_content = content.upper()

    try:
        with open('modified_output.txt', 'w') as new_file:
            new_file.write(modified_content)
        print("✅ File processed successfully. Check 'modified_output.txt'.")
    except Exception as e:
        print(f"❌ Error writing to file: {e}")

if __name__ == "__main__":
    main()
