class Seq:
    # A class for representing sequences
    # We now make use of the __init__ function to add attributes
    def __init__(self, strbases):
        valid = True
        valid_bases = ["A","C","T","G"]
        for base in strbases:
            if valid and base not in valid_bases:
                valid = False
        if valid:
            self.bases = strbases
            print("New sequence created!")
        else:
            self.bases = "ERROR"
            print("ERROR!!")

    def __str__(self):
        return self.bases


s1 = Seq("ACCGGGTTTT") #Creating an object of the class Seq
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")