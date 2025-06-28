#!/usr/bin/env python3

import os
import xml.etree.ElementTree as ET
import csv
from pathlib import Path

def parse_xml_files(directory_path, output_file):
    """
    Parse XML files in the given directory and extract filename, transcription, and speaker_name
    into a pipe-delimited CSV file.
    """
    
    if not os.path.exists(directory_path):
        print(f"Error: Directory {directory_path} does not exist")
        return
    
    data_rows = []
    xml_files = Path(directory_path).glob("*.xml")
    
    for xml_file in xml_files:
        print(f"Processing: {xml_file}")
        
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            recordings = root.findall(".//recording")
            
            for recording in recordings:

                audio_path = recording.get("audio")
                if audio_path:

                    filename = os.path.basename(audio_path)
                    orth_element = recording.find("orth")
                    transcription = ""
                    if orth_element is not None and orth_element.text:
                        transcription = orth_element.text.strip()
                    
                    speaker_name = "speaker_1"
                    
                    data_rows.append([filename, transcription, speaker_name])
        
        except ET.ParseError as e:
            print(f"Error parsing {xml_file}: {e}")
        except Exception as e:
            print(f"Error processing {xml_file}: {e}")

    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
            
            for row in data_rows:
                writer.writerow(row)
        
        print(f"Successfully created {output_file} with {len(data_rows)} entries")
        
    except Exception as e:
        print(f"Error writing to CSV file: {e}")

def main():
    directory_path = "/home/eleven/africa_voiceModels/alltalk_tts/data/Transcriptions"
    output_file = "transcriptions.csv"
    
    parse_xml_files(directory_path, output_file)
    
    if os.path.exists(output_file):
        print(f"\nFirst 5 lines of {output_file}:")
        with open(output_file, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i < 5:
                    print(line.strip())
                else:
                    break

if __name__ == "__main__":
    main()