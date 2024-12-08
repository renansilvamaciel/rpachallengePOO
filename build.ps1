$exclude = @("venv", "rpachallengePOO.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "rpachallengePOO.zip" -Force