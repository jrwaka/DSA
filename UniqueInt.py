class IntProcessor:
    # Constants that hold maximum and minimum values
    max_int = 2**31 - 1
    min_int = -2**31 - 1

    def __init__(self, input_file, output_file):
        # Input and Output file paths
        self.input_file = input_file
        self.output_file = output_file

        # Set to store unique integers
        self.unique_ints = set()

    def int_process(self):
            # Open the input file for reading
            with open(self.input_file, 'r') as file:
                for line in file:
                    # Clear any whitespace
                    line = line.strip()
                    try:
                        my_unique_int = int(line)
                        # Add the integer if it matches the condition
                        if self.min_int <= my_unique_int <= self.max_int:
                            self.unique_ints.add(my_unique_int)
                    except ValueError:
                        # Skip if it's not a valid integer
                        continue
            # Sort in ascending order
            sorted_ints = sorted(self.unique_ints)

            # Open the output file
            with open(self.output_file, 'w') as output_file:
                # Add each sorted integer in the output file, one per line
                for num in sorted_ints:
                    output_file.write(f'{num}\n')

# Define both of the file paths
input_file = 'Sample_input/input.txt'
output_file = 'Sample_output/output.txt'

# Object that holds both files
processor = IntProcessor(input_file, output_file)

# Process the integers from the input file and add them to the output file
processor.int_process()