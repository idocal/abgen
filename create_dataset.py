import os
import pandas as pd
import argparse


def csv_directory_to_txt_file(dirname, dest_file, fasta=False):
    files = os.listdir(dirname)
    files = [f for f in files if ".csv" in f]
    seq_i = 1
    print(f"Analyzing {len(files)} files")
    print(f"Writing {'fasta' if fasta else 'txt'} format")

    with open(dest_file, mode='wt', encoding='utf-8') as f:
        for i, filename in enumerate(files):
            print(f"\rFile: {i+1}/{len(files)}", end="")
            filepath = os.path.join(dirname, filename)
            df = pd.read_csv(filepath, skiprows=1)
            write_buffer = ""
            for j, line in enumerate(df["sequence_alignment_aa"]):
                if fasta:
                    write_buffer += f"> seq_{seq_i}\n{line}\n"
                else:
                    write_buffer = " ".join(line) + "\n"
                seq_i += 1
            f.write(write_buffer)

    print(f"\n{seq_i} records have been added")
    print(f"Data has been successfully saved to {dest_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert CSV directory to data file')
    parser.add_argument('--dir', help='The CSV files directory')
    parser.add_argument('--to', help='The destination .txt file')
    parser.add_argument('--fasta', action="store_true", help='write FASTA file')
    args = parser.parse_args()
    csv_directory_to_txt_file(args.dir, args.to, args.fasta)
