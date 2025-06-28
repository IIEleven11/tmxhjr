import re
import os

# Path to your Xhosa dataset
input_file = '/home/eleven/africa_voiceModels/Client_JRolo/xhosa/dataset_files/dataset_2/dataset.txt'
output_file = '/home/eleven/africa_voiceModels/Client_JRolo/xhosa/dataset_files/dataset_2/parsed_concatenated_dataset.txt'

# Define click replacements
click_replacements = {
    'c': '[_c]',
    'C': '[_c]',
    'x': '[_x]',
    'X': '[_x]',
    'q': '[_q]',
    'Q': '[_q]'
}

# Counter for statistics
click_counts = {char: 0 for char in click_replacements.keys()}
total_chars = 0
total_lines = 0

# Process the file
with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', encoding='utf-8') as outfile:
    
    for line in infile:
        total_lines += 1
        total_chars += len(line)
        
        # Count click consonants before replacement
        for char in click_replacements.keys():
            count = line.count(char)
            click_counts[char] += count
        
        # Method 1: Process character by character
        processed_chars = []
        for char in line:
            if char in click_replacements:
                processed_chars.append(click_replacements[char])
            else:
                processed_chars.append(char)
        
        processed_line = ''.join(processed_chars)
        
        # Write the processed line
        outfile.write(processed_line)

# Print statistics
print(f"Processed {total_lines} lines with {total_chars} characters")
print("Click consonant statistics:")
for char, count in click_counts.items():
    print(f"  {char}: {count} occurrences")
print(f"Processing complete. Output written to {output_file}")