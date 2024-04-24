import os.path


def build_file_path(folder, filename):
    current_directory = os.path.dirname(__file__)  # Gets the directory where the script is located
    folder_path = os.path.join(current_directory, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, filename)
    return file_path


def write_excel(df, filename, folder):
    filepath = build_file_path(folder, filename)
    df.to_excel(filepath, index=False)
