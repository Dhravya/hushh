# Hushh 🤫

AES-like encryption and decryption tool, without any dependencies.

This is a pretty simple algorithm that allows you to encrypt and decrypt strings based on a key.

### Usage

```py
hush = Hushh(key="yousussybaka")
encrypted = hush.cipher("This is a secret message")
# ^X'Qm}02zUEH"j!{5J]RnycH_':!'w}X2n3oB<DM224fj}%MCt,;X?JNQW[ffJCT[('XU"f=(E}NcOE]HrFwi?Gn{-AxuOzj!wW|dW|dB d|]s*]-dg]||Br]

decryped = hush.decipher(encrypted)
# This is a secret message
```

### How it works

- The key is used to generate a "Hush list" which is basically just a randomly shuffled list of characters, with the password as the seed.
- An encryption is generated. obviously, the encrypted string is the same length as the original string.
- The string is extended. This is done by storing the length of the "hush" somewhere in the string in the format of `{length}{number}` (where length is the length of the number and number is length of the hush)

Here's an example storing "wtf" with the password as "password" and total characters as 30:

![hush](https://us-east-1.tixte.net/uploads/img.dhravya.dev/hushh.png)

### Use cases

I made this mainly to serve as a tool for myself so I can generate and validate API keys to use for my own projects. API keys can have a username encrypted in them which I can use to identify the user. This also eliminates the need for me to store the API keys and passwords in plaintext, only store usernames instead. 
