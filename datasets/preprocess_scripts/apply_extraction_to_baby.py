import os
import random

def rename_and_generate_identity(directory):
    """
    Renames all images in the given directory to ascending numbers starting from 000001
    and creates/updates 'identity_Baby.txt' with the image names and unique random subject numbers.

    :param directory: Path to the directory containing the images
    """
    # Ensure the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")

    # Get a list of image files in the directory
    image_files = [f for f in os.listdir(directory) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    # Sort files for consistent ordering
    image_files.sort()

    # Generate a list of unique random subject numbers
    num_images = len(image_files)
    subject_numbers = random.sample(range(10000), num_images)

    # Prepare the identity file path
    identity_file_path = os.path.join(directory, 'identity_Baby.txt')

    # Open the identity file for writing
    with open(identity_file_path, 'w') as identity_file:
        for index, original_file_name in enumerate(image_files):
            new_file_name = f"{index + 1:06}.jpg"
            original_file_path = os.path.join(directory, original_file_name)
            new_file_path = os.path.join(directory, new_file_name)

            # Rename the image file
            try:
                os.rename(original_file_path, new_file_path)
            except FileExistsError:
                raise FileExistsError(f"File {new_file_name} already exists and cannot be overwritten.")

            # Write the new file name and subject number to the identity file
            identity_file.write(f"{new_file_name} {subject_numbers[index]}\n")

# Example usage:
# rename_and_generate_identity("path/to/directory")