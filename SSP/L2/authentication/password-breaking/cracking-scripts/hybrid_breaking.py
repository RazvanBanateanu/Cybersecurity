#!/usr/bin/python3

import sys
from hashlib import sha256


hashes = []


def hybrid_module():
    global hashes
    current = list(hashes)
    for s in [line.strip() for line in open("../dict/words")]:
        # TODO
        s = s.replace('a', '@').replace('e', '3').replace('i', '!').replace('o', '0').replace('s', '$')
        hash_to_match = sha256(s.encode('utf-8')).hexdigest()
        if hash_to_match in current:
        	print("{} -> {}".format(hash_to_match, s), file=sys.stderr)
        	hashes.remove(hash_to_match)


def main():
    global hashes
    # Read hashes from standard input.
    hashes = [line.strip() for line in sys.stdin]
    hybrid_module()
    print('\n'.join(h for h in hashes))


if __name__ == "__main__":
    sys.exit(main())
