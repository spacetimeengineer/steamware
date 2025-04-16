from setuptools import setup, find_packages
import os
import sys

def post_install():
    
    """Ensure ~/.local/bin is in PATH for CLI access after installation."""
    user_bin = os.path.expanduser("~/.local/bin")

    # Detect shell config file (default to bash)
    shell_rc = os.path.expanduser("~/.bashrc")  # Adjust for zsh, fish, etc. if needed

    # Only update PATH if not already present
    current_path = os.environ.get("PATH", "")
    if user_bin not in current_path:
        try:
            with open(shell_rc, "a") as f:
                f.write(f'\n# Added by Steamware installation\nexport PATH="{user_bin}:$PATH"\n')
            print(f"\n✅ {user_bin} has been added to your PATH in {shell_rc}.")
            print("➡️ Run `source ~/.bashrc` or restart your terminal to apply changes.")
        except Exception as e:
            print(f"⚠️ Could not update PATH in {shell_rc}: {e}")

setup(
    name="steamware",
    version="0.1.0",
    author="Michael C Ryan",
    author_email="spacetime.engineer@gmail.com",
    description="A modular part family and hardware assembly language for 3D printing.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/spacetimeengineer/STEAMWare",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "loguru",
    ],
    entry_points={
        "console_scripts": [
            "steamware=steamware:main",
        ],
    },
    classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)

# Post-install hook
if __name__ == "__main__":
    post_install()
