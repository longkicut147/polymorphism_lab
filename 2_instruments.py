class Guitar:
    def play(self):
        print("playing the guitar")
class Piano:
    def play(self):
        print("playing the piano")

def play_instrument(ins:isinstance):
    return ins.play()

guitar = Guitar()
play_instrument(guitar)

piano = Piano()
play_instrument(piano)