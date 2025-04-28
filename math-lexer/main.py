'''
    Base Number Class (holds a singular value)
'''
class NUMBER_NODE:
    def __init__(self, _val):
        self.val = _val

    def eval(self):
        return int(self.val)

    def __str__(self):
        return str(self.val)
'''
    Comprised of NUMBER NODE 1 and NUMBER NODE 2
'''
class ADD_NODE:
    def __init__(self, _lhs, _rhs):
        self.rhs = _rhs
        self.lhs = _lhs

    def eval(self):
        return self.lhs.eval() + self.rhs.eval()
    
    def __str__(self):
        ret = ""
        ret += str(self.lhs)
        ret += " + "
        ret += str(self.rhs)
        return ret

class SUBTRACT_NODE:
    def __init__(self, _lhs, _rhs):
        self.rhs = _rhs
        self.lhs = _lhs

    def eval(self):
        return self.lhs.eval() - self.rhs.eval()
    
    def __str__(self):
        ret = ""
        ret += str(self.lhs)
        ret += " - "
        ret += str(self.rhs)
        return ret

class MULTIPLICATION_NODE:
    def __init__(self, _lhs, _rhs):
        self.rhs = _rhs
        self.lhs = _lhs

    def eval(self):
        return self.lhs.eval() * self.rhs.eval()
    
    def __str__(self):
        ret = ""
        ret += str(self.lhs)
        ret += " * "
        ret += str(self.rhs)
        return ret

class DIVISION_NODE:
    def __init__(self, _lhs, _rhs):
        self.rhs = _rhs
        self.lhs = _lhs

    def eval(self):
        return self.lhs.eval() / self.rhs.eval()

    def __str__(self):
        ret = ""
        ret += str(self.lhs)
        ret += " / "
        ret += str(self.rhs)
        return ret

class EXPONENT_NODE:
    def __init__(self, _lhs, _rhs):
        self.rhs = _rhs
        self.lhs = _lhs

    def eval(self):
        return self.lhs.eval() ** self.rhs.eval()

    def __str__(self):
        ret = ""
        ret += str(self.lhs)
        ret += "^("
        ret += str(self.rhs)
        ret += ")"
        return ret


def parse(expr, operation_map):
    x = 0
    while(x < len(expr)):

        item = expr[x]

        if isinstance(item, str) and item in operation_map:

            operation = operation_map[item]        
            lhs = expr[x - 1]
            rhs = expr[x + 1]

            if isinstance(lhs,str):
                lhs = NUMBER_NODE(lhs)
            
            if isinstance(rhs,str):
                rhs = NUMBER_NODE(rhs)
                       
            operation_node = operation(lhs,rhs)   
            expr.pop(x + 1)
            expr.pop(x)
            expr[x - 1] = operation_node        

            x = 0
        else:
            x += 1

    return expr

def prep_input(expression_list):
    ret = []
    x = 0
    while (x < len(expression_list)):

        if expression_list[x] == " ":
            x += 1
            continue

        if expression_list[x].isnumeric():
            curr = ""
            while ( x < len(expression_list) and expression_list[x].isnumeric()):
                curr += expression_list[x]
                x += 1
            ret.append(curr)

        else:
            ret.append(expression_list[x])
            x += 1

    return ret


'''
    Precedence Levels defined
'''
level_0_operation = {"+" : ADD_NODE, "-" : SUBTRACT_NODE}
level_1_operation = {"*" : MULTIPLICATION_NODE, "/" : DIVISION_NODE}
level_2_operation = {"^" : EXPONENT_NODE}

while(True):
    
    expr = input("Input Expression: ").lower()

    if expr == "exit":
        break

    expression_list = prep_input(expr)
    expression_list = parse(expression_list, level_2_operation)
    expression_list = parse(expression_list, level_1_operation)
    expression_list = parse(expression_list, level_0_operation)

    for expr in expression_list:
        print(expr)
        print(expr.eval())


   















