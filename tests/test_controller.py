from mtcli.controller import Controller

controller = Controller("range")


def test_saida_da_view():
    assert controller.view == ""


def test_saida_string_do_controller():
    assert str(controller) == ""
