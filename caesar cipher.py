import sys

key = input()
text = raw_input()
result = ""
for let in text:
    let = chr(ord(let) + key)if ord(let) + key <= ord('Z') else chr(ord(let) + key - 26)
    result += let

# result += [let for let in text]
print result