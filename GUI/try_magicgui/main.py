from magicgui import magicgui


@magicgui
def add(my_number: int, some_word: str = 'hello', maybe=True):
    pass


add.show()
