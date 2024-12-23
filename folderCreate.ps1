$year = 2024

# Path to the .gitignore file in the parent directory of the $year folder
$yearFullPath = (Get-Item -Path $year).FullName
$parentDir = Split-Path -Path $yearFullPath -Parent
$gitignorePath = Join-Path -Path $parentDir -ChildPath ".gitignore"

# Read existing entries from .gitignore
$gitignoreEntries = Get-Content -Path $gitignorePath -ErrorAction SilentlyContinue

Write-Host "Creating directories and files for Advent of Code $year"
Write-Host "================="

for ($day = 1; $day -le 25; $day++) {
    $dayDir = "$year\Day$day"
    if (-Not (Test-Path -Path $dayDir)) {
        New-Item -ItemType Directory -Path "$dayDir" | Out-Null
        Write-Host "Created directory $dayDir... ✓" -ForegroundColor Green
    } else {
        Write-Host "Directory $dayDir already exists, skipping... ✗" -ForegroundColor Red
    }

    $pyFile = "$dayDir\day$day.py"
    if (-Not (Test-Path -Path $pyFile)) {    
        $pyfileContent = @"
# Solution for Advent of Code $year, Day $day
# https://adventofcode.com/$year/day/$day
from time import perf_counter

if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip()

    print("\033[1mPart1:\033[22m", "p1")
    print("\033[1mPart2:\033[22m", "p2")

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")

"@
        $pyfileContent | Set-Content -Path $pyFile
        Write-Host "Created file $pyFile... ✓" -ForegroundColor Green
    } else {
        Write-Host "File $pyFile already exists, skipping... ✗" -ForegroundColor Red
    }

    $testFile = "$dayDir\test.txt"
    if (-Not (Test-Path -Path $testFile)) {
        New-Item -ItemType File -Path $testFile | Out-Null
        Write-Host "Created file $testFile... ✓" -ForegroundColor Green
    } else {
        Write-Host "File $testFile already exists, skipping... ✗" -ForegroundColor Red
    }

    $readmeFile = "$dayDir\README.md"
    if (-Not (Test-Path -Path $readmeFile)) {
        $readmeContent = @"
# Advent of Code $year, Day $day
"@
    $readmeContent | Set-Content -Path "$dayDir\README.md"
    Write-Host "Created file $readmeFile... ✓" -ForegroundColor Green
    } else {
        Write-Host "File $readmeFile already exists, skipping... ✗" -ForegroundColor Red
    }

    $gitignoreEntry = "$year/day$day"
    if ($gitignoreEntries -notcontains $gitignoreEntry) {
        Add-Content -Path $gitignorePath -Value $gitignoreEntry
        Write-Host "Added $gitignoreEntry to .gitignore... ✓" -ForegroundColor Green
    } else {
        Write-Host "$gitignoreEntry already exists in .gitignore, skipping... ✗" -ForegroundColor Red
    }
}   

Write-Host "================="
Write-Host "Done! Love you. Bye! <3" -ForegroundColor Magenta