from todo import TodoItem, TodoListController


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


