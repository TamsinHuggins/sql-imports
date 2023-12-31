import os

def concatenate_files(input_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as output:
        for filename in os.listdir(input_dir):
            if filename.endswith('.txt'):  # Change the file extension if needed
                file_path = os.path.join(input_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as input_file:
                    content = input_file.read()
                    output.write(content + '\n')

if __name__ == "__main__":
    input_directory = "./scripts"  # Change this to the directory path containing your text files
    output_file_path = "sql_insert_script.txt"  # Change this to the desired output file path

    concatenate_files(input_directory, output_file_path)
    print(f"Files in {input_directory} concatenated into {output_file_path}")