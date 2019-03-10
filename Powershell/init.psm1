Function RunChessPython {
    py __main__.py
}

Function BuildChessPython {
    py setup.py build
    chess-python.exe
}

Function TestChessPython {

}

Function OpenChessPython {
    code chess-python.code-workspace;
}

Function InitChessPython{
    py -m pip install pyglet
    py -m pip install -U pytest
    py -m pip install cx_Freeze --upgrade
}

Write-Host -ForegroundColor Green "Loaded Init Successfully"