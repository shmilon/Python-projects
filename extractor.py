tfile = 'test.txt'
toutfile = 'output.txt'

# Read lines from the input file
with open(tfile, 'r') as file:
    lines = file.readlines()

# Combine lines excluding the time format lines
result = ''
skip_next_line = False
for line in lines:
    if not any(char.isdigit() for char in line.strip()):
        result += line.strip() + ' '
    else:
        skip_next_line = True

# Write the result to the output file
with open(toutfile, 'w') as output_file:
    output_file.write(result)

# Print the result
print("FINAL RESULT:", result)
