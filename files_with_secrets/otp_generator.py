import hmac
import hashlib
import base64
import time
from secrets import token_hex

# Symmetric encryption key (for OTP generation)
SECRET_KEY = "b1c29f883ba84c839fa67a8b6a12c58e"

def generate_otp(secret: str, interval: int = 30) -> str:
    """
    Generate a time-based one-time password (TOTP).
    
    :param secret: Shared secret key used for OTP generation.
    :param interval: Time step in seconds (default is 30s).
    :return: Generated OTP as a 6-digit string.
    """
    # Get the current time step
    time_step = int(time.time()) // interval
    
    # Encode the secret and time step
    key = base64.b32decode(secret)
    message = time_step.to_bytes(8, 'big')
    
    # Generate HMAC-SHA1 hash
    hmac_hash = hmac.new(key, message, hashlib.sha1).digest()
    
    # Dynamic truncation to extract 6 digits
    offset = hmac_hash[-1] & 0x0F
    truncated_hash = hmac_hash[offset:offset + 4]
    code = int.from_bytes(truncated_hash, 'big') & 0x7FFFFFFF
    return str(code)[-6:]  # Return the last 6 digits

if __name__ == "__main__":
    # Example: Using the SECRET_KEY to generate a one-time password
    shared_secret = base64.b32encode(bytes.fromhex(SECRET_KEY)).decode('utf-8')
    otp = generate_otp(shared_secret)
    
    print("Your One-Time Password (OTP):", otp)

    # Debug: Logging the shared secret for verification (not recommended in production!)
    print("DEBUG: Shared secret key (Base32):", shared_secret)
