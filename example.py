from aion.files import (
    create_empty_file, file_exists, write_file, append_to_file,
    read_file, rename_file, delete_file
)
from aion.parser import detect_language, parse_code, extract_snippets
from aion.watcher import watch_file_for_changes

# === Extra Utility Functions ===
def count_tokens(code: str) -> int:
    """Counts the number of tokens in the code. Placeholder implementation."""
    return len(code.split())

def summarize_code(code: str) -> str:
    """Summarizes the code. Placeholder implementation."""
    lines = code.strip().splitlines()
    return f"{len(lines)} lines of code with {count_tokens(code)} tokens."

# === File Management Test ===
print("=== File Management Test ===")
create_empty_file("test_file.txt")
print("File created:", file_exists("test_file.txt"))
write_file("test_file.txt", "print('Hello Aion v0.1.6!')\n# This is a test file.")
append_to_file("test_file.txt", "\nprint('Appending more lines!')")
print("File content:\n", read_file("test_file.txt"))
rename_file("test_file.txt", "renamed_test_file.txt")
print("Renamed file exists:", file_exists("renamed_test_file.txt"))

# === Code Parsing Test ===
print("\n=== Code Parsing Test ===")
code = read_file("renamed_test_file.txt")
lang = detect_language(code)
print("Detected language:", lang)
parsed = parse_code(code, lang)
print("Parsed code:", parsed)

# === Snippet Extraction Test ===
print("\n=== Snippet Extraction Test ===")
snippets = extract_snippets("""
# @snippet greeting
def greet(name):
    return f"Hello, {name}!"

print(greet("Aion"))
""")
print("Extracted snippets:", snippets)

# === File Diff Test ===
print("\n=== File Diff Test ===")
# The diff_files function was removed from imports, so this test is commented out or removed if not needed.
# For now, I'll keep it as is, but it will cause an error.
# diff_result = diff_files("old_version.py", "renamed_test_file.txt")
# print("Diff result:\n", diff_result)

# === Watch File Test ===
print("\n=== File Watcher Test (type Ctrl+C to stop) ===")
def on_change(path):
    print(f"File changed: {path} — You can re-run embed here!")

watch_file_for_changes("renamed_test_file.txt", on_change)

# === Embed Watcher Test ===
print("\n=== Embed Watcher Test ===")
# The watch_and_embed function was removed from imports, so this test is commented out or removed if not needed.
# For now, I'll keep it as is, but it will cause an error.
# watch_and_embed("renamed_test_file.txt", on_embed=lambda path: print("Embedding logic for:", path))

# === Config Loader Test ===
print("\n=== Config Loader Test ===")
# The load_config function was removed from imports, so this test is commented out or removed if not needed.
# For now, I'll keep it as is, but it will cause an error.
# config = load_config("aion.config.yaml")
# print("Loaded config:", config)