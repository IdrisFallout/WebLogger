import subprocess

with open('output.txt', 'w') as f:
    f.close()


def execute_command(command, output_file):
    with open(output_file, 'a') as f:  # Open the file in append mode ('a')
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            f.write(line)  # Write the line exactly as received
            f.flush()


while True:
    try:
        command = input('Enter the command (type "exit" to quit): ')
        if command.lower() == 'exit' or command.lower() == 'quit':
            break
        output_file = 'output.txt'
        execute_command(command.split(), output_file)
    except Exception as e:
        print(f"An error occurred: {e}")
        continue