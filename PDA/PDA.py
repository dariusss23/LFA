def read_PDA(file_path):
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines() if not line.strip().startswith("#")]

    if not lines:
        print("PDA file is empty!")
        return None, None, None, None, None, None

    states, sigma, gamma, rules, START, STOP = [], [], [], {}, None, []
    i = 0

    while i < len(lines):
        line = lines[i]
        if line == "~States~":
            i += 1
            while i < len(lines) and lines[i] != "" and not lines[i].startswith("~"):
                states.append(lines[i])
                i += 1
        elif line == "~Sigma~":
            i += 1
            while i < len(lines) and lines[i] != "" and not lines[i].startswith("~"):
                sigma.append(lines[i])
                i += 1
        elif line == "~Gamma~":
            i += 1
            while i < len(lines) and lines[i] != "" and not lines[i].startswith("~"):
                gamma.append(lines[i])
                i += 1
        elif line == "~Rules~":
            i += 1
            while i < len(lines) and lines[i] != "" and not lines[i].startswith("~"):
                parts = lines[i].split()
                if len(parts) == 5:
                    current_state, input_symbol, pop_symbol, push_symbol, next_state = parts
                    input_symbol = "" if input_symbol == "EPSILON" else input_symbol
                    pop_symbol = "" if pop_symbol == "EPSILON" else pop_symbol
                    push_symbol = "" if push_symbol == "EPSILON" else push_symbol

                    key = (current_state, input_symbol, pop_symbol)
                    if key not in rules:
                        rules[key] = []
                    rules[key].append((push_symbol, next_state))
                i += 1
        elif line == "~Start~":
            if i + 1 < len(lines):
                START = lines[i + 1]
            i += 1
        elif line == "~Stop~":
            i += 1
            while i < len(lines) and lines[i] != "" and not lines[i].startswith("~"):
                STOP.append(lines[i])
                i += 1
        i += 1

    return states, sigma, gamma, rules, START, STOP


from collections import deque

def validate_string_PDA(input_string, start_state, accept_states, rules):
    queue = deque()
    queue.append((start_state, input_string, []))  # (stare curentă, input rămas, stivă)
    
    while queue:
        current_state, remaining_input, stack = queue.popleft()

        if not remaining_input and current_state in accept_states and not stack:
            return True

        for (state, symbol, pop_symbol), transitions in rules.items():
            if state != current_state:
                continue

            input_symbol = remaining_input[0] if remaining_input else ""
            rest_input = remaining_input[1:] if remaining_input else remaining_input

            if symbol == "":
                if pop_symbol == "" or (stack and stack[-1] == pop_symbol):
                    new_stack = stack[:]
                    if pop_symbol != "":
                        new_stack.pop()
                    for push_symbol, next_state in transitions:
                        temp_stack = new_stack[:]
                        if push_symbol != "":
                            temp_stack.append(push_symbol)
                        queue.append((next_state, remaining_input, temp_stack))

            elif symbol == input_symbol:
                if pop_symbol == "" or (stack and stack[-1] == pop_symbol):
                    new_stack = stack[:]
                    if pop_symbol != "":
                        new_stack.pop()
                    for push_symbol, next_state in transitions:
                        temp_stack = new_stack[:]
                        if push_symbol != "":
                            temp_stack.append(push_symbol)
                        queue.append((next_state, rest_input, temp_stack))

    return False




def display_PDA(states, sigma, gamma, rules, start_state, stop_states):
    print("\n--- PDA Details ---")
    print("States:", ", ".join(states))
    print("Input Alphabet (Σ):", ", ".join(sigma))
    print("Stack Alphabet (Γ):", ", ".join(gamma))
    print("Start State:", start_state)
    print("Accept States:", ", ".join(stop_states))
    print("\nTransition Rules:")
    for (state, input_sym, pop_sym), transitions in rules.items():
        input_display = input_sym if input_sym else "ε"
        pop_display = pop_sym if pop_sym else "ε"
        for push_sym, next_state in transitions:
            push_display = push_sym if push_sym else "ε"
            print(f"  {state} --{input_display},{pop_display}/{push_display}--> {next_state}")


def main():
    file_path = "PDA.txt"

    while True:
        print("\n--- PDA Interactive Menu ---")
        print("1. Validate Strings")
        print("2. Display PDA")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            states, sigma, gamma, rules, START, STOP = read_PDA(file_path)
            if not states:
                print("PDA file is invalid or empty.")
                continue

            while True:
                user_input = input("\nEnter a string to validate (or 'exit' to go back): ").strip()
                if user_input.lower() == "exit":
                    break

                result = validate_string_PDA(user_input, START, STOP, rules)
                print(f"String '{user_input}' is {'✅ Accepted' if result else '❌ Rejected'}")

        elif choice == "2":
            states, sigma, gamma, rules, START, STOP = read_PDA(file_path)
            if states:
                display_PDA(states, sigma, gamma, rules, START, STOP)
            else:
                print("PDA file is empty or invalid.")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please enter 1, 2, or 3.")



main()
