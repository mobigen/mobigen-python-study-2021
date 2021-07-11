from collections import defaultdict


def read_text(path):
    with open(path, 'r', encoding='UTF-8') as f:
        data = f.read()
    return data


def get_word_counted(data):
    words = data.split()
    result = defaultdict(int)
    for word in words:
        result[word] += 1
    return result


def get_top_ten_words(data: dict):
    return sorted(data.items(), key=lambda x: x[1], reverse=True)[:10]


if __name__ == '__main__':
    text = read_text('../wiki_python.txt')

    word_counted = get_word_counted(text)

    for k, v in word_counted.items():
        print(f"word: {k}, count: {v}")

    print("\nTop 10 words")
    print(get_top_ten_words(word_counted))
