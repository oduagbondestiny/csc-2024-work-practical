
#Create Class to reverse words

class StringReverse:

    @staticmethod
    def reverse_string(input_string):

        reverse_words = reversed(input_string)
        reverse_string = ''.join(reverse_words)

        return reverse_string

#calling elements in class

reverser = StringReverse()
       
#Collecting user input
input_string = input("Type in your word: ")

reverse_string = reverser.reverse_string(input_string)

print(reverse_string)

