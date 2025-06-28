import csv
import random
import os

# Paths
input_file = '/home/eleven/africa_voiceModels/Client_JRolo/xhosa/dataset_files/metadata.csv'
train_output = '//home/eleven/africa_voiceModels/Client_JRolo/xhosa/dataset_files/vmetadata_train.csv'
eval_output = '/home/eleven/africa_voiceModels/Client_JRolo/xhosa/dataset_files/metadata_eval.csv'

# Define click replacements
click_replacements = {
    'c': '[_c]',
    'C': '[_c]',
    'x': '[_x]',
    'X': '[_x]',
    'q': '[_q]',
    'Q': '[_q]'
}


total_rows = 0
total_replaced = 0
replacement_counts = {char: 0 for char in click_replacements}


processed_data = []
header = None

print(f"Processing {input_file}...")

with open(input_file, 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile, delimiter='|')
    

    header = next(reader)
 
    for row in reader:
        if len(row) >= 3:  # Ensure row has enough columns
            audio_file, text, speaker_name = row[0], row[1], row[2]
            

            processed_chars = []
            for char in text:
                if char in click_replacements:
                    processed_chars.append(click_replacements[char])
                    replacement_counts[char] += 1
                    total_replaced += 1
                else:
                    processed_chars.append(char)
            
            processed_text = ''.join(processed_chars)
            processed_data.append([audio_file, processed_text, speaker_name])
            total_rows += 1


random.shuffle(processed_data)


split_index = int(len(processed_data) * 0.9)
train_data = processed_data[:split_index]
eval_data = processed_data[split_index:]


with open(train_output, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.writer(outfile, delimiter='|')
    writer.writerow(header)
    writer.writerows(train_data)


with open(eval_output, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.writer(outfile, delimiter='|')
    writer.writerow(header)
    writer.writerows(eval_data)


print(f"Processed {total_rows} rows")
print(f"Replaced {total_replaced} click consonants")
for char, count in replacement_counts.items():
    print(f"  {char}: {count} replacements")
print(f"Training set: {len(train_data)} samples ({len(train_data)/total_rows*100:.1f}%)")
print(f"Evaluation set: {len(eval_data)} samples ({len(eval_data)/total_rows*100:.1f}%)")
print(f"Training data saved to: {train_output}")
print(f"Evaluation data saved to: {eval_output}")