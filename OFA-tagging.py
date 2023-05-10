import os.path
import subprocess, sys
from tkinter import filedialog, simpledialog, messagebox


def main():
    args = []
    messagebox.showinfo(message="Select the image folder")
    folder = filedialog.askdirectory()
    if not folder:
        print("no folder given, quitting")
        quit()
    args.append(folder)
    args.append("--caption_extension=.txt")
    batch = simpledialog.askinteger(title="Batch Size", prompt="What batch size do you want?")
    if batch:
        args.append(f"--batch_size={batch}")
    args.append("--max_data_loader_n_workers=1")
    beams = simpledialog.askinteger(title="Beams", prompt="How many beams do you want?")
    if beams:
        args.append(f"--num_beams={beams}")
    temp = simpledialog.askfloat("Temperature", "What is the temperature you want?")
    if temp:
        args.append(f"--temperature={temp}")
    max_len = simpledialog.askinteger("Maximum Length", "What is the maximum length of a caption?")
    min_len = simpledialog.askinteger("Minimum Length", "what is the minimum length of a caption?")
    if max_len:
        args.append(f"--max_length={max_len}")
    if min_len:
        args.append(f"--min_length={min_len}")
    args.append("--seed=23")
    no_rep = simpledialog.askinteger("No Repeat Ngram Size", "What \"no repeat ngram size\" do you want?")
    if no_rep:
        args.append(f"--no_repeat_ngram_size={no_rep}")
    python = sys.executable
    subprocess.check_call([python, os.path.join("finetune", "make_captions_by_ofa.py")] + args)


if __name__ == "__main__":
    main()
