import os

# Get the directory of the current file
current_directory = os.path.dirname(os.path.abspath(__file__))

# Create a new file to store the combined contents
with open(os.path.join(current_directory, 'combined_texts.txt'), 'w', encoding='utf-8') as outfile:
    # Iterate over all files in the current directory
    for filename in os.listdir(current_directory):
        # Check if the file is a .txt file
        if filename.endswith('.txt'):
            # Open the .txt file and read its contents
            with open(os.path.join(current_directory, filename), 'r', encoding='utf-8', errors='ignore') as infile:
                outfile.write(infile.read() + '\n')  # Write contents to the new file, add a newline as separator