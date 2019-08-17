"""
the setup to install vault_printer
"""
import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="vault_printer",
    version="0.1.0",
    author="Philip Molares",
    author_email="philipmolares@yahoo.de",
    description="A program to get all secrets from a vault servers kv_store for printing",
    entry_points={
        'console_scripts': [
            "vault_printer = vault_printer.main:main"
        ]
    },
    install_requires=["hvac", "hvac[parser]", "jinja2"],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/DerMolly/vault_printer",
    packages=setuptools.find_packages(),
    python_requires='>=3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)