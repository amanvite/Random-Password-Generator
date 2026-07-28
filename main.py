import string
import secrets
import math

class EnterprisePasswordGenerator:
    """
    A robust, cryptographically secure password generator.
    Guarantees character class representation, prevents ambiguity, 
    and calculates true Shannon entropy.
    """
    def __init__(self, length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True, exclude_ambiguous=True):
        if length < 8:
            raise ValueError("For adequate security, password length must be at least 8 characters.")
            
        self.length = length
        self.char_sets = {}
        
        if use_lower: self.char_sets['lower'] = string.ascii_lowercase
        if use_upper: self.char_sets['upper'] = string.ascii_uppercase
        if use_digits: self.char_sets['digits'] = string.digits
        if use_symbols: self.char_sets['symbols'] = "!@#$%^&*()_+-=[]{}|;:,.<>?"
            
        if not self.char_sets:
            raise ValueError("At least one character set must be selected.")
            
        if exclude_ambiguous:
            ambiguous = set('O0l1I')
            for key in self.char_sets:
                self.char_sets[key] = ''.join(c for c in self.char_sets[key] if c not in ambiguous)
                
        self.pool = ''.join(self.char_sets.values())
        
    def generate(self) -> str:
        """Generates the password ensuring at least one character from each selected set."""
        password_chars = []
        
        for charset in self.char_sets.values():
            if charset: 
                password_chars.append(secrets.choice(charset))
                
        remaining_length = self.length - len(password_chars)
        for _ in range(remaining_length):
            password_chars.append(secrets.choice(self.pool))
            
        sys_random = secrets.SystemRandom()
        sys_random.shuffle(password_chars)
        
        return ''.join(password_chars)
        
    def calculate_entropy(self) -> float:
        """Calculates the Shannon entropy of the password."""
        pool_size = len(self.pool)
        entropy = self.length * math.log2(pool_size)
        return round(entropy, 2)

if __name__ == "__main__":
    generator = EnterprisePasswordGenerator(length=20, exclude_ambiguous=True)
    password = generator.generate()
    entropy = generator.calculate_entropy()
    
    print(f"Generated Password : {password}")
    print(f"Character Pool Size: {len(generator.pool)} characters")
    print(f"Calculated Entropy : {entropy} bits")
    
    if entropy >= 128:
        print("Strength: CRITICAL (Suitable for master passwords and encryption keys)")
    elif entropy >= 64:
        print("Strength: STRONG (Suitable for most online accounts)")
    else:
        print("Strength: WEAK (Easily cracked by modern hardware)")