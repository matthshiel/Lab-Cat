import sys

def cat(file):
    while chunk := file.read(64 * 1024):
        sys.stdout.buffer.write(chunk)  # or file → sys.stdout.buffer

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
