# SUI corpus: System utterance based on User Information corpus

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

This repository contains the SUI corpus, System utterance based on User Information corpus.
More details about the dataset can be found in our LREC-COLING 2024 paper:
I Remember You!: SUI Corpus for Remembering and Utilizing Users' Information in Chat-oriented Dialogue Systems

> [!NOTE]
> This public version has been filtered from all collected the expanded system utterances. Please note that it may slightly differ from the statistical information in our paper.

## Data overview

The SUI corpus was constructed by extending the Osaka University Multimodal Dialogue Corpus Hazumi (Hazumi1911)[^1].
The SUI corpus contains triplets formed of <user information, dialogue context, system utterance based on the user information and dialogue context (expanded system utterance)>.
We constructed the SUI corpus by following two tasks:

1. Extract user information from a dialogue (called dialogue-1)
2. Create system utterances based on the user information extracted in task 1 and another dialogue context (called dialogue-2).

Dialogue-1 and dialogue-2 are dialogues in which the same user talks about different topics.
We first divided each dialogue in Hazumi1911 into topic segments and then created pairs of dialogue-1 and dialogue-2.
Then, we collected seven expanded system utterances based on each pair.

## Requirements

- Python 3.8+
- Osaka University Multimodal Dialogue Corpus (Hazumi1911)

## Data creation

1. Clone sui-corpus repository
```bash
git clone https://github.com/nu-dialogue/sui-corpus.git
cd sui-corpus
```

2. Clone Hazumi1911 repository
```bash
git clone https://github.com/ouktlab/Hazumi1911.git
```

3. Create the SUI corpus
```bash
bash run_make_sui_corpus.sh
```

## Data format

The created dataset (`sui-corpus/sui_corpus.json`) consists of dialogue_pair_id, expanded_system_utterance_id, user_information, dialogue_context, and expanded_system_utterance.

| Key | Type | Explanation |
| --- | --- | --- |
| dialogue_pair_id | int | Dialogue pair ID of dialogue-1 and dialogue-2. |
| expanded_system_utterance_id | int | Expanded system utterance ID, unique within the dialogue pair. Indexed starting from 1 to 7. |
| user_information | list (dict) | List of user information extracted by dialogue-1. |
| user_information.speaker | str | Speaker name. |
| user_information.text | str | Utterance text. |
| dialogue_context | list (dict) | List of dialogue context, i.e., dialogue-2. |
| dialogue_context.utterance_id | int | Utterance ID, unique within the dialogue. Indexed starting from 1. |
| dialogue_context.speaker | str | Speaker name. |
| dialogue_context.text | str | Utterance text. |
| expanded_system_utterance | str | Expanded system utterance text. |

```jsonc
[
	{
		"dialogue_pair_id": 1,
		"expanded_system_utterance_id": 1
		"user_information": [
			{
				"speaker": "User",
				"text": "そうですね ビールとか 日本酒 酎ハイ 大概のものは飲みます"
			},
			// ...
		],
		"dialogue_context": [
			{
				"utterance_id": 1,
				"speaker": "User",
				"text": "最近見た映画 最近見た映画 最近見た映画最近映画館は行かないので テレビでもいいですか"
			},
			{
				"utterance_id": 2,
				"speaker": "System",
				"text": "それでは少し「テレビ」の話をしましょう！"
			},
			// ...
		],
		"expanded_system_utterance": "ドラマを見るときは、なにかお酒を飲みながらが多いですか？"
	},
	{
		"dialogue_pair_id": 1,
		"expanded_system_utterance_id": 2
		// ...
	},
	// ...
]
```

## Citation

```bibtex
@inproceedings{tsunomori2024i,
    title = "I Remember You!: SUI Corpus for Remembering and Utilizing Users' Information in Chat-oriented Dialogue Systems",
    author = "Tsunomori, Yuiko and Higashinaka, Ryuichiro",
    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation",
    year = "2024",
    url = "",
    pages = "",
}

@inproceedings{tsunomori2022user,
    title = "ユーザ情報と対話文脈を考慮した発話生成のための対話コーパスの構築",
    author = "角森, 唯子 and 東中, 竜一郎",
    booktitle = "人工知能学会全国大会論文集第36回全国大会",
    year = "2022",
    url = "https://www.jstage.jst.go.jp/article/pjsai/JSAI2022/0/JSAI2022_3Yin201/_pdf/-char/ja",
    pages = "3Yin201-3Yin201",
}
```

## References

[^1]: Kazunori Komatani, Shogo Okada, Haruto Nishimoto, Masahiro Araki, and Mikio Nakano. Multimodal Dialogue Data Collection and Analysis of Annotation Disagreement.  In Proceedings of the International Workshop on Spoken Dialogue Systems Technology (IWSDS), pp. 201-213, 2019.
