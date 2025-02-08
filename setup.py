import subprocess
import sys


def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError:
        print(f"Failed to run: {command}")
        sys.exit(1)


def main():
    print("Installing dependencies...")
    run_command("poetry install")

    print("Installing pre-commit hooks...")
    run_command("pre-commit install")

    print("Setup complete!")


if __name__ == "__main__":
    main()
