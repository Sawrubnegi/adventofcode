print("Adventofcode is here")

# Specify the file path and the symbol you want to count
file_path = 'example.txt'  # Replace with the path to your file
symbol_to_count = '('      # Replace with the symbol you want to count

try:
    with open(file_path, 'r') as file:
        # Initialize a counter for the symbol
        count = 0
        pos = 0

        # Read the file character by character
        for char in file.read():
            pos += 1
            # Check if the current character matches the symbol
            if char == symbol_to_count:
                count += 1
                pos += 1               
            elif char == ')':
                count -= 1
        print (pos)                    
        # Print the count
        print(f"The symbol '{symbol_to_count}' appears {count} times in the file.")
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
