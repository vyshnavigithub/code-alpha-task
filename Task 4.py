import os
import shutil

def organize_files(directory):
   
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Create a folder name based on the file extension
        if file_extension:
            folder_name = file_extension[1:].capitalize()  # e.g., ".txt" -> "Txt"
        else:
            folder_name = "Unknown"

        # Create the folder if it doesn't exist
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        # Move the file into the corresponding folder
        shutil.move(file_path, os.path.join(folder_path, filename))

    print(f"Files in '{directory}' have been organized by type.")

if __name__ == "__main__":
    directory = input("Enter the directory path to organize: ")
    organize_files(directory)
