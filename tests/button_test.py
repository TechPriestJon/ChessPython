import pytest
import pyglet
from ChessPython.components.button import Button

def test_return_true():
    button_name = 'XYZ'
    button = Button(button_name,0,0)

    assert button.label().text == button_name

def test_return_false():
    button_name = 'XYZS'
    button = Button(button_name,0,0)
    assert button.label().text == button_name

#def f():
#    raise SystemExit(1)

#def test_mytest():
#    with pytest.raises(SystemExit):
#        f()