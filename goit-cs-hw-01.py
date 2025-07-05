####### Тема 1. Вступ до архітектури комп'ютерів
####### Тема 2. Вступ до компіляторів та інтерпретаторів

'''
Завдання 2

У вас є початковий код інтерпретатора з конспекту, який вміє обробляти арифметичні вирази, включаючи операції додавання та віднімання (посилання на папку репозиторію до конспекту).

Ваше завдання полягає в розширенні цього інтерпретатора таким чином, щоб він також підтримував операції множення та ділення, а також коректно обробляв вирази, що містять дужки.



Покрокова інструкція



1. Розширте лексер Lexer

Додайте нові типи токенів для операцій множення MUL, ділення DIV та дужок, які відкривають LPAREN та закривають RPAREN частину арифметичного виразу.
Модифікуйте метод get_next_token класу Lexer так, щоб він розпізнавав ці нові символи.
2. Модифікуйте парсер Parser

Додайте метод factor для обробки чисел та виразів у дужках.
Змініть метод term, щоб він включав обробку множення та ділення.
Внесіть відповідні зміни в метод expr для підтримки нової ієрархії операцій.
3. Оновіть Інтерпретатор Interpreter

Доповніть метод visit_BinOp у класі Interpreter так, щоб він міг обробляти операції множення та ділення.
4. Тестування

Перевірте коректність роботи інтерпретатора на різних арифметичних виразах, включаючи вирази з дужками, наприклад (2 + 3) * 4 повинно дати результат 20.


Критерії прийняття

- Додано нові типи токенів для операцій множення MUL, ділення DIV та дужок.

- Модифіковано метод get_next_token, щоб він розпізнавав нові символи.

- Модифіковано парсер Parser .

- Оновлено Інтерпретатор так, щоб він підтримував операції множення та ділення, обробляв вирази з дужками.

- Інтерпретатор працює.
'''

#====================
### Лексичний аналіз
#====================

class LexicalError(Exception):
    pass


class ParsingError(Exception):
    pass


class EvaluationError(Exception):
    pass


class TokenType:
    INTEGER = "INTEGER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    EOF = "EOF"  # Означає кінець вхідного рядка
    # 1.1 Розширте лексер Lexer. Додайте нові типи токенів для операцій множення MUL, ділення DIV та дужок, які відкривають LPAREN та закривають RPAREN частину арифметичного виразу.
    MUL = "*"
    DIV = "/"
    LPAREN = "("
    RPAREN = ")"    

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {repr(self.value)})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        """Переміщуємо 'вказівник' на наступний символ вхідного рядка"""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Означає кінець введення
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        """Пропускаємо пробільні символи."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Повертаємо ціле число, зібране з послідовності цифр."""
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """Лексичний аналізатор, що розбиває вхідний рядок на токени."""
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(TokenType.INTEGER, self.integer())

            if self.current_char == "+":
                self.advance()
                return Token(TokenType.PLUS, "+")

            if self.current_char == "-":
                self.advance()
                return Token(TokenType.MINUS, "-")
            
            # 1.2.  Розширте лексер Lexer. Модифікуйте метод get_next_token класу Lexer так, щоб він розпізнавав ці нові символи.
            if self.current_char == "*":
                self.advance()
                return Token(TokenType.MUL, "*")
            
            if self.current_char == "/":
                self.advance()
                return Token(TokenType.DIV, "/")
            
            if self.current_char == "(":
                self.advance()
                return Token(TokenType.LPAREN, "(")
            
            if self.current_char == ")":
                self.advance()
                return Token(TokenType.RPAREN, ")")

            raise LexicalError("Помилка лексичного аналізу")

        return Token(TokenType.EOF, None)


#========================================
### Створення парсера (синтаксичний аналіз)
#========================================

class AST:
    pass


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise ParsingError("Помилка синтаксичного аналізу")

    def eat(self, token_type):
        """
        Порівнюємо поточний токен з очікуваним токеном і, якщо вони збігаються,
        'поглинаємо' його і переходимо до наступного токена.
        """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    ## 2.1. Модифікуйте парсер Parser. Додайте метод factor для обробки чисел та виразів у дужках.

    def factor(self):
        token = self.current_token
        if token.type == TokenType.INTEGER:
            self.eat(TokenType.INTEGER)
            return Num(token)
        # якщо дужки
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node
        else:
            self.error()
    
    ## 2.2. Модифікуйте парсер Parser. Змініть метод term, щоб він включав обробку множення та ділення.
    def term(self):
        """Парсер для 'term' правил граматики. У нашому випадку - це цілі числа."""
        node = self.factor()
        while self.current_token.type in (TokenType.MUL, TokenType.DIV):
            token = self.current_token

            # Обробляємо токени множення та ділення
            if token.type == TokenType.MUL:
                self.eat(TokenType.MUL)
            elif token.type == TokenType.DIV:
                self.eat(TokenType.DIV)
            node = BinOp(left=node, op=token, right=self.factor())
        return node

    ## 2.3. Модифікуйте парсер Parser. Внесіть відповідні зміни в метод expr для підтримки нової ієрархії операцій.
    def expr(self):
        """Парсер для арифметичних виразів."""
        node = self.term()

        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            elif token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)
            node = BinOp(left=node, op=token, right=self.term())
        return node


def print_ast(node, level=0):
    indent = "  " * level
    if isinstance(node, Num):
        print(f"{indent}Num({node.value})")
    elif isinstance(node, BinOp):
        print(f"{indent}BinOp:")
        print(f"{indent}  left: ")
        print_ast(node.left, level + 2)
        print(f"{indent}  op: {node.op.type}")
        print(f"{indent}  right: ")
        print_ast(node.right, level + 2)
    else:
        print(f"{indent}Unknown node type: {type(node)}")


#========================================
### Створення інтерпретатора
#========================================

class Interpreter:
    def __init__(self, parser):
        self.parser = parser

## 3. Оновіть Інтерпретатор Interpreter. Доповніть метод visit_BinOp у класі Interpreter так, щоб він міг обробляти операції множення та ділення.
    def visit_BinOp(self, node):
        if node.op.type == TokenType.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == TokenType.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == TokenType.MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == TokenType.DIV:
            right = self.visit(node.right)
            if right == 0:
                raise EvaluationError("Ділення на нуль")
            return self.visit(node.left) / right

    def visit_Num(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.expr()
        return self.visit(tree)

    def visit(self, node):
        method_name = "visit_" + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f"Немає методу visit_{type(node).__name__}")


def main():
    while True:
        try:
            text = input('Введіть вираз (або "exit" для виходу): ')
            if text.lower() == "exit":
                print("Вихід із програми.")
                break
            lexer = Lexer(text)
            parser = Parser(lexer)
            interpreter = Interpreter(parser)
            result = interpreter.interpret()
            print(result)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
