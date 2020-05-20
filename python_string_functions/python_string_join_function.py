"""
join function takes a list as an argument and is written as
'ddelimiter'.join()
"""

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join( reapers_line_one_words)
print(reapers_line_one)
print('/./././././././././././././././././././././././././././././././././././././././././././.')


winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!',
                      'A liquid moon', 'moves gently among', 'the long branches.',
                      'Thus having prepared their buds', 'against a sure winter', 'the wise trees',
                      'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)

print('############################################################################')
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for words in love_maybe_lines:
  love_maybe_lines_stripped.append(words.strip())

print(love_maybe_lines_stripped)




