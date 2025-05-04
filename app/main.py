import sys

builtin_commands = [
    "echo",
    "type",
    "exit"
]

def main():
    while True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        # Wait for user input
        command = input()

        if command.startswith("echo"):
            # Extract the argument after "echo"
            argument = command[5:] if len(command) > 4 else ""
            print(argument)
            continue
        
        if command.startswith("type"):
            sub_command = command[5:] if len(command) > 4 else ""
            if sub_command == "":
                print("")
            elif sub_command in builtin_commands:
                print(f"{sub_command} is a shell builtin")
            else:
                print(f"{sub_command}: not found")
            continue
        
        if command == "exit 0" or command == "exit":
            break

        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
