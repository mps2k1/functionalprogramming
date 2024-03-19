def filter_long_words(words):
    avg_length = sum(len(word) for word in words) / len(words)
    return [word for word in words if len(word) > avg_length]
