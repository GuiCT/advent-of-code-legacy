from typing import Optional
import unittest
import ctypes

wire_map: dict[str, int] = dict()


def safe_int_cast(input: str) -> Optional[int]:
    try:
        v = int(input)
        return v
    except ValueError:
        return


class Operation:
    def __init__(self, symbols: list[str], name: str = ''):
        self.name = name
        length = len(symbols)
        assert len(symbols) <= 3
        if length == 1:
            self.expression = [symbols[0]]
        elif length == 2 and symbols[0] == 'NOT':
            self.expression = [symbols[1], lambda v: ctypes.c_uint16(~v).value]
            self.expression.append(1)
        elif length == 3:
            self.expression = list()
            self.expression.append(symbols[0])
            self.expression.append(symbols[2])
            match symbols[1]:
                case 'AND':
                    self.expression.append(lambda u, v: u & v)
                case 'OR':
                    self.expression.append(lambda u, v: u | v)
                case 'LSHIFT':
                    self.expression.append(lambda u, v: u << v)
                case 'RSHIFT':
                    self.expression.append(lambda u, v: u >> v)
                case _:
                    raise ValueError('Invalid operation')
            self.expression.append(2)
        else:
            raise ValueError('Invalid operation')

    def _evaluate(self) -> Optional[int]:
        length = len(self.expression)
        stack: list[int] = list()
        i = 0
        while i < length:
            current_is_function = callable(self.expression[i])
            current_is_int = isinstance(self.expression[i], int)
            if current_is_function:
                num_args = int(self.expression[i + 1])
                # Remove last args
                stack_args = stack[-num_args:]
                # Apply function with args, put in the position
                fun_value = self.expression[i](*stack_args)  # type: ignore
                stack.append(fun_value)
                del stack[-1-num_args:-1]
            elif current_is_int:
                pass
            else:
                val: Optional[int] = safe_int_cast(self.expression[i])
                if val is None:
                    val = wire_map.get(self.expression[i], None)
                    if val is None:
                        return None
                stack.append(val)
            i += 1
        return stack[0]
    
    def try_save(self) -> bool:
        if (val := self._evaluate()) is not None:
            wire_map[self.name] = val
            return True
        else:
            return False

class TestOperation(unittest.TestCase):
    def test_evaluation(self):
        op1 = Operation(['123', 'AND', '456'])
        self.assertEqual(op1._evaluate(), 72)
        op2 = Operation(['123', 'OR', '456'])
        self.assertEqual(op2._evaluate(), 507)
        op3 = Operation(['123', 'LSHIFT', '2'])
        self.assertEqual(op3._evaluate(), 492)
        op4 = Operation(['456', 'RSHIFT', '2'])
        self.assertEqual(op4._evaluate(), 114)
        op5 = Operation(['NOT', '123'])
        self.assertEqual(op5._evaluate(), 65412)
        op6 = Operation(['NOT', '456'])
        self.assertEqual(op6._evaluate(), 65079)

    def test_fetch_from_map(self):
        wire_map['x'] = 123
        wire_map['y'] = 456
        op1 = Operation(['x', 'AND', 'y'])
        self.assertEqual(op1._evaluate(), 72)
        op2 = Operation(['x', 'OR', 'y'])
        self.assertEqual(op2._evaluate(), 507)
        op3 = Operation(['x', 'LSHIFT', '2'])
        self.assertEqual(op3._evaluate(), 492)
        op4 = Operation(['y', 'RSHIFT', '2'])
        self.assertEqual(op4._evaluate(), 114)
        op5 = Operation(['NOT', 'x'])
        self.assertEqual(op5._evaluate(), 65412)
        op6 = Operation(['NOT', 'y'])
        self.assertEqual(op6._evaluate(), 65079)
        wire_map.clear()

def parse_line(line: str) -> tuple[str, list[str]]:
    lhs, name = line.split(' -> ')
    symbols = lhs.split(' ')
    return name, symbols

class TestLineParse(unittest.TestCase):
    def test_line_parsing(self):
        name, symbols_parsed = parse_line('x RSHIFT 5 -> aa')
        self.assertEqual(name, 'aa')
        self.assertEqual(symbols_parsed, ['x', 'RSHIFT', '5'])

if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        lines = f.readlines()
    operations_queue: list[Operation] = []
    for line in lines:
        name, symbols = parse_line(line.strip())
        operations_queue.append(Operation(symbols, name))
    while len(operations_queue) > 0:
        current_operation = operations_queue[0]
        operations_queue.pop(0)
        if not current_operation.try_save():
            operations_queue.append(current_operation)
        else:
            if (val := wire_map.get('a', None)) is not None:
                print(f'Result for wire a: {val}')
                break
    # For the second part, i literally just override the value of the wire b
    # In my case:
    # 14146 -> b became 956 -> b
    # Then recompute.