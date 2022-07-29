from main import Hushh

sentence = 'hi I am dhravya'
success = 0

hush = Hushh(password="yousussybaka")
for i in range(0,100 * 1000):
    print(f"Completing...{i}")
    key = hush.generate_password(sentence)
    decryped = hush.decode_password(key)
    if sentence == decryped:
        success += 1
    print("\033[F\033[K", end="")
    
print(f"{success / 1000}%")

