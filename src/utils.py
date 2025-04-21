import random
import string

def generate_random_string(n):
    """
    Generate a random string of length n.
    
    Args:
        n (int): Length of the random string to generate
        
    Returns:
        str: Random string containing uppercase letters, lowercase letters, and digits
    """
    # Define the character set to choose from
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    
    # Generate the random string
    random_string = ''.join(random.choice(characters) for _ in range(n))
    
    return random_string