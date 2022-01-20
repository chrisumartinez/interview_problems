""" 
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.
In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix
Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.

Example 1:
Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Example 4:
Input: "/a/./b/../../c/"
Output: "/c"

Example 5:
Input: "/a/../../b/../c//.//"
Output: "/c"

Example 6:
Input: "/a//b////c/d//././/.."
Output: "/a/b/c" """

def simplifyPath(path):
    output = ""
    cur_level = 0
    index = 1
    counter = 0
    dirs = []

    #begin iterating through the path:
    while index < len(path)-1:
        #print("Character: ", path[index])
        if path[index] == ".":
            if path[index+1] == ".":
                if cur_level > 0:
                    cur_level -= 1
                index += 2
                if len(dirs) > 0:
                    dirs.pop()
                #print("Cur_level: ", cur_level)
                #print()
            else:
                index += 1

        elif path[index] == "/":
            #print("index to start: ", index)
            #traverse through the slashes, increase level by 1
            while path[index] == "/" and index < len(path)-1:
                index += 1
            #print("cur_level: ", cur_level)
            #print()
        else:
            #grab the directory name
            dir_name = ""
            while path[index] != "/":
                dir_name += path[index]
                index += 1

            dirs.append(dir_name)
            cur_level += 1
            index += 1
    #if were at root
    if cur_level <= 0:
        output = "/"
        return output
    # if were not
    while counter < cur_level:
        if counter != cur_level:
            output += "/"
        output += dirs.pop(0)
        counter += 1

    return output
    
# test1 = "/home/" #Expected: /home
# test2 = "/../" #Expected: /
# test3 = "/home//foo/" #Expected: /home/foo
# test4 = "/a//b////c/d//././/.." #Expected: /a/b/c
# test5 = "/a/../../b/../c//.//" #Expected: /c
# test6 = "/a/./b/../../c/" #Expected: /c

# print(simplifyPath(test1))
# print(simplifyPath(test2))
# print(simplifyPath(test3))
# print(simplifyPath(test4))
# print(simplifyPath(test5))
# print(simplifyPath(test6))
