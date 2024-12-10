$year = 2024

# Path to the .gitignore file in the parent directory of the $year folder
$yearFullPath = (Get-Item -Path $year).FullName
$parentDir = Split-Path -Path $yearFullPath -Parent
$gitignorePath = Join-Path -Path $parentDir -ChildPath ".gitignore"

# Read existing entries from .gitignore
$gitignoreEntries = Get-Content -Path $gitignorePath -ErrorAction SilentlyContinue

Write-Host "Creating directories and files for Advent of Code $year"
Write-Host "================="

for ($i = 1; $i -le 25; $i++) {
    $dayDir = "$year\Day$i"
    if (-Not (Test-Path -Path $dayDir)) {
        New-Item -ItemType Directory -Path "$dayDir" | Out-Null
        Write-Host "Created directory $dayDir... ✓" -ForegroundColor Green
    } else {
        Write-Host "Directory $dayDir already exists, skipping... ✗" -ForegroundColor Red
    }

    $pyFile = "$dayDir\day$i.py"
    if (-Not (Test-Path -Path $pyFile)) {    
        $pyfileContent = @"
# Solution for Advent of Code $year, Day $i
# https://adventofcode.com/$year/day/$i

from time import time

from aocd import get_data


# Problem things go here :)

start_time = time()


def load_data(use_test_data=False):
    if use_test_data:
        with open("test.txt") as f:  # noqa: PTH123
            return f.read()
    else:
        return get_data(day=9, year=2024)


data = list(load_data(use_test_data=0))

# Parsing stuff
data = [line.split() for line in data.splitlines()]

print(f"Part1:",)
print(f"Part2:",)

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")
"@
        $pyfileContent | Set-Content -Path $pyFile
        Write-Host "Created file $pyFile... ✓" -ForegroundColor Green
    } else {
        Write-Host "File $pyFile already exists, skipping... ✗" -ForegroundColor Red
    }

    $inputFile = "$dayDir\input.txt"
    if (-Not (Test-Path -Path $inputFile)) {
        New-Item -ItemType File -Path $inputFile | Out-Null
        Write-Host "Created file $inputFile... ✓" -ForegroundColor Green
    } else {
        Write-Host "File $inputFile already exists, skipping... ✗" -ForegroundColor Red
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
# Advent of Code $year, Day $i
"@
    $readmeContent | Set-Content -Path "$dayDir\README.md"
    Write-Host "Created file $readmeFile... ✓" -ForegroundColor Green
    } else {
        Write-Host "File $readmeFile already exists, skipping... ✗" -ForegroundColor Red
    }

    $gitignoreEntry = "$year/day$i"
    if ($gitignoreEntries -notcontains $gitignoreEntry) {
        Add-Content -Path $gitignorePath -Value $gitignoreEntry
        Write-Host "Added $gitignoreEntry to .gitignore... ✓" -ForegroundColor Green
    } else {
        Write-Host "$gitignoreEntry already exists in .gitignore, skipping... ✗" -ForegroundColor Red
    }
}   

Write-Host "================="
Write-Host "Done! Love you. Bye! <3" -ForegroundColor Magenta