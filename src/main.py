import random
from constants import ALL_LETTERS


class Hushh:
    def __init__(self, key: str, total_characters: int = 120) -> None:
        """
        password (str): The password to be used for encryption and decryption.
        """
        self.key = key
        self.total_characters = total_characters
        self.hush_ls = self._shuffle_letters()

    def _shuffle_letters(self):
        all_letters_copy = ALL_LETTERS[:]
        random.Random(self.key).shuffle(all_letters_copy)

        return all_letters_copy

    def cipher(self, string: str):
        """
        Generates a unique string based on the provided string and password.

        The password can then be used to decrypt the string.
        """

        returned_pass = ""

        for letter in string:
            if letter in ALL_LETTERS:
                returned_pass += self.hush_ls[ALL_LETTERS.index(letter)]

        return self._extend_password(returned_pass)

    def decrypt(self, hushh: str):

        returned = ""
        storage_letter = random.Random(self.key).randint(0, self.total_characters // 2)
        for letter in hushh:
            if letter in ALL_LETTERS:
                returned += ALL_LETTERS[self.hush_ls.index(letter)]

        try:
            total = int(hushh[storage_letter])
            index = int(hushh[storage_letter + 1 : storage_letter + total + 1])
        except ValueError:
            # print("[red]Error: Failed to decode password. Encrypted string may be too long or too long[/red]")
            # raise ValueError
            return

        return returned[len(hushh) - index :]

    def _extend_password(self, hush: str):
        """
        Extends the hush to the length of self.total_characters such that it can still be decrypted
        """
        extra = self.total_characters - len(hush)

        if not extra > 0:
            return hush

        # A random letter in extra will store the length of the hush
        storage_letter = random.Random(self.key).randint(0, self.total_characters // 2)

        # Storage string has the length of storage (so it can be decoded) and the length of the hush
        storage_string = str(len(str(storage_letter))) + str(len(hush))

        returned = ""
        total = len(storage_string) + len(hush)

        for i in range(extra):

            if i == storage_letter:
                returned += storage_string
            else:
                if total >= self.total_characters:
                    break

                returned += random.choice(ALL_LETTERS)
                total += 1

        returned += hush

        return returned


if __name__ == "__main__":
    from rich import print

    hushh = Hushh("password", total_characters=30)

    sentence = input("Enter a sentence: ")

    encrypted = hushh.cipher(sentence)

    print(f"[yellow]Encrypted[/yellow]: `[blue bold]{encrypted}[/blue bold]`")

    decryped = hushh.decrypt(encrypted)
    print("[yellow]Decrypted[/yellow]: ", decryped)

    success = sentence == decryped
    print("[yellow]Success[/yellow]: " + str(success))

    if not success:
        print(
            f"[yellow]Debug[/yellow]: The length of the encrypted string is {len(encrypted)}. Length of original string is {len(sentence)}"
        )
