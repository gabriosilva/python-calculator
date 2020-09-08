import operator

banner      = print("[+] Welcome to this simple calculator\n")
operationInput   = input("[I] Type any value to be calculated and its function separated by a comma. ex.: (1,+,1): ")

#define the object values
class opVal:
    def __init__(self, raw, splitedBy):
        self.ops = ops = {"+":operator.add, "-":operator.sub, "*":operator.mul, "**":operator.pow}
        self.raw = raw
        self.splitedBy = splitedBy

#define the class that splits the input and processes it after
class final(opVal):
    def __init__(self, raw, splitedBy):
        super().__init__(raw, splitedBy)

        def breakInput(raw,splitedBy):
            return raw.split(str(splitedBy))
    
        def process(splitedValue,ops):
            v0 = int(splitedValue[0])
            v1 = int(splitedValue[2])
            op = splitedValue[1]
            return  ops[op](v0,v1)

        self.splitedValue = breakInput(self.raw,self.splitedBy)
        self.result = process(self.splitedValue,self.ops)

oper = final(operationInput,',')
result = oper.result
print(result)