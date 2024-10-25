# Password Generator

## Overview
This Python-based Password Generator is a robust tool designed to help users create secure passwords and check existing ones for security vulnerabilities. It offers three core functionalities:
1. **Generate Random Passwords** with customizable character options.
2. **Check Password Security** by comparing against a list of known compromised passwords.
3. **Generate Memorable, Strong Passwords** by transforming existing passwords with secure substitutions.

## Features
- **Random Password Generation**: Users can create a strong password of specified length, choosing whether to include uppercase letters, lowercase letters, numbers, and symbols.
- **Password Security Check**: Validates if a password is present in a list of known compromised passwords (`10-million-password-list-top-1000000.txt`) and suggests strengthening if found compromised.
- **Memorable Password Conversion**: Transforms an existing password or word into a strong password by substituting certain characters with more secure alternatives, e.g., `a` with `@` and `s` with `$`.

## Requirements

- **Python**: Version 3.12.5 or higher.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/niranjan-bhol/password-generator.git
   cd password-generator
