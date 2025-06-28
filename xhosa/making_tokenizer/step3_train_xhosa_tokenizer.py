from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace
import json
import argparse

def train_xhosa_tokenizer(input_path, tokenizer_path, vocab_size=1024):
    # Define special tokens, including click consonants
    special_tokens = [
        "[STOP]", "[UNK]", "[SPACE]", "[_c]", "[_x]", "[_q]"
    ]
    
    tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
    
    tokenizer.pre_tokenizer = Whitespace()
    
    trainer = BpeTrainer(
        special_tokens=special_tokens,
        vocab_size=vocab_size
    )
    
    tokenizer.train([input_path], trainer)
    

    tokenizer.save(tokenizer_path)
    

    with open(tokenizer_path, 'r', encoding='utf-8') as f:
        tokenizer_json = json.load(f)
    

    tokenizer_json['model']['language'] = "xh"
    

    with open(tokenizer_path, 'w', encoding='utf-8') as f:
        json.dump(tokenizer_json, f, ensure_ascii=False, indent=4)
    
    print(f"Xhosa tokenizer saved to {tokenizer_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train BPE tokenizer for Xhosa")
    parser.add_argument("--input-path", 
                        default="/home/eleven/africa_voiceModels/Client_JRolo/xhosa/dataset_files/Combined_1_2/dataset.txt",
                        help="path to processed Xhosa text")
    parser.add_argument("--tokenizer-path",
                        default="/home/eleven/africa_voiceModels/Client_JRolo/xhosa/making_tokenizer/xhosa_tokenizer_6_25.json",
                        help="where to save the tokenizer JSON")
    parser.add_argument("--vocab-size", type=int, default=1024,
                        help="size of the BPE vocab")
    args = parser.parse_args()

    train_xhosa_tokenizer(
        args.input_path,
        args.tokenizer_path,
        vocab_size=args.vocab_size
    )