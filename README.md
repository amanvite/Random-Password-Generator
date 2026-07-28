# Enterprise Python Password Generator

A robust, cryptographically secure password generator written in Python. This tool goes beyond naive `random` scripts by guaranteeing character class representation, preventing ambiguity (excluding confusing characters like `l` and `1`), and calculating true Shannon entropy in bits.

## Features

*   **Cryptographically Secure:** Uses Python's built-in `secrets` module (CSPRNG) instead of the predictable `random` module.
*   **Guaranteed Character Sets:** Ensures that at least one character from every selected set (uppercase, lowercase, numbers, symbols) is actually included in the final string.
*   **Cryptographic Shuffling:** Masks the position of guaranteed characters to prevent predictable placement (e.g., stopping the tool from always putting the guaranteed number at the beginning).
*   **Ambiguity Prevention:** Optionally removes visually similar characters (`l`, `1`, `I`, `O`, `0`) to prevent manual-entry and reading errors.
*   **Math-Based Verification:** Calculates the exact Shannon entropy of the generated string so you can verify its true mathematical strength.

## Requirements

*   Python 3.6 or higher (relies on the built-in `secrets` module introduced in 3.6).
*   No external dependencies or `pip` installs required!

## Installation

Simply copy the `EnterprisePasswordGenerator` class into your Python project or run the script directly from your terminal.

## Usage

```python
from password_generator import EnterprisePasswordGenerator

# Initialize the generator (default length 16)
# Exclude ambiguous characters by default for readability
generator = EnterprisePasswordGenerator(length=20, exclude_ambiguous=True)

# Generate the password
password = generator.generate()

# Calculate cryptographic strength
entropy = generator.calculate_entropy()

print(f"Generated Password : {password}")
print(f"Character Pool Size: {len(generator.pool)} characters")
print(f"Calculated Entropy : {entropy} bits")
```

### Customizing the Generator

You can toggle specific character sets on or off when initializing the class:

```python
# Generate a 12-character PIN code (numbers only)
pin_generator = EnterprisePasswordGenerator(
    length=12, 
    use_upper=False, 
    use_lower=False, 
    use_symbols=False
)
```

## Understanding Entropy Scores

Security is based on mathematical probability, not arbitrary rules. This tool calculates Shannon entropy using the formula:

`E = L * log2(R)`

Where `L` is the password length and `R` is the size of the active character pool. 

*   **< 64 bits (WEAK):** Vulnerable to targeted brute-force attacks by modern hardware.
*   **64 - 127 bits (STRONG):** Highly secure. Suitable for most online accounts and daily use.
*   **128+ bits (CRITICAL):** Uncrackable by current technology. Suitable for master passwords, encryption keys, and highly sensitive data.

## License

This project is licensed under the MIT License - feel free to use, modify, and distribute it in your own personal or commercial projects.
