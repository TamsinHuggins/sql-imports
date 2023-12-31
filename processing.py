def read_and_split_file(input_file):
    # Read the string from the input file
    with open(input_file, 'r') as file:
        data = file.read()

    # Trim the string to keep only the tuples
    start = data.find('(')
    data = data[start:]

    # Split the string into a list of tuples
    tuples = data.split('),')
    tuples = [t + ')' for t in tuples if t]  # Add the closing parenthesis back

    # Divide the tuples into groups of 1000
    groups = [tuples[i:i + 1000] for i in range(0, len(tuples), 1000)]

    # Write each group to a new file
    for i, group in enumerate(groups):
        with open(f'./scripts/{filename}{i+1}.txt', 'w') as file:
            file.write('INSERT INTO ' + filename + ' VALUES ')
            file.write(','.join(group))
            file.write(';')

# Example usage
if __name__ == '__main__':
    filenames = ['person', 'games_competitor', 'competitor_event'] # Replace with your file name
    for filename in filenames: 
        input_file = f'{filename}.txt'  
        read_and_split_file(input_file)
