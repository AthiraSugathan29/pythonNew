class A:
    var1 = None #Public data member
    _var2 = None #Protected data member
    __var3 = None # Private data member

    def __init__(self,var1,var2,var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    # Public Member Function
    def displayPublicMembers(self):
        # Accessing Public Data Member
        print("Public Data Member :",self.var1)

    # Protected Member Function
    def _displayProtectedMembers(self):
        # Accessing Protected Data Member
        print("Protected Data Member :",self._var2)

    # Private Member Function
    def __displayPrivateMembers(self):
        # Accessing Private Data Member
        print("Private Data Member :",self.__var3)

    # Public Member Function To Access Private Member Function
    def accessPrivateMemberFunction(self):
        self.__displayPrivateMembers()

class B(A):
    def __init__(self,var1,var2,var3):
        A.__init__(self,var1,var2,var3)

    # Public Member Function To Access Protected Member Function
    def accessProtectedMemberFunction(self):
        # Accessing Protected Member Functions of super class
        self._displayProtectedMembers()

obj = B('Public_Red','Protected_Red','Private_Red') # Passing parameters to constructor
obj.displayPublicMembers()
obj.accessProtectedMemberFunction()
obj.accessPrivateMemberFunction()

print("Object Accessing Public Data Member : ",obj.var1) # Accessing Public Data Member using object
print("Object Accessing Protected Data Member : ",obj._var2) # Accessing Protected Data Member using object

# Object cannot access private data member. It will generate Attribute Error
print("Object Accessing Private Data Member : ",obj._A__var3) # Accessing using Name Mangled variables

