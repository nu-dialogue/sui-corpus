cd source/

python prerocess_elan.py
python make_topic_segments.py
python concat_hazumi_expanded_utterances.py

cd ../
rm -r tmp
