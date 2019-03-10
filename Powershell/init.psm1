Function RunChessPython {
    py __main__.py
}

Function BuildChessPython {
    $projectLocation = $global:externalDrive + '\' + $global:currentProject + '\'
    
    Write-Host $projectLocation

    $sourceRootMusic = $global:projectLocation + 'app\music'
    $sourceRootComponents = $global:projectLocation + 'app\components'
    $destinationRootMusic = $global:projectLocation + 'build\exe.win-amd64-3.6\app\music'
    $destinationRootComponents = $global:projectLocation + 'build\exe.win-amd64-3.6\app\components'


    Write-Host $sourceRootMusic
    Write-Host $destinationRootMusic

    Copy-Item -Path $sourceRootMusic -Recurse -Destination $destinationRootMusic -Container
    Copy-Item -Path $sourceRootComponents -Recurse -Destination $destinationRootComponents -Container
    
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