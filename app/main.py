import sys
import shutil
import os

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

        if command.startswith('exit'):
            break

        elif command.startswith("echo"):
            # Extract the argument after "echo"
            argument = command[5:] if len(command) > 4 else ""
            print(argument)
            continue
        
        elif command.startswith("type"):
            sub_command = command[5:] if len(command) > 4 else ""
            if sub_command == "":
                print("")
            elif sub_command in builtin_commands:
                print(f"{sub_command} is a shell builtin")
            elif path := shutil.which(sub_command):
                print(f"{sub_command} is {path}")
            else:
                print(f"{sub_command}: not found")
            continue

        elif shutil.which(command.split(' ')[0]) != None:
            sub_commands = command.split(' ')
            os.system(f"{command[0]} {' '.join(command[1:])}")
        
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
