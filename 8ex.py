# sets the formatter variable, to use the raw format
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
# look at the output below, which shows the "but" string as single quotes. that's because it has the word 'didn't' which uses a single quote, which python changes when generating the representation
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# outputs with the following
# 1 2 3 4
# 'one' 'two' 'three' 'four'
# True False False True
# '%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
# 'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'