alphabet_dict = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
print("--- Begin report of books/frankenstein.txt ---")

with open("frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.lower().split()
    file_lower = file_contents.lower()
for i in range(0, (len(file_contents)-1)):
    if file_lower[i] in alphabet_dict:
        alphabet_dict[file_lower[i]] += 1
    else:
        alphabet_dict[file_lower[i]] = 1

print(f"{len(words)} words found in the document")

def sort_on(dict):
    return dict["num"]
#alphabet_dict.sort(reverse = True, key=sort_on)
print(alphabet_dict)
print(len(words))
print(len(file_contents))
#print(words)