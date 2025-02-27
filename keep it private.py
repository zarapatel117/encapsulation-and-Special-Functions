class myclass:
    __privatevar=227;
    def __privmeth(self):
        print("i'm inside my class")
    def hello(self):
        print("private variable values",myclass.__privatvar)
foo=myclass()
foo.hello()
foo.__privatevar

