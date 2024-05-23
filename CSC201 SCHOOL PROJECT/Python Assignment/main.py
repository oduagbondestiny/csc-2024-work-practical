#Making sure we cann run the program at least 5 times
i = 0

while i < 5:

    # Step 1: Accept the input sentence from the user
    sentence = input("Enter a sentence: ")
    i= i+1

    # Step 2: Split the sentence into words based on spaces
    words = sentence.split()

    # Step 3: Count the number of words
    word_count = len(words)

    # Step 4: Print the total number of words
    print(f"Total number of words: {word_count}")

    # Step 5: Print each word
    print("The words in the sentence are:")
    for word in words:
        print(word)