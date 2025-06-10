# Importing necessary libraries
import os  # For interacting with the operating system
import zipfile  # For handling zip files
import shutil  # For file operations like copy and delete
from pathlib import Path  # For working with file system paths

# Defining folder paths
ZIPPED_DIR = Path("ZippedData")  # Folder where zip files are stored
DATA_DIR = Path("Data")  # Folder where extracted data will be saved

# Checking if 'ZippedData' folder exists and contains any .zip files
if not ZIPPED_DIR.exists() or not any(ZIPPED_DIR.glob("*.zip")):
    print("Oops, no 'ZippedData/' folder or no zip files in there.")
    print("Pop your zip files into 'ZippedData/' and try again.")
    exit(1)  # Exit the program if no zip files found

# Creating the 'Data' folder if it doesn't already exist
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Looping through all .zip files in the ZippedData folder
for zip_path in ZIPPED_DIR.glob("*.zip"):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extract contents into a temporary folder inside XippedData
        temp_extract_path = ZIPPED_DIR / "temp_extracted"
        zip_ref.extractall(temp_extract_path)

        # Going through all files in the extracted folder
        for root, dirs, files in os.walk(temp_extract_path):
            for file in files:
                # copying files with specific extensions 
                if file.endswith((".csv", ".json", ".xlsx", ".xls", ".sqlite", ".db", ".txt")):
                    src_file = Path(root) / file  # Path to source file
                    dest_file = DATA_DIR / file  # Path to destination

                    # Copy the file if it doesn't already exist in 'Data'
                    if not dest_file.exists():
                        shutil.copy2(src_file, dest_file)  # Copy file with metadata
                        print(f"Got it: {file}")
                    else:
                        print(f"Skipped (already there): {file}")

        # Remove the temporary folder after processing each zip file
        shutil.rmtree(temp_extract_path)

# Print message once all files are processed and copied
print("Done! All data files are now in the Data folder.")

