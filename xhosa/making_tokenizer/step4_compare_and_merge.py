import json
import os

def merge_vocabularies(base_vocab_path, new_vocab_path, output_path):

    with open(base_vocab_path, 'r') as f:
        base_data = json.load(f)


    with open(new_vocab_path, 'r') as f:
        new_data = json.load(f)

    base_vocab = base_data['model']['vocab']
    new_vocab = new_data['model']['vocab']


    max_value = max(base_vocab.values())


    for key, value in new_vocab.items():
        if key not in base_vocab:
            max_value += 1
            base_vocab[key] = max_value

 
    base_data['model']['vocab'] = base_vocab
    
    if 'language' in new_data['model']:
        base_data['model']['language'] = new_data['model']['language']


    with open(output_path, 'w') as f:
        json.dump(base_data, f, ensure_ascii=False, indent=2)

    print(f"Merged vocabulary saved to {output_path}")


base_vocab_path = "/home/eleven/africa_voiceModels/alltalk_tts/models/xtts/xttsv2_2.0.3/vocab.json"
new_vocab_path = "/home/eleven/africa_voiceModels/Client_JRolo/xhosa/dataset_files/Combined_1_2/xhosa_tokenizer_6_25.json"
output_path = "/home/eleven/africa_voiceModels/Client_JRolo/xhosa/dataset_files/Combined_1_2/xhosa_merged_vocab_tokenizer_6_25.json"


merge_vocabularies(base_vocab_path, new_vocab_path, output_path)