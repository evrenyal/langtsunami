import subprocess

def print_logo():
    logo = r"""
  _                        _____                                _ 
 | |    __ _ _ __   __ _  |_   _|__ _   _ _ __   __ _ _ __ ___ (_)
 | |   / _` | '_ \ / _` |   | |/ __| | | | '_ \ / _` | '_ ` _ \| |
 | |__| (_| | | | | (_| |   | |\__ \ |_| | | | | (_| | | | | | | |
 |_____\__,_|_| |_|\__, |   |_||___/\__,_|_| |_|\__,_|_| |_| |_|_|
                   |___/                                          
    """
    print(logo)

def display_menu():
    menu = """
    Please choose a command:
    1. Code-Switching
    2. Code-Switching with Leetspeak (1337 speak)
    3. Code-Switching with Unicode
    4. Scrambling
    5. Ollama Fuzzer
    6. Exit
    """
    print(menu)

def run_script(script_path):
    try:
        process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip(), flush=True)
        err = process.stderr.read()
        if err:
            print(f"Error: {err}", flush=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}", flush=True)
    except Exception as e:
        print(f"Unexpected error: {e}", flush=True)

def main():
    script_map = {
        '1': 'code_switch.py',
        '2': 'code_switch_leetcode.py',
        '3': 'code_switch_unicode.py',
        '4': 'code_scramble.py',
        '5': 'fuzz.py'
    }

    print_logo()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '6':
            print("Exiting...", flush=True)
            break
        elif choice in script_map:
            run_script(script_map[choice])
        else:
            print("Invalid choice. Please try again.", flush=True)

if __name__ == '__main__':
    main()
