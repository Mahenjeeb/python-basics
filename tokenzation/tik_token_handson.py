import tiktoken

token = tiktoken.encoding_for_model('gpt-4o')
enc = token.encode("Hey There! I am Mahenjeeb")

print("Encoded Token", enc)
# Encoded Token [25216, 3274, 0, 357, 939, 18429, 138187, 1113]

dec = token.decode(enc)
print("Decoded Token", dec)
# Decoded Token Hey There! I am Mahenjeeb