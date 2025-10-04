import os

def print_Logo():
    print(
        '''
     __  __ _       _   _ ___    ____      _ _           _   _             
    |  \\/  (_)_ __ | | | |_ _|  / ___|___ | | | ___  ___| |_(_) ___  _ __  
    | |\\/| | | '_ \\| | | || |  | |   / _ \\| | |/ _ \\/ __| __| |/ _ \\| '_ \\ 
    | |  | | | | | | |_| || |  | |__| (_) | | |  __/ (__| |_| | (_) | | | |
    |_|  |_|_|_| |_|\\___/|___|  \\____\\___/|_|_|\\___|\\___|\\__|_|\\___/|_| |_|
                                                                  - cttynul
        '''
    )

def get_sd_card_path():
    while True:
        path = input("Enter the SD card path [E:\\]: ").strip()
        if os.path.exists(path):
            return path
        else:
            print("Invalid path. Please try again.")

def get_collection_name():
    return input("Enter the collection name [Pokemon]: ").strip()

def get_search_parameters():
    parameters = input("Enter search parameters separated by commas [pokemon,pkmn]: ").strip()
    return [param.strip() for param in parameters.split(',')]

def get_exclude_parameters():
    parameters = input("Enter exclude parameters separated by commas (leave empty if none) [hack,hck]: ").strip()
    if not parameters:
        return []
    return [param.strip() for param in parameters.split(',')]

def find_files(sd_card_path, search_parameters, exclude_parameters):
    roms_path = os.path.join(sd_card_path, "Roms")
    found_files = []

    if not os.path.exists(roms_path):
        print(f"Roms folder not found at: {roms_path}")
        return found_files

    for root, dirs, files in os.walk(roms_path):
        # Exclude .res folders
        dirs[:] = [d for d in dirs if d != ".res"]

        for file in files:
            file_path = os.path.join(root, file)
            file_name_lower = file.lower()
            if all(param.lower() in file_name_lower for param in search_parameters) and not any(exclude_param.lower() in file_name_lower for exclude_param in exclude_parameters):
                # Replace backslashes with forward slashes and remove sd_card_path
                relative_path = file_path.replace(sd_card_path, "/").replace(os.path.sep, "/")
                found_files.append(relative_path)

    return found_files

def create_collection_file(sd_card_path, collection_name, search_parameters, exclude_parameters, found_files):
    collections_path = os.path.join(sd_card_path, "Collections")
    if not os.path.exists(collections_path):
        try:
            os.makedirs(collections_path)
            print(f"Created 'Collections' folder at: {collections_path}")
        except Exception as e:
            print(f"Error creating 'Collections' folder: {e}")
            return

    file_path = os.path.join(collections_path, f"{collection_name}.txt")
    try:
        with open(file_path, 'a') as file:
            for found_file in found_files:
                file.write(f"{found_file}\n")
        print(f"Collection file created successfully at: {file_path}")
    except Exception as e:
        print(f"Error creating collection file: {e}")

if __name__ == "__main__":
    print_Logo()
    sd_card_path = get_sd_card_path()
    collection_name = get_collection_name()
    search_parameters = get_search_parameters()
    exclude_parameters = get_exclude_parameters()
    found_files = find_files(sd_card_path, search_parameters, exclude_parameters)
    create_collection_file(sd_card_path, collection_name, search_parameters, exclude_parameters, found_files)
