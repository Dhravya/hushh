from main import Hushh

sentence = 'hi I am dhravya'
success = 0

hush = Hushh(key="yousussybaka")
for i in range(0,100 * 1000):
    # Determine the success rate
    print(f"Completing...{i}")
    encrypted = hush.cipher(sentence)
    decryped = hush.decrypt(encrypted)
    if sentence == decryped:
        success += 1
    print("\033[F\033[K", end="")
    
# TODO: for some reason, very short strings (less than 10 chars) have a success rate of about 1%
print(f"{success / 1000}%")

