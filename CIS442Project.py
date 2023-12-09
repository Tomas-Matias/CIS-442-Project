import os

def fileSignature(filePath, hex):
    # Opens the file patch and reads the content within and brings the hex value length down to match them with the library I have in main()   
    with open(filePath, 'rb') as file:
        content = file.read(len(max(hex, key=len)) // 2)
        return any(content == bytes.fromhex(hex) for hex in hex)

def ListMaskedFiles(folderPath, signatures):
    masqueraded_files = []
    # Loops through the files and roots within the Folder Path entered by the user
    for root, _, files in os.walk(folderPath):
        # Loops through the files themselvves
        for file in files:
            # Brings together the crrent directory and any files within it
            filePath = os.path.join(root, file)
            # Loops through the signatures dictionary to match ext of the files and the expected extensions
            for info in signatures.values():
                # Makes the extension lower case and matches it with file_extension value in the dictionary 
                if file.lower().endswith(tuple(ext.lower() for ext in info["file_extension"])):
                    # Appends the name of the file to the list if they do not match the hex_values expected
                    if not fileSignature(filePath, info["hex_values"]):
                        masqueraded_files.append(filePath)
                        break
    
    return masqueraded_files


def main():
    # Dictionary of signatures
    signatures = {
        "JPEG": {
            "description": "JPEG raw or in the JFIF or Exif file format",
            "file_extension": ["jpg", "jpeg"],
            "hex_values": ["FFD8FFE1", "FFD8FFE0", "FFD8FFDB"],  
            "offset": "0",
        },
        ".PNG": {
            "description": "Image encoded in the Portable Network Graphics format",
            "file_extension": ["png"],
            "hex_values": ["89504E47"],
            "offset": "0",
        },
        "PK..": {
            "description": "ZIP file format and formats based on it, such as JAR, ODF, OOXML",
            "file_extension": ["docx", "zip", "jar", "odt", "ods", "odp", "xlsx", "pptx", "vsdx", "apk"],
            "hex_values": ["504B0304"],
            "offset": "0",
        },
        "PDF": {
            "description": "Adobe Portable Document Format",
            "file_extension": ["pdf"],
            "hex_values": ["25504446"],
            "offset": "0",
         },
        "GIF": {
            "description": "Graphics Interchange Format",
            "file_extension": ["gif"],
            "hex_values": ["47494638"],
            "offset": "0",
        },
        "MP3": {
            "description": "MPEG Audio Layer III (MP3) file",
            "file_extension": ["mp3"],
            "hex_values": ["494433"],
            "offset": "0",
        },
        "DOC": {
            "description": "Microsoft Word document",
            "file_extension": ["doc"],
            "hex_values": ["D0CF11E0"],
            "offset": "0",
        },
        "XLS": {
            "description": "Microsoft Excel spreadsheet",
            "file_extension": ["xls"],
            "hex_values": ["D0CF11E0"],
            "offset": "0",
        },
        "MP4": {
            "description": "MPEG-4 Part 14 multimedia format",
            "file_extension": ["mp4"],
            "hex_values": ["66747970", "4D534E56"],
            "offset": "4",
        },
    }


    # Get folder path from user
    folderPath = input("Enter the folder path that you would like to check for Masqueraded Files: ")

    # Check to see if path exists
    while not os.path.exists(folderPath) or not os.path.isdir(folderPath):
        print("Invalid folder path. Please enter a valid path.")
        folderPath = input("Enter the folder path that you would like to check for Masqueraded Files: ")

    # List masqueraded files
    masqueraded_files = ListMaskedFiles(folderPath, signatures)

    # Print the results
    if masqueraded_files:
        print("Masqueraded Files:")
        for filePath in masqueraded_files:
            print(filePath)
    else:
        print("No masqueraded files found.")

if __name__ == "__main__":
    main()
