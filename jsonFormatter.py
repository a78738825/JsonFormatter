import os
import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

def format_and_save_json(input_file):
    try:
        with open(input_file, "r") as json_file:
            data = json.load(json_file)

        formatted_data = json.dumps(data, indent=4)
        output_file = input_file.replace(".json", "(formatted).json")

        with open(output_file, "w") as new_file:
            new_file.write(formatted_data)
        
        print("Formatted data saved to:", output_file)
        return formatted_data
    except Exception as err:
        print("Error:", err)

def input_files(method):
    files = []
    if method == "m":
        filename = input("Enter the file name: ")
        if filename.endswith(".json") and filename in os.listdir():
            files.append(filename)
        else:
            raise Exception("Invalid file name!")
    elif method == "s":
        for item in os.listdir():
            if item.endswith(".json") and "formatted" not in item:
                files.append(item)
    else:
        raise Exception("Invalid input!\nEnter 'm' for manual file input, 's' for automatic scan.")

    return files

def main():
    method = input("Enter 'm' to input files manually or 's' to scan for all JSON files in the directory: ")
    files = input_files(method)

    if len(files) >= 1:
        for file in files:
            formatted_data = format_and_save_json(file)
            
            # Highlight and print JSON data
            lexer = JsonLexer()
            formatter = TerminalFormatter()
            highlighted_json = highlight(formatted_data, lexer, formatter)
            print(highlighted_json)

if __name__ == "__main__":
    main()
