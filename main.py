def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
	print(file_contents)
	print(wordCount(file_contents))
	tempDict = letterCount(file_contents)
	#sortedDict = dict(sorted(tempDict.items()))
	sortedDict = dict(sorted(tempDict.items(), key=lambda item: item[1], reverse=True))
	for item in sortedDict:
		if(item.isalpha()):
			print(f"The {item} character was found {tempDict[item]} times")
            
def wordCount(book):
	words = book.split()
	return len(words)
def letterCount(book):
    letterdict = {}
    words = book.split()
    for word in words:
        temp = list(word)
        for letter in temp:
            letter = letter.lower()
            if letter in letterdict:
                  #print("it exists")
                  letterdict[letter] += 1
            else:
                  #print("doesn't exist")
                  letterdict[letter] = 1
    return letterdict

main()
