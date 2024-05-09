from pilha_encadeada import Stack

class TextEditor:
    def __init__(self):
        self.undo_stack = Stack()
        self.redo_stack = Stack()
        self.text = ""

    def insert_text(self, text):
        self.text += text
        self.undo_stack.push(("insert", text))

    def delete_text(self, length):
        deleted_text = self.text[-length:]
        self.text = self.text[:-length]
        self.undo_stack.push(("delete", deleted_text))

    def undo(self):
        if not self.undo_stack.is_empty():
            operation = self.undo_stack.pop()
            if operation[0] == "insert":
                self.text = self.text[:-len(operation[1])]
            elif operation[0] == "delete":
                self.text += operation[1]
            self.redo_stack.push(operation)

    def redo(self):
        if not self.redo_stack.is_empty():
            operation = self.redo_stack.pop()
            if operation[0] == "insert":
                self.text += operation[1]
            elif operation[0] == "delete":
                self.text = self.text[:-len(operation[1])]
            self.undo_stack.push(operation)

    def get_text(self):
        return self.text


# Exemplo de uso:
editor = TextEditor()
print("Texto atual:", editor.get_text())

editor.insert_text("Olá, ")
editor.insert_text("mundo!")
print("Texto atual:", editor.get_text())

editor.delete_text(6)
print("Texto atual:", editor.get_text())

editor.undo()
print("Texto atual após desfazer:", editor.get_text())

editor.redo()
print("Texto atual após refazer:", editor.get_text())
