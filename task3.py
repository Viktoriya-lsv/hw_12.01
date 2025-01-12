# Задание 3
file_paths = ['1.txt', '2.txt', '3.txt']


output_file_path = 'result.txt'
file_data = []
for file in file_paths:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        file_data.append((file, len(lines), lines))
file_data.sort(key=lambda x: x[1])
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for file_path, line_count, lines in file_data:
        file_name = file_path.split('/')[-1]
        output_file.write(f'{file_name}\n{line_count}\n')
        output_file.writelines(lines)
        output_file.write("\n")
