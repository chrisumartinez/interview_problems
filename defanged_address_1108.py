# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

# Example 1:

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:

# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"


def defangIPaddr(address):
    defanged_address = []
    for i in range(0, len(address)):
        if address[i] == ".":
            defanged_address.append("[.]")
        else:
            defanged_address.append(address[i])
    str1 = "".join(defanged_address)
    return str1


address = "1.1.1.1"  # Expect "1[.]1[.]1[.]1"
address_two = "255.100.50.0"  # Expect "255[.]100[.]50[.]0"

print(defangIPaddr(address))
print(defangIPaddr(address_two))
