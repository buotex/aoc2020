from dataclasses import dataclass

@dataclass
class State:
    pointer = 0
    acc = 0

def parse_instruction(data, state):
    tokens = data[state.pointer]
    instruction, argument = tokens.split()
    argument = int(argument)
    if instruction == "jmp":
        state.pointer += argument
    else:
        state.pointer += 1
    if instruction == "acc":
        state.acc += argument

    return state


def pc(data, state=None):
    if state is None:
        state = State()
    used_pointers = set()
    graceful_terminate = True
    while True:
        if state.pointer >= len(data):
            graceful_terminate = True
            break
        if state.pointer in used_pointers:
            graceful_terminate = False
            break
        used_pointers.add(state.pointer)
        state = parse_instruction(data, state)
    #data = list(map(subfunc, data))
    return state, graceful_terminate
