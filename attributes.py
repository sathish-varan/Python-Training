class whatsapp:
    def __init__(self,name,status,password):
        self.name=name #public
        self._status=status #protected
        self.__password=password #private
    def view_profile(self):
        print(user.name)
        print(user._status)
        print(user.__password)
user =whatsapp('Nobita','Friends','Doremon123')
user.view_profile()
