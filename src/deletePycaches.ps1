# Get the current directory
$currentDirectory = Get-Location

# Function to recursively search for and delete "__pycache__" folders
function DeletePycache {
    param (
        [Parameter(Mandatory = $true)]
        [string]$path
    )

    # Get all "__pycache__" folders in the given path
    $pycacheFolders = Get-ChildItem -Path $path -Filter "__pycache__" -Directory -Recurse -ErrorAction SilentlyContinue

    # Loop through each "__pycache__" folder and delete it
    foreach ($folder in $pycacheFolders) {
        Write-Host "Deleting folder: $($folder.FullName)"
        Remove-Item -Path $folder.FullName -Force -Recurse
    }
}

# Call the function to delete "__pycache__" folders in the current directory
DeletePycache -path $currentDirectory
