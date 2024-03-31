import re
import glob
import os

outfile_root = "../tmp/topic_segments/"
os.makedirs(outfile_root, exist_ok=True)
corpus_root = '../tmp/elan_preprocessed/'
for file_path in glob.glob('{}/*.tsv'.format(corpus_root)):
    count = 0
    output_file = 0
    for line in open(file_path):
        if "について話しましょう" in line:
            count += 1
            output_file = outfile_root + file_path.split("/")[-1].replace(".tsv", "") + "_" + str(count) + ".tsv"
            f_out = open(output_file, "w")
            f_out.write(line)
        elif "それではつぎの話題にうつりたいとおもいます。" in line:
            f_out.write(line)
            count += 1
            output_file = outfile_root + file_path.split("/")[-1].replace(".tsv", "") + "_" + str(count) + ".tsv"
            f_out = open(output_file, "w")
        elif "それでは最後の質問です。" in line:
            break
        else:
            if output_file == 0:
                continue
            else:
                f_out.write(line)
f_out.close()

for file_path in glob.glob('{}*.tsv'.format(outfile_root)):
    # Delete empty files
    if os.stat(file_path).st_size == 0:
        os.remove(file_path)
        continue

    # Delete low turns files
    N = 15
    with open(file_path) as f:
        lines = f.readlines()
        if len(lines) < N:
            os.remove(file_path)
