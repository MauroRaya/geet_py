import sys
from commands.init   import init
from commands.add    import add
from commands.reset  import reset
from commands.status import status

command_map = {
    "init":   init,
    "add":    add,
    "reset":  reset,
    "status": status
}

def run():
    if len(sys.argv) < 2:
        print('Error: No command provided')
        sys.exit(1)

    command = sys.argv[1]
    args    = sys.argv[2:]

    if command in command_map:
        try:
            command_map[command](*args)
        except Exception as e:
            print('Error: Invalid arguments for command', e)
            sys.exit(1)
    else:
        print('Error: Unknown command', command)
        sys.exit(1)


if __name__ == '__main__':
    run()