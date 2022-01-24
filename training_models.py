import main
import math
test = open("text/processed_test.txt", "r", encoding='UTF-8')
train = open("text/processed_train.txt", "r", encoding='UTF-8')


# make a dictionary for the newly processed text
def new_dict(file):
    a_dict = dict()
    for line in file:
        for word in line.split():
            if word not in a_dict:
                a_dict[word] = 1
            # else increment key if there is multiple occurrence of that key
            else:
                a_dict[word] += 1
    return a_dict


def number_of_unk(file):
    return len(file)-1


def number_of_words(file):
    count = 0
    for words in file:
        if words != '<s>':
            count += file[words]
    return count


# count = words in test but not in train
# total = total number of words in train before <unk>
# percent = (count / total) * 100
def did_not_occur(test_file, train_file):
    count = 0
    for word in test_file:
        if word not in train_file and word != '<s>':
            count += test_file[word]
    percent_token = (count / (main.test[1] - test_file['<s>'])) * 100

    print('1.3.3 - Percentage of word tokens', percent_token)

    count = 0
    for word in test_file:
        if word not in train_file and word != '<s>':
            count += 1
    percent_type = (count / (len(test_file) - 1)) * 100
    print('1.3.3 - Percentage of word type', percent_type)


def bigram_types(file):
    bigram = dict()
    test_type = open(file, "r", encoding='UTF-8')
    for line in test_type:
        words = line.split()
        for i in range(1, len(words)):
            string = words[i] + ' | ' + words[i - 1]
            if string not in bigram:
                bigram[string] = 1
            else:
                bigram[string] += 1
    test_type.close()
    length = 0
    for word in bigram:
        length += bigram[word]
    return bigram, length


def did_not_occur_bigram(test_file, train_file):
    count = 0
    length = 0
    for word in test_file:
        length += test_file[word]
        if word not in train_file and not ('<s>' in word):
            count += test_file[word]
    percent_token = (count / length) * 100
    print('1.3.4 - Percentage of word tokens', percent_token)

    count = 0
    length = 0
    for word in test_file:
        length += 1
        if word not in train_file and not ('<s>' in word):
            count += 1

    percent_type = (count / length) * 100
    print('1.3.4 - Percentage of word type', percent_type)


# Create a new dictionary for faster runtime
test_dict = new_dict(test)
train_dict = new_dict(train)

# Question 1
print('1.3.1 - Unique words in training corpus:', number_of_unk(train_dict)) #41738

# Question 2
print('1.3.2 - Word tokens in training corpus',number_of_words(train_dict)) #2468210

# Question 3
# Percentage of word tokens 1.6612495485734922
# Percentage of word type 3.6057692307692304
did_not_occur(main.test[0], main.train[1])

# Question 4
bigram_train_types = bigram_types("text/processed_train.txt")
bigram_test_types = bigram_types("text/processed_test.txt")
did_not_occur_bigram(bigram_test_types[0], bigram_train_types[0])

# Question 5

string = '<s> I look forward to hearing your reply . </s>'

def quest_5_unigram(string):
    string = string.lower().split()
    total = 0
    for word in string:
        if word != '<s>':
            current = math.log(main.train[1][word] / (number_of_words(main.train[1])), 2)
            total = total + current
    return total


def quest_5_bigram(string):
    string = string.lower().split()
    arr = []
    string_dict = dict()
    for word in string:
        if word not in main.train[1]:
            arr.append('<unk')
        else:
            arr.append(word)

    for i in range(1, len(arr)):
        stri = arr[i] + ' | ' + arr[i - 1]
        if stri not in string_dict:
            string_dict[stri] = 1
        else:
            string_dict[stri] += 1
    for word in string_dict:
        if word not in bigram_train_types[0]:
            return "This '" + word + "' is not in the training", string_dict


def quest_5_bigram_smoothing(bigram_dict):
    total = 0
    v = number_of_unk(train_dict)
    for word in bigram_dict:
        prev = word.split(' | ')[1]
        if word not in bigram_train_types[0]:
            current = math.log(1 / (train_dict[prev] + v), 2)
        else:
            current = math.log((bigram_train_types[0][word] + 1) / (train_dict[prev] + v), 2)
        total += current

    return total

def quest_6_unigram(string):
    length = 0
    for word in string.split():
        length += 1

    l = (1 / (length - 1)) * quest_5_unigram(string)
    perplex_unigram = 2 ** (-l)
    print('1.3.6 - Perplexity unigram:', perplex_unigram)

    print('1.3 6 - Perplexity bigram: N/A')
    l = (1 / (length - 1)) * quest_5_bigram_smoothing(bigram[1])
    perplex_bigram = 2 ** (-l)
    print('1.3.6 - Perplexity bigram with add-one smoothing:', perplex_bigram)


bigram = quest_5_bigram(string)
print('1.3.5 - Unigram:', quest_5_unigram(string))
print('1.3.5 - Bigram:', quest_5_bigram(string)[0])
print('1.3.5 - Bigram with add one smoothing:', quest_5_bigram_smoothing(bigram[1]))
quest_6_unigram(string)


# compute the log probability of test then compute the perplexity
def quest_7():
    file = open("text/processed_test.txt", "r", encoding='UTF-8')
    train_7 = open("text/processed_train.txt", "r", encoding='UTF-8')
    test_list = []
    test_bigram = dict()
    train_bigram = dict()

    for line in train_7:
        words = line.split()
        for i in range(1, len(words)):
            string = words[i] + ' | ' + words[i - 1]
            if string not in train_bigram:
                train_bigram[string] = 1
            else:
                train_bigram[string] += 1

    for line in file:
        words = line.split()
        for i in range(1, len(words)):
            string = words[i] + ' | ' + words[i - 1]
            if string not in test_bigram:
                test_bigram[string] = 1
            else:
                test_bigram[string] += 1

    for line in file:
        for word in line.split():
            test_list.append(word)
    log_unigram = 0
    for word in test_list:
        if word != '<s>':
            current = math.log(train_dict[word] / (number_of_words(train_dict)), 2)
            log_unigram = log_unigram + current

    l = (1 / (number_of_words(test_dict))) * log_unigram
    perplex_unigram = 2 ** (-l)
    print('1.3.7 - Perplexity Unigram: ', perplex_unigram)



    v = number_of_unk(train_dict)
    log_bigram = 0
    for word in test_bigram:
        prev = word.split(' | ')[1]
        if word not in train_bigram:
            current = math.log(1 / (train_dict[prev] + v), 2)

        else:
            current = math.log((train_bigram[word] + 1) / (train_dict[prev] + v), 2)
            print(word, train_bigram[word])
        log_bigram = current + log_bigram
    print(log_bigram)
    l = (1 / number_of_words(test_dict)) * log_bigram
    perplex_bigram = 2 ** (-l)
    print('1.3.7 - Perplexity Bigram with add one smoothing: ', perplex_bigram)


quest_7()
print("Process Complete")