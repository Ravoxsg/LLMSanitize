"""
This file implements the string-matching done for data contamination as in GPT-2's paper.
"""

import re
import numpy as np
from llmsanitize.utils.string_utils import *


def clean_text_gpt2(text):
    text = text.lower()  # lower case
    text = ''.join(i if (i.isalpha() or i == " ") else '' for i in text)  # keep alphanumeric characters
    text = re.sub(' +', ' ', text)  # only single spaces
    text = text.strip()  # initial and final spaces

    return text

# Following the logic in GPT-2's paper: https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf section 4
def main_gpt2(
    train_data,
    eval_data,
    train_data_name,
    eval_data_name,
    eval_set_key
):
    ## only keep the content per data example, discard labels
    train_data = train_data["text"]
    eval_data = eval_data["text"]

    ngram_size = 8
    train_ngrams = build_ngrams(train_data, ngram_size, clean_text_gpt2)
    message = f"There are {len(train_ngrams.keys())} {ngram_size}-grams in the training set"
    print(message)

    ngram_overlaps = overlap_ngrams(eval_data, train_ngrams, ngram_size, clean_text_gpt2)
    contaminated = np.array([int(x[0] > 0) for x in ngram_overlaps])
    frac = 100 * np.mean(contaminated)
    n_contaminated = np.sum(contaminated)
    overlaps = np.array([100 * x[0]/x[1] for x in ngram_overlaps])
    mean_overlap = np.mean(overlaps)
    message = f"\nData contamination: checking {eval_data_name}/{eval_set_key} against {train_data_name} (train)"
    message += f"\nMethod: matching of {ngram_size}-grams (GPT-2 style data contamination)"
    message += f"\n# Contaminated points: {n_contaminated}/{len(contaminated)} or {frac:.4f}%"
    message += f"\nMean {ngram_size}-grams overlap: {mean_overlap:.4f}%"
    print(message)