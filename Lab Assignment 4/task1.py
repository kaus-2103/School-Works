def check(list):
    stack = []
    counter = 0
    for i in list:
        if i in ["(","{","["]:
            stack= stack + [i]
        else:
            if not stack and i==')':
                print("Missing ( expected at",counter)
                return False
            if not stack and i=='}':
                print("Missing { expected at",counter)
                return False
            if not stack and i==']':
                print("Missing [ expected at",counter)
                return False
            c = stack.pop()
            if c == '(':
                l = 0
                for j in list:
                    if i ==")":
                        l = l+1
                if l==0:
                    print("The expression ) is missing in ",counter)
                    return False
            if c == '{':
                for i in list:
                    l = 0
                    if i =="}":
                        l = l+1
                    if l==0:
                        print("The expression } is missing in ",counter)
                        return False
            if c == '[':
                for j in list:
                    l = 0
                    if i =="]":
                        l = l+1
                    if l==0:
                        print("The expression ] is missing in ",counter)
                        return False
        counter = counter + 1
    if stack:
        print("Expected ",i," at ",counter)
        return False
    return True
    def pop():
        p = stack[:-1]
        t = p[0]
        return t

list = ")"
if check(list):
    print("The Expression is correct")
else:
    print("The expression is not correct.")