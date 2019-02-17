Function RunChessPython {
    py __main__.py
}

Function BuildChessPython {
    py setup.py build
}

Function TestChessPython {

}

Function OpenChessPython {
    code chess-python.code-workspace;
}

Write-Host -ForegroundColor Green "Loaded Init Successfully"