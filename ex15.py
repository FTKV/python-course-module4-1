import sys

# print("-"*100)

# print(sys.argv)

# print("-"*100)

try:
    path = sys.argv[1]
    print(path)

except IndexError as e:
    print(f"Take path to folder as param. {e}")