
# Function to find smallest window
# containing all characters of 'pat'
def findSubString(string, pat):
 
    len1 = len(string)
    len2 = len(pat)
 
    # Check if string's length is
    # less than pattern's
    # length. If yes then no such
    # window can exist
    if len1 < len2:
        print("No such window exists")
        return ""
 
    hash_pat = {}
    hash_str = {}
 
    # Store occurrence ofs characters of pattern
    for char in pat:
        if char not in hash_pat.keys():
            hash_pat[char] = 1
        else:
            hash_pat[char] += 1

    start, start_index, min_len = 0, -1, float('inf')
 
    # Start traversing the string
    count = 0  # count of characters
    for j in range(0, len1):
        char = string[j]

        if char not in hash_pat.keys():
            hash_pat[char] = 0
        # If string's char matches with
        # pattern's char then increment count
        if char in hash_str.keys():
            # count occurrence of characters of string
            hash_str[char] += 1
        else:
            # count occurrence of characters of string
            hash_str[char] = 1
        
        if (hash_str[char] <= hash_pat[char]):
            count += 1
    
        # if all the characters are matched
        if count == len2:

            # Try to minimize the window
            while (hash_str[string[start]] > hash_pat[string[start]] or hash_pat[string[start]] == 0):

                if (hash_str[string[start]] > hash_pat[string[start]]):
                    hash_str[string[start]] -= 1
                start += 1

            # update window size
            len_window = j - start + 1
            if min_len > len_window:

                min_len = len_window
                start_index = start
 
    # If no window found
    if start_index == -1:
        print("No such window exists")
        return ""
 
    # Return substring starting from
    # start_index and length min_len
    return string[start_index: start_index + min_len]
 
 
# Driver code
if __name__ == "__main__":
 
    string = "this is a test string"
    pat = "erg"
 
    print(findSubString(string, pat))