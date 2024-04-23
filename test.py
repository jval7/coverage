from unittest.mock import patch, MagicMock

import pytest

from todo import TodoItem, TodoListController, ConsoleView, CommandStrategy, AddCommandStrategy, \
    CompleteCommandStrategy, ListCommandStrategy


def test_should_mark_as_completed_when_calling_mark_as_completed_method():
    # configuration
    task1 = TodoItem(title="Tarea 1", description="Descripcion")
    # act
    task1.mark_as_completed()
    # assert
    assert task1.completed == True


def test_should_add_task_when_calling_add_item_method():
    # configuration
    list_test = []
    controller = TodoListController(todo_list=list_test)
    # act
    controller.add_item(title="task1", description="description")
    # assert
    assert len(list_test) > 0
    
def test_should_list_items_when_calling_list_items_method():
    # configuration
    list_test = []
    controller = TodoListController(todo_list=list_test)
    controller.add_item(title="task1", description="description")
    # act
    controller.list_items()
    # assert
    assert len(list_test) > 0

def test_should_mark_item_as_completed_when_calling_complete_item_method():
    # Bloque de configuración (Configuration)
    controller = TodoListController([])  # Crea una instancia de TodoListController con una lista vacía
    controller.add_item("Título", "Descripción")  # Añade un elemento a la lista

    # Bloque de acción (Act)
    controller.complete_item(0)  # Intenta marcar el elemento como completado


    # Bloque de aserción (Assert)
    assert controller.todo_list[0].completed == True  # Verifica que el elemento se haya marcado como completado

    with pytest.raises(IndexError):  # Verifica que se lanza una excepción IndexError
        controller.complete_item(1)

def test_should_return_command_when_calling_get_command_method():
    # Configuración
    view = ConsoleView()

    with patch('builtins.input', return_value='add'):
        # Actuar
        command = view.get_command()

        # Afirmar
        assert command == 'add', "El comando debería ser 'add'"

def test_should_list_items_when_calling_list_items_method2():
    # Configuración
    todo_list = []
    controller = TodoListController(todo_list)
    controller.add_item(title="task1", description="description1")

    # Actuar
    controller.list_items()

    # Afirmar
    assert len(todo_list) == 1, "La lista de tareas debería tener 1 ítem"
    assert todo_list[0].title == "task1", "El título de la primera tarea debería ser 'task1'"
    assert todo_list[0].description == "description1", "La descripción de la primera tarea debería ser 'description1'"
def test_should_print_items_when_calling_show_list_method():
    # Configuración
    view = ConsoleView()
    items = ['task1', 'task2', 'task3']

    with patch('builtins.print') as mock_print:
        # Actuar
        view.show_list(items)

        # Afirmar
        mock_print.assert_any_call("Lista de tareas:")
        mock_print.assert_any_call("1. task1")
        mock_print.assert_any_call("2. task2")
        mock_print.assert_any_call("3. task3")

def test_should_print_message_when_calling_show_message_method():
    # Configuración
    view = ConsoleView()
    message = "¡Hola, Mundo!"

    with patch('builtins.print') as mock_print:
        # Actuar
        view.show_message(message)

        # Afirmar
        mock_print.assert_called_once_with(message)

def test_should_initialize_controller_when_creating_commandstrategy_instance():
    # Configuración
    todo_list = []
    controller = TodoListController(todo_list)

    # Actuar
    strategy = CommandStrategy(controller)

    # Afirmar
    assert strategy.controller == controller, "El controlador de la estrategia debería ser el controlador proporcionado"

def test_should_do_nothing_when_calling_execute_method():
    # Configuración
    controller = None  # Como el método execute no hace nada, podemos usar None para el controlador
    strategy = CommandStrategy(controller)

    # Actuar y afirmar
    try:
        strategy.execute("command")
    except Exception as e:
        pytest.fail(f"El método execute produjo un error: {e}")
def test_should_add_item_when_calling_execute_method():
    # Configuración
    todo_list = []
    controller = TodoListController(todo_list)
    strategy = AddCommandStrategy(controller)
    command = "task1,description1"

    # Mock the add_item method of the controller
    controller.add_item = MagicMock()

    # Actuar
    strategy.execute(command)

    # Afirmar
    controller.add_item.assert_called_once_with("task1", "description1")
def test_should_complete_item_when_calling_execute_method():
    # Configuración
    todo_list = []
    controller = TodoListController(todo_list)
    strategy = CompleteCommandStrategy(controller)
    command = "1"

    # Mock the complete_item method of the controller
    controller.complete_item = MagicMock()

    # Actuar
    strategy.execute(command)

    # Afirmar
    controller.complete_item.assert_called_once_with(0)
def test_should_list_items_when_calling_execute_method():
    # Configuración
    todo_list = []
    controller = TodoListController(todo_list)
    strategy = ListCommandStrategy(controller)

    # Mock the list_items method of the controller
    controller.list_items = MagicMock()

    # Actuar
    strategy.execute()

    # Afirmar
    controller.list_items.assert_called_once()