Algorithm:

Purpose: Read data from a file into a list of headlines
    Name: read_file
    Parameters: file_name
    Return: table (list of headlines)
    Algorithm:
        Open the file in read mode.
        Read each line, strip whitespace, and store it in a list.
        Close the file.
        Return the list.
Purpose: Count headlines containing a specific word
    Name: count_word_in_headlines
    Parameters: table, word
    Return: count (number of matching headlines)
    Algorithm:
        Initialize a counter.
        For each headline, check if the word is present (case-insensitive).
        Increment the counter for matches.
        Return the counter.
Purpose: Write headlines containing a specific word to a file
    Name: write_headlines_to_file
    Parameters: table, word, output_file_name
    Return: None
    Algorithm:
        Open the output file in write mode.
        Write headlines containing the word (case-insensitive) to the file.
        Close the file.
Purpose: Calculate average characters per headline
    Name: average_headline_length
    Parameters: table
    Return: average (float)
    Algorithm:
        Sum the lengths of all headlines.
        Divide by the number of headlines.
        Return the average.
Purpose: Find the longest and shortest headlines
    Name: longest_and_shortest_headlines
    Parameters: table
    Return: Tuple of longest and shortest
    Algorithm:
        Find the longest and shortest headlines by length.
        Return them as a tuple.
Purpose: Read a new file to replace current data
    Name: overwrite_file
    Parameters: file_name
    Return: table (new list of headlines)
    Algorithm:
        Call read_file with the new file name.
        Return the new list of headlines.





