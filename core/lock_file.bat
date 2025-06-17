@echo off
SET "FILE=%~1"

IF "%FILE%"=="" (
    ECHO Usage: lock_file.bat <file_path>
    EXIT /B 1
)

:: Make file read-only
attrib +R "%FILE%"

:: Deny write and delete access for current user
icacls "%FILE%" /deny "%USERNAME%:W"
icacls "%FILE%" /deny "%USERNAME%:D"

echo File locked successfully on Windows.
