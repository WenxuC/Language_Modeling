# Language_Modeling
Natural language modeling project

# Main.py
Performs the pre-processing on the training and the test files.
1. Pad each sentence in the training and test corpora with start and end symbols (you can
use <s> and </s>, respectively).
2. Lowercase all words in the training and test corpora. Note that the data already has
been tokenized (i.e. the punctuation has been split off words).
3. Replace all words occurring in the training data once with the token <unk>. Every word
in the test data not seen in training should be treated as <unk>.
