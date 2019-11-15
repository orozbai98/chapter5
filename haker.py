import re

q = int(input().strip())
regex = r"h.*a.*c.*k.*e.*r.*r.*a.*n.*k"
compiled_regex = re.compile(regex)
for a0 in range(q):
    s = input().strip()
    result = compiled_regex.search(s)
    if result == None:
        print("NO")
    else:
        print("YES")