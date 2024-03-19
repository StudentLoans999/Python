## TASK: Write a program to perform a GET request on the route https://coderbyte.com/api/challenges/json/age-counting which contains a data key and the value is a string which contains items in the format: key=STRING, age=INTEGER ##
## Your goal is to count how many items exist that have an age equal to or greater than 50, and print this final value
## Once your function is working, take the final output string and combine it with your ChallengeToken both in reverse order and separated by a colon

## Example Input: {"data":"key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47"}
## Example Output: 2
## Example Output with ChallengeToken: 2gXfcXp1Xa5X

## Your ChallengeToken: Ikocdyfis28

import requests

# Extract data from the response directly
def perform_get_request(response):
    data_string = response.json()['data']  # assuming the response is in JSON format
  
    # This line is commented out because data_string is long, but uncomment if you want to verify 
    #print("Extracted Data String:", data_string) # shows the original data string extracted from the response (to verify we're getting the correct data)
    
    # Split the data string into individual key-value pairs
    pairs = data_string.split(', ') # splits the data_string into individual key-value pairs
    
    # This line is commented out because pairs is long, but uncomment if you want to verify 
    #print("Extracted Pairs:", pairs) # to verify if the string splitting is working as expected
    
    count = 0 # initialize count
    
    # Iterate over each key-value pair
    for pair in pairs:
        key, value = pair.split('=') # splits the pairs into keys and values

        # This block is commented out because there are a lot of Keys and Values, but uncomment if you want to verify 
        #print("Key:", key.strip())
        #print("Value:", value.strip()) # verify if the keys and values are correctly extracted and trimmed of any leading or trailing whitespaces
      
        if key.strip() == 'age': 
            if int(value.strip()) >= 50:
                count += 1 # increment 'count' wherever 'key' is 'age' and the corresponding 'value' is greater than or equal to 50
    
    print("Count:", count)  # print the final count of values where 'age' is equal to and greater than 50
    
    # Combine output string with 'Ikocdyfis28' in reverse order separated by a colon
    output_string = f"Ikocdyfis28:{count}"
    print(output_string[::-1]) # reverse the order of output_string

# Calls the 'perform_get_request' function and passes the response object as an argument
r = requests.get('https://coderbyte.com/api/challenges/json/age-counting') # makes a GET request
perform_get_request(r)

## OUTPUT ##
Count: 128
821:82sifydcokI
