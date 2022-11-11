# Write a program that prompts for a file name, then opens that file and reads
# through the file, looking for lines of the form: [X-DSPAM-Confidence: 0.8475]
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown above.
fname = input("Enter file name: ")
fh = open(fname)
total = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    index = line.find(".")
    line = line[index - 1:]
    total += float(line)
    count += 1
print("Average spam confidence:", total / count)
