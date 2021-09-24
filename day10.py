# task 1

class Song:
    def __init__(self, title='', author='', lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(
            f"Initialized class instance with {self.title=} {self.author=} and {self.lyrics=} \n")
        print(f"New song made - {self.title} - {self.author} \n")

    def sing(self, max_lines=-1):
        if self.title and self.author:
            print(self.title, "-", self.author)
            print('♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪')
        if self.lyrics and max_lines == -1:
            for i in self.lyrics:
                print(i)
            print('')
        else:
            if len(self.lyrics) >= max_lines:
                for num in range(max_lines):
                    print(self.lyrics[num])
            else:
                print('Sorry, there are not enough lines to print')
            print('')
        return self

    def yell(self, max_lines=-1):
        if self.title and self.author:

            print(self.title.upper(), "-", self.author.upper())
            print('♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪')
        if self.lyrics and max_lines == -1:
            for i in self.lyrics:
                print(i.upper())
            print('')
        else:
            if len(self.lyrics) >= max_lines:
                for num in range(max_lines):
                    print(self.lyrics[num].upper())
            else:
                print('Sorry, there are not enough lines to print')
            print('')
        return self


ziemelmeita = Song("Ziemeļmeita", "Jumprava", [
    "Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])

tuvutuvu = Song("Tuvu Tuvu", "Lādezers", [
                "Tuvu tuvu", "tuvāk vēl", "ko vēl var vēlēties"])


ziemelmeita.sing(1)
ziemelmeita.yell(1)
tuvutuvu.sing().yell()


# Task 2

class Rap(Song):
    def __init__(self, title, author, lyrics):
        super().__init__(title=title, author=author, lyrics=lyrics)

    def break_it(self, max_lines=-1, drop="YEAH"):
        print(self.title, "-", self.author)
        print("♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪")
        txt = [' '.join]


zrap = Rap("Tuvu Tuvu", "Lādezers", [
    "Tuvu tuvu", "tuvāk vēl", "ko vēl var vēlēties"])
zrap.break_it()
