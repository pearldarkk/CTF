param(
    [Parameter(Mandatory = $true)]
    [string]$FileInput,
    [Parameter(Mandatory = $true)]
    [string]$FileOutput
)
Set-Alias -Name newObj -Value New-Object; Set-Alias -Name getContent -Value Get-Content; Set-Alias -Name testPath -Value Test-Path
$inp = $FileInput
$out = $FileOutput
$wClient = newObj System.Net.WebClient
$link = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3LzFtTkFFOXlw"))
$data = $wClient.DownloadData($link)
if (testPath $inp) {
    $inpData = getContent -Path $inp -Encoding Byte
    $len = $inpData.Length
    $bytes = [System.Byte[]]::new($len)
    $bytes[0] = 0x89
    for ($i = 0; $i -lt $len; $i++) {
        $bytes[($($i + 1) % $len)] = $($inpData[$i] -bxor $data[$($bytes[$i] % 8)])
    }
    Set-Content -Path $out -Value $bytes -Encoding Byte
}
else {
    Write-Host "Cannot find input file"
}
#powershell
#.\warmup.ps1 -FileInput flag.png.enc -FileOutput flag.png
# flag BKSEC{Powershell-is-easy-612256483485126}