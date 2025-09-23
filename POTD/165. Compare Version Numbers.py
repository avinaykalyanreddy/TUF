"""
Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
"""

version1 = "1.2"; version2 = "1.10"


v1 = version1.split(".")
v2 = version2.split(".")

n1 = len(v1)
n2 = len(v2)

max_len = max(n1,n2)

for i in range(max_len):

    val1 = int(v1[i]) if i < n1 else 0
    val2 = int(v2[i] ) if i < n2 else 0

    if val1 < val2:

        print(-1)

    elif val1 > val2:

        print(1)

print(0)