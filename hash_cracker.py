import hashlib
import time

def hash_cracker(hash_to_crack, hash_type, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding="utf-8", errors='ignore') as file:
            for words in file:
                word = words.strip()
                if hash_type == 'md5':
                    hashed_word = hashlib.md5(word.encode())
                elif hash_type == 'sha1':
                    hashed_word = hashlib.sha1(word.encode())
                else:
                    print("[-]Unsupported hash type")
                    return
                if hashed_word.hexdigest() == hash_to_crack :
                    print(f"[+] Hash was cracked: {word}")
                    return
            print("[-] Hash not found in the wordlist.")
    except FileNotFoundError as e:
        print(f"[-] {wordlist_path} was not found!")


if __name__ == "__main__" :
    print("===Welcome to Hash Cracker===")
    hash_to_crack = input("Enter the hash: ").strip()
    hash_type = input("Enter the hash type between to this 'md5' or 'sha1' : ").strip()
    wordlist_path = input("Enter the path of wordlist: ").strip()
    
    print("Hash cracking Starting......")
    time.sleep(1)


    hash_cracker(hash_to_crack, hash_type, wordlist_path)