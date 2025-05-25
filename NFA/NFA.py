def read_NFA(file_path):
    f=open(file_path, "r")
    lines=[line.strip() for line in f.readlines() if not line.strip().startswith("#")]
    f.close()

    if not lines:
        print("NFA file is empty! Please create a valid NFA first.")
        return None, None, None, None, None

    states, sigma, rules, START, STOP = [], [], {}, None, []

    i=0
    while i<len(lines):
        line=lines[i]

        if line=="~States~":
            i+=1
            while i<len(lines) and lines[i]!="":
                states.append(lines[i])
                i+=1

        elif line=="~Sigma~":
            i+=1
            while i<len(lines) and lines[i]!="":
                sigma.append(lines[i])
                i+=1

        elif line=="~Rules~":
            i+=1
            while i<len(lines) and lines[i]!="":
                parts=lines[i].split()
                if len(parts)==3:
                    current_state, symbol, next_state = parts
                    if (current_state, symbol) not in rules:
                        rules[(current_state, symbol)] = []
                    rules[(current_state, symbol)].append(next_state)
                i+=1

        elif line=="~Start~":
            START=lines[i + 1]
            i+=1

        elif line=="~Stop~":
            i+=1
            while i<len(lines) and lines[i]!="":
                STOP.append(lines[i])
                i+=1

        i+=1

    return states, sigma, rules, START, STOP


def get_epsilon_reachable_states(states, transitions):
    reachable_states=set(states)
    changed=True

    while changed:
        changed=False
        for state in list(reachable_states):
            for next_state in transitions.get((state, "EPSILON"), []):
                if next_state not in reachable_states:
                    reachable_states.add(next_state)
                    changed=True

    return reachable_states


def validate_string(input_string, start_state, accept_states, transitions):
    current_states=get_epsilon_reachable_states([start_state], transitions)

    for symbol in input_string:
        next_states=set()
        for state in current_states:
            for target in transitions.get((state, symbol), []):
                next_states.add(target)
        current_states=get_epsilon_reachable_states(next_states, transitions)

    return any(state in accept_states for state in current_states)


def display_nfa(states, sigma, rules, start_state, stop_states):
    print("\n--- NFA Details ---")
    print("States:", ", ".join(states))
    print("Sigma (Alphabet):", ", ".join(sigma))
    print("Start State:", start_state)
    print("Stop States:", ", ".join(stop_states))

    print("\nTransition Rules:")
    for (state, symbol), next_states in rules.items():
        for next_state in next_states:
            print(f"  {state} --{symbol}--> {next_state}")


def main():
    file_path="NFA.txt"

    while True:
        print("\n--- NFA Interactive Menu ---")
        print("1. Validate Strings")
        print("2. Display NFA")
        print("3. Exit")

        choice=input("Choose an option: ").strip()

        if choice=="1":
            states, sigma, rules, START, STOP = read_NFA(file_path)
            if not states:
                print("NFA file is invalid or empty. Please create an NFA first.")
                continue

            while True:
                user_input=input("\nEnter a string to validate (or 'exit' to go back): ").strip()
                if user_input.lower()=="exit":
                    break

                result=validate_string(user_input, START, STOP, rules)
                print(f"➡ String '{user_input}' is {'✅ Accepted' if result else '❌ Rejected'}")

        elif choice=="2":
            states, sigma, rules, START, STOP = read_NFA(file_path)
            if states:
                display_nfa(states, sigma, rules, START, STOP)
            else:
                print("NFA file is empty or invalid. Please create a valid NFA first.")

        elif choice=="3":
            print("Goodbye!")
            break

        else:
            print("Invalid option! Please enter 1, 2, or 3.")



main()
