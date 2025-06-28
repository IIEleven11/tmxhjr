<<<<<<< HEAD
# tmpafxh
=======
### Client_JRolo

# Progress 
(click the arrows to drop down the information from each attempt)
- Made a "Xhosa" branch of dataset maker using a custom OpenAI  Xhosa Whisper model for ASR. [Automatic Audio Dataset Maker - Xhosa](https://github.com/IIEleven11/Automatic-Audio-Dataset-Maker/tree/xhosa)
- [Audiobook Dataset with transcriptions](https://huggingface.co/datasets/IIEleven11/xhosa_audiobooks)
<details>
<summary><strong>1st attempt</strong></summary>

- was jumping the gun, cancelled training

</details>

<details>
<summary><strong>2nd attempt</strong></summary>

- Was done on only the highest quality data samples  
- Model spoke fluently but did not properly articulate the clicks  
- Used a `[CLICK_C]`, `[CLICK_X]`, `[CLICK_Q]` custom token solution (I don’t think I like this solution)

</details>

<details>
<summary><strong>3rd attempt</strong></summary>

- ~currently training~  
- Decided to use an "easier to type" custom token solution for clicking sounds  
    - `[_c]`, `[_x]`, `[_q]`  
- Trained on the entire Xhosa dataset (~120,000 samples)  
    - Model should have enough examples of clicks to properly articulate them  
- Tensorboard data looks wonderful so far ![img](https://github.com/IIEleven11/Client_JRolo/blob/main/image.png)

- Testing results are in the xhosa folder (reference wav was used to reproduce text with click sounds. Female to male)  
  - I'd call it 75% success. Click sounds were learned and it read the text as:

    ```  
    Zoba umfanekiso walo mboniso uze uzobe ne[_q]ampu lentetho ye[_x]hegokazi.  
    ```

  - Quality of the overall generation was poor/noisy. This is a trivial issue that can be solved later  
  - Important to note that male to female also caused some potential artifacting as it's a stressful and difficult change  
  - Click sounds were still not as strong as I'd like. Solution is probably targeting a more specific distribution of audio data. (Gaussian?)

- Will begin curating the dataset now that we know we have control over the specific tokens required to produce the clicking sounds  
    - This should then mean when we train the final voice model we can just provide it English text with the special tokens like:

    ```  
    Hello its nice to meet you [xh]ne[_q]ampu  
    ```  
    `"ne[_q]ampu"` is probably not a name, I'm just using it as an example.

</details>

<details>
<summary><strong>4th Attempt</strong></summary>

- Proof of concept verified.  
- The goal now is to refine the dataset, fix the uneven class distribution and train again.  
    - High quality dataset of 296 audiobook samples is undergoing a denoising and desilencing process. Should be done in the morning.

</details>

<details>
<summary><strong>5th Attempt</strong></summary>

- Using new dataset 
- Started training
- Ideal training data output so far![img](https://github.com/IIEleven11/Client_JRolo/blob/main/Screenshot%202025-06-26%20174312.png)

- Same or slightly better results, not good enough though in my opinion.
- Plan of attack: Move from equal class distribution (clicks and no clicks) to a single class dataset where only sentences with click sounds are included. 
</details>

<details>
<summary><strong>6th Attempt - 6/27 @2218 PST</strong></summary>

- Made only click dataset
  ```
  === SUMMARY ===
  Original entries: 120850
  Entries with click consonants: 41920
  Entries without click consonants: 78930
  ```
- Training on that dataset started now
- Update - Results were not as strong as I expected. Re-evaluated my code and found a potential issue. We can see in the image below the tokenizer is splitting up the special tokens. This means it was 
  splitting the tokens instead of keeping it as a single whole representation of the sound. The outcome of this being it had less examples of the right tokens to train on.
- ![image](https://github.com/user-attachments/assets/ea37b4d6-1dad-4835-b324-2fc494ec4f44)
- Fixing the tokenizer now will train another attempt shortly
- - Perfection is iteration
</details>
>>>>>>> be763ca (updated)
