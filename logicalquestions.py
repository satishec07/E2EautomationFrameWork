l = [{'a': 2, 'b': 4}, {'g': 9, 'k': 90}]
# find Max Value in list of dictionaries
d = {}
for i in l:
    for k, v in i.items():
        d[k] = v

print(max(d.values()))

for k in d.values():
    if k > 9:
        print(k)

s = "abbbaaaaaaccdaaa"  # Output="ab3a6c2da3b"
n = len(s)
count = 1
d = []
for i in range(1, n):
    if s[i] == s[i - 1]:
        count += 1

    else:
        d.append(s[i - 1])
        if count > 1:
            d.append(str(count))
        count = 1
else:
    d.append(s[-1])
    if count > 1:
        d.append(str(count))
print("".join(d))

mg = 'appleakmuytrpplea'  # find largest substring
length = 0
l = []
for i in range(len(mg)):
    sub_string = ""
    for j in range(i + 1, len(mg)):
        if mg[j] not in sub_string:
            sub_string = sub_string + mg[j]

        else:
            break

    if len(sub_string) > length:
        length = len(sub_string)
        l = [sub_string]

    else:
        if length == len(sub_string):
            l.append(sub_string)

print(l)
