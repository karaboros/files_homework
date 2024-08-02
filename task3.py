def combine_files(input_files, output_file):
    file_contents = []
    
    for file_name in input_files:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.readlines()
            file_contents.append((file_name, len(content), content))
    
    file_contents.sort(key=lambda x: x[1])
    
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_name, line_count, content in file_contents:
            out_file.write(f"{file_name}\n")
            out_file.write(f"{line_count}\n")
            out_file.writelines(content)
            out_file.write("\n")  
    
input_files = ['1.txt', '2.txt', '3.txt']  
output_file = 'result.txt'
combine_files(input_files, output_file)