class SecretDiary:
    def __init__(self, diary):
        self.diary = diary
        self.locked = True

    def read(self):
        if self.locked == True:
            raise Exception('Go away!')
        else:
            return self.diary.contents

        

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False