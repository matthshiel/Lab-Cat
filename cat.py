'''
This program prints stdin to the screen.
'''
import sys

CHUNK_SIZE = 65536

def cat(file):
    out = sys.stdout.buffer
    while True:
        chunk = file.read(CHUNK_SIZE)
        if not chunk:
            break
        out.write(chunk)
    out.flush()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
