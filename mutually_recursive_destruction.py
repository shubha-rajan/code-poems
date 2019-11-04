# codependency // mutually recursive destruction - 
class You:
    def __init__(self):
        self.countdown = 10
        self.bound = None

    def attach_to(self,another):
        print("We are bound to each other.")
        self.bound = another
        if not another.bound:
            another.attach_to(self)
        print("A bond that will smother")
    
    def drain(self, another):
        if self.countdown < 0: return
        another.countdown -= 1
        if self.countdown == 0: 
            print("until you have nothing left to take")
        elif self.countdown > 5:
            if self.countdown % 2 == 0:
                print("I give")
            else:
                print("and you take")
        elif self.countdown < 5:
            print("and you take")
        another.drain(self)

class I:
    def __init__(self):
        self.countdown = 10
        self.bound = None

    def attach_to(self,another):
        print("You and I")
        self.bound = another
        if not another.bound:
            another.attach_to(self)
        print("We engulf one another.")

    def drain(self, another):
        if self.countdown < 0: return
        another.countdown -= 1
        if self.countdown==0: 
            print("until you have nothing left to give")
        elif self.countdown > 5:
            if self.countdown % 2 == 0:
                print("and I take")
            else:
                print("you give")
        elif self.countdown < 5:
            print("and I take")
        another.drain(self)

you = You()
me = i = I()

i.attach_to(you)
assert(me == you.bound)
assert(you == me.bound)
you.drain(me)