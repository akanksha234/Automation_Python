"""
Given a string containing author names,
print out a list of last names of each author.
"""

authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, " \
          "An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya," \
          "Langston Hughes, Adrienne Rich, Nikki Giovanni"
author_names = authors.split(',')

author_last_names = [name.split()[-1] for name in author_names]
print( author_last_names)