class Grandad:
    def gun(self):
        print("He has a revolver")
class Dad:
    def ak(self):
        print("He has a AK47")
class grandchild(Grandad,Dad):
    pass
gc=grandchild()
gc.ak()
gc.gun()