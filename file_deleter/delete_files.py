import os
import glob
import tkinter as tk
from tkinter import filedialog, messagebox

def delete_files_of_type(folder_path, file_extension):
    """
    Deletes all files of a specific type from a specified folder.

    :param folder_path: Path to the folder
    :param file_extension: File extension of the files to delete (e.g., '.txt')
    """
    # Create the pattern for the specific file type
    search_pattern = os.path.join(folder_path, f"*{file_extension}")

    # Find all files that match the pattern
    files_to_delete = glob.glob(search_pattern)

    # Delete each file found
    for file_path in files_to_delete:
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

def main():
    # Create the main window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask the user for the folder path
    folder = filedialog.askdirectory(title="Select Folder")
    if not folder:
        messagebox.showinfo("Info", "No folder selected. Exiting...")
        return

    # Ask the user for the file extension
    file_extension = tk.simpledialog.askstring("Input", "Enter the file extension (e.g., '.txt'):")
    if not file_extension:
        messagebox.showinfo("Info", "No file extension provided. Exiting...")
        return

    # Confirm deletion
    confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete all {file_extension} files in {folder}?")
    if not confirm:
        messagebox.showinfo("Info", "Operation cancelled. Exiting...")
        return

    # Perform the deletion
    delete_files_of_type(folder, file_extension)
    messagebox.showinfo("Info", "Deletion complete.")

if __name__ == "__main__":
    main()
