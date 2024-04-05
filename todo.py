# Modelo (Model)
class TodoItem:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True


# Controlador (Controller)
class TodoListController:
    def __init__(self, todo_list):
        self.todo_list = todo_list

    def add_item(self, title, description):
        item = TodoItem(title, description)
        self.todo_list.append(item)

    def complete_item(self, index):
        try:
            self.todo_list[index].mark_as_completed()
        except IndexError:
            print("Índice de tarea no válido")

    def list_items(self):
        for i, item in enumerate(self.todo_list):
            status = "Completada" if item.completed else "Pendiente"
            print(f"{i + 1}. [{status}] {item.title}: {item.description}")


# Vista (View) - Patrón Strategy
class ConsoleView:
    def get_command(self):
        return input("Ingrese un comando: ")

    def show_list(self, items):
        print("Lista de tareas:")
        for i, item in enumerate(items):
            print(f"{i + 1}. {item}")

    def show_message(self, message):
        print(message)


# Estrategia para manejar comandos de usuario
class CommandStrategy:
    def __init__(self, controller):
        self.controller = controller

    def execute(self, command):
        pass


class AddCommandStrategy(CommandStrategy):
    def execute(self, command):
        title, description = command.split(",", 1)
        self.controller.add_item(title, description)


class CompleteCommandStrategy(CommandStrategy):
    def execute(self, command):
        index = int(command) - 1
        self.controller.complete_item(index)


class ListCommandStrategy(CommandStrategy):
    def execute(self, command=None):
        self.controller.list_items()


# Aplicación
class TodoApp:
    def __init__(self):
        self.todo_list = []
        self.controller = TodoListController(self.todo_list)
        self.view = ConsoleView()
        self.command_strategies = {
            "add": AddCommandStrategy(self.controller),
            "complete": CompleteCommandStrategy(self.controller),
            "list": ListCommandStrategy(self.controller)
        }

    def run(self):
        print("Bienvenido a la aplicación de tareas")
        print("Comandos disponibles:")
        print("add <título>, <descripción>")
        print("complete <índice>")
        print("list")
        print("Escribe 'exit' para salir")
        while True:
            command = self.view.get_command().strip()
            if command == "exit":
                break
            elif command.split(" ", 1)[0] in self.command_strategies:
                action, *args = command.split(" ", 1)
                strategy = self.command_strategies[action]
                strategy.execute(*args)
            else:
                self.view.show_message("Comando no reconocido")


# Ejecutar la aplicación
if __name__ == "__main__":
    app = TodoApp()
    app.run()
