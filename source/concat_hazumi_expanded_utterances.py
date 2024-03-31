import re
import csv
import json

master_filename = "../collection/master.tsv"
utterances_filename = "../collection/expanded_utterances.csv"
topic_segments_dir = "../tmp/topic_segments/"

f_outfile_sui = open("../sui_corpus.json", mode = "w", encoding="utf-8")

master_dict = {}
for idx, line in enumerate(open(master_filename)):
    if idx == 0:
        continue
    data = line.rstrip().split("\t")
    master_dict[data[0]] = [data[1], data[2], data[3], data[4]]

with open(utterances_filename, "rt") as f:
    reader = csv.reader(f)
    utterances_data = [row for row in reader]

output_list = []
for utterances in utterances_data:
    t_id = utterances[1].replace("タスク確認用", "")
    d1_filename = topic_segments_dir + master_dict[t_id][0] + ".tsv"
    d2_source_filename = topic_segments_dir + master_dict[t_id][1] + ".tsv"

    d1_dict = {}
    for _line in open(d1_filename):
        _data = _line.rstrip().split("\t")
        d1_dict[_data[0]] = {"speaker":_data[1], "text":_data[2]}

    d2_list = []
    u_id = 0
    for _line in open(d2_source_filename):
        _data = _line.strip().split("\t")
        if int(master_dict[t_id][2]) <= int(_data[0]) and int(_data[0]) <= int(master_dict[t_id][3]):
            u_id += 1
            d2_list.append({"utterance_id":u_id, "speaker":_data[1], "text":_data[2]})

    ex_id = 0
    for num in range(4, 24, 3):
        ex_id += 1
        ui_list = []
        _ui_list = []
        for i in re.split('[,，-]', utterances[num]):
            if i in d1_dict.keys():
                ui_list.append(d1_dict[i])
                _ui_list.append(d1_dict[i]["speaker"])
        expanded_utterances = utterances[num + 1]
        if ui_list != [] and "User" in "".join(_ui_list):
            output = {
                "dialogue_pair_id": int(t_id.replace("ID.", "")),
                "expanded_system_utterance_id": ex_id,
                "user_information": ui_list,
                "dialogue_context": d2_list,
                "expanded_system_utterance": expanded_utterances
            }
            output_list.append(output)

data_w = json.dumps(output_list, ensure_ascii=False, indent=2)
f_outfile_sui.write(str(data_w))
f_outfile_sui.close()
