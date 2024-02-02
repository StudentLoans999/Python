The code below works by first reading a given file (coding_qual_input.txt), and reads the contents line-by-line and returning a list where each element is a line from the file (assigned to 'lines').
Next, an empty list is created/initialized ('words_in_message')which would be used to store the words in the given file, and a placeholder of 300 empty strings is added to that list.
Now in the real list of file contents, each line is split into two parts, a number and a word, and they get assigned to variables.
For each line (of the 300), the line is arranged into a pyramid shape, in order to decode the hidden message. Then the last number in each line is checked against the 'number' value created earlier. If they match, then that is the key to decoding the hidden message (that number is useful).
Since that number is useful, it then goes to the line in the given file that has that value, and gets the word beside it, which is then added to the list of decoded words.
Finally, the list of decoded words are concatenated into a single string to output the hidden message.

def decode(message_file): # a function to decode a hidden message
    with open(message_file, "r") as f: # read the lines from the specified (given) file
        lines = f.readlines()
  
    words_in_message = [] # initialize an empty list to store the words in the message

    for x in range(300): # initialize the list elements with 300 length, to serve as place holders, since there are 300 lines in the dataset
        words_in_message.append('') # these empty strings will be replaces with actual words later in the function

    # Loop through the lines in the file
    for line in lines:
        # Extract the number and word from each line
        number, word = int(line.split()[0]), line.split()[1] # splits the line into the two separate elements (the number being the first element and word being the second) and converts the word into an int

        # Check if the number corresponds to the last element value of a "pyramid" line
        for x in range(300):
            if number == (int((x * x + x) / 2)): # get the last element and check if it is the same value as 'number'
                words_in_message[x] = word # if so, then it looks in 'lines' for that value/element and then makes the word on that line be a decoded word
                break

    # Concatenate the non-null list values to form a sentence
    text = " ".join(x for x in words_in_message if x != '') # creates a list of non-empty words from the list of decoded words and then joins them into a single string

    # Return the resulting decoded message
    return text

file_path = "c:/Users/david/Downloads/message.txt" # specify the file path

decoded_message = decode(file_path) # decode the message and output the result
print(decoded_message)
