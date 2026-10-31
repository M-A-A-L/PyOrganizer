import fileOrganizer

folder = input("Enter the directory you want to organize: ")
generate_a_log = input("Want to generate a log? (Y/n): ").lower().startswith("y")
if fileOrganizer.is_valid_folder(folder):
    modifications = fileOrganizer.organize_folder(folder)
    if modifications:
        if (generate_a_log):
            fileOrganizer.generate_log(folder, modifications)
        print("organized directory")
    else:
        print("No files to organize. (T-T)")
else:
    print("ERROR: Invalid directory")