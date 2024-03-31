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

## References

[^1]: Kazunori Komatani, Shogo Okada, Haruto Nishimoto, Masahiro Araki, and Mikio Nakano. Multimodal Dialogue Data Collection and Analysis of Annotation Disagreement.  In Proceedings of the International Workshop on Spoken Dialogue Systems Technology (IWSDS), pp. 201-213, 2019.
