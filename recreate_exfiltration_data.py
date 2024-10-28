with open('exfiltrated_data', 'r') as file:
    lines = file.readlines()

# Deduplication
unique_lines = list(dict.fromkeys(lines)) 

final_result = ""

for line in unique_lines:
    start = line.find('.') + 1
    end = line.find('.', start)

    if start != -1 and end != -1:
        extracted_value = line[start:end]
        final_result += extracted_value

with open('output.txt', 'w') as output_file:
    output_file.write(final_result)

print(final_result)
