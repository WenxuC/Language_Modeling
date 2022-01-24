test = open("text/test.txt", "r", encoding='UTF-8')
processed_test = open("text/processed_test.txt", "w", encoding='UTF-8')

train = open("text/train.txt", "r", encoding='UTF-8')
processed_train = open("text/processed_train.txt", "w", encoding='UTF-8')


# convert the train data into a new file with the follow characteristics
# <s> and </s> at the end of the sentence
# lowercase all words
# replace all the single occurrence words with <unk>
def convert_train(file, output):
    train_diction = dict()
    train_data = []
    string = ""

    # append each word onto an array for train
    for line in file:
        x = line.lower()
        x = '<s> ' + x.replace("\n", " </s>")
        for word in x.split():
            train_data.append(word)

    # make a dictionary for the words that are only used once in train
    for word in train_data:
        # if the word is not in the dictionary then create a key for that word
        if word not in train_diction:
            train_diction[word] = 1
        # else increment key if there is multiple occurrence of that key
        else:
            train_diction[word] += 1

    train_dict_model = train_diction.copy()
    # concat each word and store it into a new file
    for word in train_data:
        if train_diction[word] == 1:
            string += "<unk> "
            del train_diction[word]
        elif word == '</s>':
            string += '</s>\n'
        else:
            string += word + " "
    output.write(string)
    return train_diction, train_dict_model


def convert_test(file, training, output):
    test_diction = dict()
    test_data = []
    string = ""
    # append each word onto an array for test
    for line in file:
        x = line.lower()
        x = '<s> ' + x.replace("\n", " </s>")
        for word in x.split():
            test_data.append(word)
    # make a dictionary for the words that are only used once in text
    for word in test_data:
        # if the word is not in the dictionary then create a key for that word
        if word not in test_diction:
            test_diction[word] = 1
        else:
            test_diction[word] += 1

    for word in test_data:
        if word not in training:
            string += "<unk> "
        elif word == '</s>':
            string += '</s>\n'
        else:
            string += word + " "
    output.write(string)
    return test_diction, len(test_data)


train = convert_train(train, processed_train)
test = convert_test(test, train[0], processed_test)
print("Training Complete.")


































