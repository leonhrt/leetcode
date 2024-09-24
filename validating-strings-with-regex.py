# Validation String with RegEx

# Given a list of string made up of characters 'a' and 'b', create a regular expression that will match string that begin and end with the same letter.

# Example:
# 'a', 'aa', and 'bababbb' match.
# 'ab' and 'baba' do not match.

regularExpression = '^(a.*a|b.*b|a|b)$'