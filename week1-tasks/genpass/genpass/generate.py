import click
import string
import random

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

@click.command()
@click.argument('length', type=int)
@click.option('--include-uppercase', '-uc', help = "Include uppercase letters", is_flag = True, default = False)
@click.option('--include-lowercase', '-lc', help = "Include lowercase letters", is_flag = True, default = False)
@click.option('--include-letters', '-alpha', help = "Include letters (both uppercase and lowecase)", is_flag = True, default = False)
@click.option('--include-digits', '-d', help = "Include digits", is_flag = True, default = False)
@click.option('--include_symbols', '-sy', help = "Include symbols", is_flag = True, default = False)
def generate_password(length, include_uppercase, include_lowercase, include_letters, include_digits, include_symbols):
    character_options = ""
    
    if include_uppercase:
        character_options += uppercase_letters
        
    if include_lowercase:
        character_options += lowercase_letters
        
    if include_letters:
        if not include_lowercase:
            character_options += uppercase_letters
        if not include_uppercase:
            character_options += lowercase_letters
        
        
    if include_digits:
        character_options += digits
        
    if include_symbols:
        character_options += special_characters
        
        
    if len(character_options) == 0:
        click.echo("Please select what to include in password. Run --help to view the options")
        return
    
    password = ""
    for i in range(length):
        password += random.choice(character_options)
    
    click.echo(password)
    

if __name__ == '__main__':
    generate_password()
        

        
    