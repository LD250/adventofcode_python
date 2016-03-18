import hashlib

def main():
    input = 'ckczppom'
    def mine(starts_with):
        out = False
        i = 0
        while not out:
            i += 1
            h = hashlib.md5(input + str(i)).hexdigest()
            if h.startswith(starts_with):
                out = True
        return i

    print mine('00000')
    print mine('000000')

if __name__ == "__main__":
    main()
