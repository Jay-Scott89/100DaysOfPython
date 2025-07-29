
# A Doc String is a multi line comment. When placed directly under the function it adds comments to that function to help when its called. 
def names(f_name, l_name):
    """Take a first and last name and format it to 
    return a tile case version of the name."""
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"

name = names("jamie", "SCOTT")
print(f"Hello {name}, how are you?")