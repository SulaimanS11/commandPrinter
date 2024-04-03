import subprocess
import os

def execute_commands_from_file(file_path, location, prefix_command):
    # Check if the specified location exists and is a directory
    if not os.path.isdir(location):
        print(f"Error: The specified location ({location}) does not exist or is not a directory.")
        return

    try:
        # Open and read the file
        with open(file_path, 'r') as file:
            commands = file.readlines()
            
        # Change the current working directory to the specified location
        os.chdir(location)

        # Execute each command
        for command in commands:
            full_command = prefix_command + " " + command.strip()  # Add the prefix and remove newline characters
            print(f"Executing: {full_command}")
            result = subprocess.run(full_command, shell=True, check=True)
            print("Command executed successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error: A command failed to execute. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
file_path = 'path/to/your/commands.txt'  # Replace with the path to your .txt file
location = '/path/to/execute/in'  # Replace with your desired location
prefix_command = 'sudo'  # Replace with your desired prefix command

execute_commands_from_file(file_path, location, prefix_command)