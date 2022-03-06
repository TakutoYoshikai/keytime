from setuptools import setup, find_packages

setup(
    name = 'keytime',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/keytime.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = "keyboard time logger",
    install_requires = ['setuptools', "pyxhook"],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "keytime = keytime.keytime:main",
        ]
    }
)
