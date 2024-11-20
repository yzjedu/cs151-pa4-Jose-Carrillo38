def read_file():
    file_found = False
    file_name = ""
    valid_files = ["2014.txt", "2015.txt", "2016.txt", "2017.txt", "2018.txt", "2019.txt"]
    print(f"Available files: {', '.join(valid_files)}")
    while file_found != True:
        file_name = input("Enter the file name you want to analyze: ")
        if file_name in valid_files:
            try:
                with open(file_name, 'r') as file:
                    table = [line.strip() for line in file]
                    file_found = True
                    return table
            except FileNotFoundError:
                print(f"File {file_name} not found. Please try again.")
        else:
            print("Invalid file name. Please choose a valid file from the list.")

def count_word_in_headlines(table, word):
    word = word.lower()
    count = sum(1 for headline in table if word in headline.lower())
    return count

def write_headlines_to_file(table, word, output_file_name):
    with open(output_file_name, 'w') as file:
        for headline in table:
            if word.lower() in headline.lower():
                file.write(headline + '\n')

def average_headline_length(table):
    total_characters = sum(len(headline) for headline in table)
    return total_characters / len(table) if table else 0

def longest_and_shortest_headlines(table):
    longest = max(table, key=len, default="")
    shortest = min(table, key=len, default="")
    return longest, shortest

def main():
    print("Welcome to the ABC Headline Analyzer!")
    print("This program helps analyze headlines from files containing real headlines.")
    print("------------------------------------------------")

    table = read_file()

    options = [
        "Count headlines with a specific word",
        "Write headlines with a specific word to a file",
        "Calculate the average headline length",
        "Find the longest and shortest headlines",
        "Read a new file to analyze",
        "Quit"
    ]

    user_choice = None
    while user_choice != 6:
        print("\nChoose an option:")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        try:
            user_choice = int(input("Enter your choice (1-6): "))
            if user_choice == 1:
                word = input("Enter the word to search for: ")
                count = count_word_in_headlines(table, word)
                print(f"There are {count} headlines containing the word '{word}'.")
            elif user_choice == 2:
                word = input("Enter the word to search for: ")
                output_file_name = input("Enter the name of the output file: ")
                write_headlines_to_file(table, word, output_file_name)
                print(f"Headlines containing the word '{word}' have been written to {output_file_name}.")
            elif user_choice == 3:
                avg_length = average_headline_length(table)
                print(f"The average headline length is {avg_length:.2f} characters.")
            elif user_choice == 4:
                longest, shortest = longest_and_shortest_headlines(table)
                print(f"The longest headline is: {longest}")
                print(f"The shortest headline is: {shortest}")
            elif user_choice == 5:
                print("Reading a new file...")
                table = read_file()
                print("New file loaded successfully.")
            elif user_choice == 6:
                print("Thank you for using the ABC Headline Analyzer. Goodbye!")
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
