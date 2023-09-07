def count_and_replace_terrible(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            text = file.read()

        # Count the occurrences of the word "terrible"
        terrible_count = text.lower().count("terrible")

        # Split the text into words and iterate to replace even/odd occurrences
        words = text.split()
        for i in range(len(words)):
            if words[i].lower() == "terrible":
                if i % 2 == 0:
                    words[i] = "pathetic"
                else:
                    words[i] = "marvellous"

        # Join the modified words back into a string
        new_text = ' '.join(words)

        # Write the modified text to the output file
        with open(output_file, 'w') as result_file:
            result_file.write(new_text)

        return terrible_count

    except FileNotFoundError:
        return -1  # Return -1 to indicate the input file was not found

if __name__ == "__main__":
    input_file = "/Users/mxqdecomputer/Downloads/file_to_read.txt"  # Update with your actual file path
    output_file = "result.txt"

    terrible_count = count_and_replace_terrible(input_file, output_file)

    if terrible_count == -1:
        print("Input file not found.")
    else:
        print(f"Total occurrences of 'terrible': {terrible_count}")
        print("Modified text has been written to 'result.txt'")
