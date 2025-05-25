def read_DFA(file_path):
    f=open(file_path, "r")
    lines=[line.strip() for line in f.readlines() if not line.strip().startswith("#")]
    f.close()
        
    if not lines:
        print("DFA file is empty! Please create a valid DFA first.")
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
                    rules[(current_state, symbol)]=next_state
                i+=1

        elif line=="~Start~":
            START=lines[i+1]
            i+=1

        elif line=="~Stop~":
            i+=1
            while i<len(lines) and lines[i]!="":
                STOP.append(lines[i])
                i+=1

        i+=1

    return states, sigma, rules, START, STOP


def validate_string(input_string, start_state, accept_states, transitions):
    current_state=start_state
    has_spoon=False
    spoon_location="KITCHEN"
    reached_exit=False

    for symbol in input_string.upper().split():
        if symbol=="PICK":
            if current_state==spoon_location:
                has_spoon=True
                spoon_location=None
            continue

        elif symbol=="DROP":
            if has_spoon:
                has_spoon=False
                spoon_location=current_state
            continue

        elif (current_state, symbol) in transitions:
            current_state=transitions[(current_state, symbol)]
            if current_state in accept_states and has_spoon:
                reached_exit=True

    return reached_exit

def display_dfa(states, sigma, rules, start_state, stop_states):
    print("\n--- DFA Details ---")
    print("States:", ", ".join(states))
    print("Sigma (Alphabet):", ", ".join(sigma))
    print("Start State:", start_state)
    print("Stop States:", ", ".join(stop_states))

    print("\nTransition Rules:")
    for (state, symbol), next_state in rules.items():
        print(f"  {state} --{symbol}--> {next_state}")


def main():
    file_path="LFA.txt"

    while True:
        print("\n--- DFA Interactive Menu ---")
        print("1. Validate Strings")
        print("2. Display DFA")
        print("3. Exit")

        choice=input("Choose an option: ").strip()
        
        if choice=="1":
            states, sigma, rules, START, STOP = read_DFA(file_path)
            if not states:
                print("DFA file is invalid or empty. Please create a DFA first.")
                continue

            while True:
                user_input=input("\nEnter a string to validate (or 'exit' to go back): ").strip()
                if user_input.lower()=="exit":
                    break

                result=validate_string(user_input, START, STOP, rules)
                print(f"➡ String '{user_input}' is {'✅ Accepted' if result else '❌ Rejected'}")

        elif choice=="2":
            states, sigma, rules, START, STOP = read_DFA(file_path)
            if states:
                display_dfa(states, sigma, rules, START, STOP)
            else:
                print("DFA file is empty or invalid. Please create a valid DFA first.")
        
        elif choice=="3":
            print("Goodbye!")
            break

        else:
            print("Invalid option! Please enter 1, 2, or 3.")

main()
