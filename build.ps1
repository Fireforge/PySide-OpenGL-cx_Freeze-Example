$buildlog = "build.log"
Write-Host "Building..."
C:\pyzo2013c\python.exe .\setup.py build > $buildlog

# Creating Shortcut
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("hellogl.lnk")
$Shortcut.TargetPath = "C:\Users\DAS\PythonProjects\hellogl\build\exe.win-amd64-3.3\hellogl.exe"
$Shortcut.Save()

Write-Host "Build complete!"
Write-Host "Press any key to continue ..."
$x = $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")