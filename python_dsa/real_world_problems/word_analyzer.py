while True:

    sentence = input("Enter a sentence: ").strip()

    if len(sentence) == 0:
        print("Sentence Cannot Be Empty")
    else:
        break


words = sentence.lower().split()

total_words = len(words)

unique_words = len(set(words))

longest_word = words[0]
shortest_word = words[0]

for word in words:

    if len(word) > len(longest_word):
        longest_word = word

    if len(word) < len(shortest_word):
        shortest_word = word


print("\nTotal Words:", total_words)
print("Longest Word:", longest_word)
print("Shortest Word:", shortest_word)
print("Unique Words:", unique_words)


search_word = input("\nEnter word to search: ").lower()

if search_word in words:
    print("Word Found")
else:
    print("Word Not Found")