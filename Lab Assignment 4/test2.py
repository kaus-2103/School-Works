def check(expr):
    stack = []
 
    # Traversing the Expression
    for i in expr:
        if i in ["(", "{", "["]:
 
            # Push the element in the stack
            stack = stack + [i]
        else:
 
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if i != ")":
                    return False
            if current_char == '{':
                if i != "}":
                    return False
            if current_char == '[':
                if i != "]":
                    return False

    # Check Empty Stack
    if stack:
        return False
    return True

     
list = "{()}[]"
 
    # Function call
if check(list):
    print("The expression is correct")
else:
    print("The expression is not correct")

 