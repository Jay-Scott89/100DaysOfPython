# Function with outputs
def format_name(f_name, l_name):
    """Take a first and last name and format it 
    to return the title case version of the name."""
    titled_f_name = f_name.title()
    titled_l_name = l_name.title()

    return f"{titled_f_name} {titled_l_name}"

formated_string = format_name("jamie", "SCOTT")
print(formated_string)

