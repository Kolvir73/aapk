import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)
    pyperclip.paste()

# Define the path to your text file
input_text_path = 'formatted_data.txt'

# Read the text file
with open(input_text_path, 'r') as text_file:
    # Split the file into blocks separated by '---'
    content_blocks = text_file.read().split('---\n')

    for block in content_blocks:
        # Remove any leading/trailing whitespace
        block = block.strip()

        if block:  # If the block is not empty
            # Copy block to clipboard
            copy_to_clipboard(block)
            print("The following block has been copied to the clipboard:")
            print(block)
            print("\nPress ENTER to copy the next block...")
            input()  # Wait for user to press ENTER

print("All blocks have been processed.")

