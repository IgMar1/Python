#Generador de contraseñas en python
import secrets

def generate_password():
  # Generate a random password of 12 characters
  password = secrets.token_urlsafe(12)
  return password

# Generate and print the password
password = generate_password()
print("Your password is: ",password)
