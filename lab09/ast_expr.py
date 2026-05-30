from abc import ABC, abstractmethod

class Node(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Number(Node):
    def __init__(self, value: float):
        self.value = value

    def accept(self, visitor):
        return visitor.visit_number(self)

class BinOp(Node, ABC):
    """Clasă de bază pentru operatori binari (stânga, dreapta)."""
    def __init__(self, left: Node, right: Node):
        self.left = left
        self.right = right

class Add(BinOp):
    def accept(self, visitor):
        return visitor.visit_add(self)

class Sub(BinOp):
    def accept(self, visitor):
        return visitor.visit_sub(self)

class Mul(BinOp):
    def accept(self, visitor):
        return visitor.visit_mul(self)

class Div(BinOp):
    def accept(self, visitor):
        return visitor.visit_div(self)

class Visitor(ABC):
    @abstractmethod
    def visit_number(self, node: Number): pass
    @abstractmethod
    def visit_add(self, node: Add): pass
    @abstractmethod
    def visit_sub(self, node: Sub): pass
    @abstractmethod
    def visit_mul(self, node: Mul): pass
    @abstractmethod
    def visit_div(self, node: Div): pass


class EvaluationVisitor(Visitor):

    def visit_number(self, node: Number) -> float:
        return node.value

    def visit_add(self, node: Add) -> float:
        return node.left.accept(self) + node.right.accept(self)

    def visit_sub(self, node: Sub) -> float:
        return node.left.accept(self) - node.right.accept(self)

    def visit_mul(self, node: Mul) -> float:
        return node.left.accept(self) * node.right.accept(self)

    def visit_div(self, node: Div) -> float:
        right_val = node.right.accept(self)
        if right_val == 0:
            raise ZeroDivisionError("Împărțire la zero în AST!")
        return node.left.accept(self) / right_val


class PrintVisitor(Visitor):
    def visit_number(self, node: Number) -> str:
        return str(node.value)

    def visit_add(self, node: Add) -> str:
        return f"({node.left.accept(self)} + {node.right.accept(self)})"

    def visit_sub(self, node: Sub) -> str:
        return f"({node.left.accept(self)} - {node.right.accept(self)})"

    def visit_mul(self, node: Mul) -> str:
        return f"({node.left.accept(self)} * {node.right.accept(self)})"

    def visit_div(self, node: Div) -> str:
        return f"({node.left.accept(self)} / {node.right.accept(self)})"