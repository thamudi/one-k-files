import time
from subprocess import Popen
from os import mkdir, path, name, walk


def group_files_languages(destination_dir="lang", root_dir="tests"):
    print("Grouping languages ...")
    full_destination_dir = path.join(root_dir, destination_dir)
    generate_dir(full_destination_dir)

    try:
        for subdir, dirs, files in walk("files"):
            for file in files:
                if file.endswith(".txt"):
                    original_file_path = path.join("files", file)
                    new_file_path = path.join(
                        full_destination_dir, file.split("-")[0])

                generate_dir(new_file_path)

            if name == "nt":  # Check for windows operating systems
                Popen(
                    f"copy {original_file_path} {new_file_path}".split(), shell=True)
            else:
                Popen(f"cp {original_file_path} {new_file_path}".split())
    except Exception as e:
        print("An error occurred")
        print(e)


def generate_dir(directory_full_path):
    """
    A safe way to generate a new directory in a given path
    """
    if not path.isdir(directory_full_path):
        mkdir(directory_full_path)


if __name__ == "__main__":
    destination_dir = input("Enter directory name to be created: ")
    start_time = time.time()  # start execution timer
    group_files_languages(destination_dir, ".")
    print(f"Process took: --- { (time.time() - start_time)} seconds ---")
