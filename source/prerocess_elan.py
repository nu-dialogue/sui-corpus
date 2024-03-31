import xml.etree.ElementTree as ET
import glob
import re
import os

def revise_utt(utt_list):
    result_list = []
    for utt in utt_list:
        if utt is None:
            result = utt
        else:
            result = re.sub(r'\(.*?\)', ' ', utt)
            result = re.sub(r'\|', ' ', result)
            result = re.sub('[ 　]+', ' ', result)
            result = result.lstrip(" ")
        result_list.append(result)
    return result_list

corpus_root = "../Hazumi1911/elan/"
outfile_root = "../tmp/elan_preprocessed/"
os.makedirs(outfile_root, exist_ok=True)

for file_path in glob.glob('{}/*.eaf'.format(corpus_root)):
    output_file = outfile_root + file_path.split("/")[-1].replace(".eaf", "") + ".tsv"
    tree = ET.parse(file_path)
    root = tree.getroot()

    tier_list = []
    for name in root.iter('TIER'):
        tier_list.append(name.attrib['TIER_ID'])

    sys_utterance_list = []
    for child in root.findall('TIER'):
        if child.attrib["TIER_ID"] == "sys_utterance":
            for tmp in child.iter('ANNOTATION_VALUE'):
                sys_utterance_list.append(tmp.text)

    user_utterance_list = []
    for child in root.findall('TIER'):
        if child.attrib["TIER_ID"] == "user_utterance":
            for tmp in child.iter('ANNOTATION_VALUE'):
                user_utterance_list.append(tmp.text)

    dialogue_act_list = []
    for child in root.findall('TIER'):
        if child.attrib["TIER_ID"] == "dialogue_act":
            for tmp in child.iter('ANNOTATION_VALUE'):
                dialogue_act_list.append(tmp.text)

    # Delite fillers
    sys_utterance_list = revise_utt(sys_utterance_list)
    user_utterance_list = revise_utt(user_utterance_list)

    f_out = open(output_file, "w")
    count = 0
    for sys, user in zip(sys_utterance_list, user_utterance_list):
        if sys != None and sys != " " and sys != "" and sys != "<F>":
            count += 1
            f_out.write(str(count) + "\t" + "System\t" + sys + "\n")
        if user != None and user != " " and user != "" and user != "<F>":
            count += 1
            f_out.write(str(count) + "\t" + "User\t" + user + "\n")
