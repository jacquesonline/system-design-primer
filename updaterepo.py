import subprocess


def run_command(command):
    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)


# # Add the original repository as a remote
# run_command(
#     "git remote add upstream https://github.com/donnemartin/system-design-primer")

# Fetch the latest changes from the original repository
run_command("git fetch upstream")

# Checkout your main branch
run_command("git checkout master")

# Merge the changes from the original repository into your fork
run_command("git merge upstream/master")
