from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from data import Data

base = Data()



while True:
    text=input("Bart: ")

    tokenizer=Lexer(text)
    tokens=tokenizer.tokenize()
    #print(tokens)

    parser = Parser(tokens)
    tree = parser.parser()
    #print(tree)

    interpreter = Interpreter(tree, base)
    result = interpreter.interpret()
    if result is not None:
       print(result)

