def  filter_and_sort_evens(numbers):
    evens = []
    for i in numbers:
        if i % 2 == 0:
            evens.append(i)
    return sorted(evens)

def count_character_frequency(text):
    freq = {}
    for ch in text.lower():  # convert to lowercase
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

num = [3, 1, 4, 1, 5, 9, 2, 6]
print(filter_and_sort_evens(num))

text = "Hello Sucharitha"
print(count_character_frequency(text))




