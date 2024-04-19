# Write a function that removes the spaces from the string, then return the resultant string.
# Your input will always be a string that only contains spaces, numbers, and letters.

# Examples:

# Input -> Output
# "8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
# "8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
# "8aaaaa dddd r     " -> "8aaaaaddddr"
# "                 " -> ""


#define a function that takes in a string

# I can look at each character individually, and if its not a string, add it to an output string that i return
#-- use a for loop to loop over each character ---
#-- check if the character is space ----
#-- if not add to output



# replace all the spaces with empty strings

#split the string would split on space into a list with no spaces, then join that split string


#return that string without any spaces

def solution(astring):
    output = ''
    for char in astring:
        if char != ' ':
            output += char
    return output


print(solution("8 j 8   mBliB8g  imjB8B8  jl  B"))