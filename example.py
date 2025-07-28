from aion import text, files, parser, ai_utils

# Text processing
text.count_words("Hello world!")  # 2
emails = text.extract_emails("Contact us at info@linkai.com")

# AI-powered features
language = ai_utils.detect_language("Bonjour le monde")  # 'french'
sensitive_data = ai_utils.scan_sensitive_data("My password is secret123")  # ['secret123']
is_question = ai_utils.is_question("What is your name?")  # True

# File operations
content = files.read_file("data.txt")
files.write_file("output.txt", "Hello World!")

# Parsing
numbers = parser.extract_numbers("Price: $99.99 and $149.99")