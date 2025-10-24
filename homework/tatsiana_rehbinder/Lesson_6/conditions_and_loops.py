text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel."
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)
words = text.split()
new_words = []

for word in words:
    if word[-1] in [',', '.']:
        new_word = word[:-1] + 'ing' + word[-1]
    else:
        new_word = word + 'ing'
    new_words.append(new_word)
print(' '.join(new_words))
