# Write a program to read through the mbox-short.txt and figure out
# the distribution by hour of the day for each of the messages. You can
# pull the hour out from the 'From ' line by finding the time and then
# splitting the string a second time using a colon.
# [From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008]
# Once you have accumulated the counts for each hour, print out the
# counts, sorted by hour as shown below.
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dict_hrs = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split(" ")
        time = words[len(words) - 2]
        hrs = time.split(":")[0]
        dict_hrs[hrs] = dict_hrs.get(hrs, 0) + 1

sorted_items = sorted(list(dict_hrs.items()))
for key, val in sorted_items:
    print(key, val)