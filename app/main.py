import sys
import shutil
import os

BUILTIN_COMMANDS = ["echo", "type", "exit", "pwd", "cd"]

def shell_prompt():
    # return input(f"{os.getcwd()}$ ")
    return input(f"$ ")

def handle_echo(args):
    print(' '.join(args))

def handle_type(args):
    if not args:
        print("")
        return
    
    for sub_command in args:
        if sub_command in BUILTIN_COMMANDS:
            print(f"{sub_command} is a shell builtin")
        elif path := shutil.which(sub_command):
            print(f"{sub_command} is {path}")
        else:
            print(f"{sub_command}: not found")

def handle_pwd():
    print(os.getcwd())

def handle_cd(args):
    directory = args[0]
    try:
        os.chdir(directory)
    except FileNotFoundError:
        print(f"cd: {directory}: No such file or directory")
    # print(handle_pwd())

def run_external_command(command_parts):
    try:
        os.system(' '.join(command_parts))
    except Exception as e:
        print(f"Error running command: {e}")

def execute_command(command):
    if not command.strip():
        return

    parts = command.strip().split()
    cmd, args = parts[0], parts[1:]

    if cmd == "exit":
        sys.exit(0)
    elif cmd == "echo":
        handle_echo(args)
    elif cmd == "type":
        handle_type(args)
    elif cmd == "pwd":
        handle_pwd()
    elif cmd == "cd":
        handle_cd(args)
    elif shutil.which(cmd):
        run_external_command(parts)
    else:
        print(f"{cmd}: command not found")

def main():
    while True:
        try:
            command = shell_prompt()
            execute_command(command)
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit the shell.")
        except EOFError:
            print("\nExiting.")
            break

if __name__ == "__main__":
    main()
