# Language_Modeling
Natural language modeling project

# Main.py
Performs the pre-processing on the training and the test files.
1. Pad each sentence in the training and test corpora with start and end symbols (you can
use `<s>` and `</s>`, respectively).
2. Lowercase all words in the training and test corpora. Note that the data already has
been tokenized (i.e. the punctuation has been split off words).
3. Replace all words occurring in the training data once with the token `<unk>`. Every word
in the test data not seen in training should be treated as `<unk>`.

# Training_models.py
This file produces answers the following questions

1. How many word types (unique words) are there in the training corpus? Please include
the end-of-sentence padding symbol `</s>` and the unknown token `<unk>`. Do not include
the start of sentence padding symbol `<s>`.

2. How many word tokens are there in the training corpus? Do not include the start of
sentence padding symbol `<s>`.

3. What percentage of word tokens and word types in the test corpus did not occur in
training (before you mapped the unknown words to `<unk>` in training and test data)?
Please include the padding symbol `</s>` in your calculations. Do not include the start
of sentence padding symbol `<s>`.

4. Now replace singletons in the training data with `<unk>` symbol and map words (in the
test corpus) not observed in training to `<unk>`. What percentage of bigrams (bigram
types and bigram tokens) in the test corpus did not occur in training (treat `<unk>` as a
regular token that has been observed). Please include the padding symbol `</s>` in your
calculations. Do not include the start of sentence padding symbol `<s>`.

5. Compute the log probability of the following sentence under the three models (ignore
capitalization and pad each sentence as described above). Please list all of the parameters
required to compute the probabilities and show the complete calculation. Which
of the parameters have zero values under each model? Use log base 2 in your calculations.
Map words not observed in the training corpus to the `<unk>` token.
> I look forward to hearing your reply.

6. Compute the perplexity of the sentence above under each of the models.

7. Compute the perplexity of the entire test corpus under each of the models. Discuss the
differences in the results you obtained.
