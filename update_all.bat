@echo off
:: Styled Update Script for Windows

:: Function to print colorful text
set "RESET="
set "RED=[31m"
set "GREEN=[32m"
set "YELLOW=[33m"
set "BLUE=[34m"

echo [34m========================================
echo Updating Combined Repository and Subtrees
echo ========================================[RESET]

:: Pull updates for the combined repo
echo [33mPulling updates for the combined repo...[RESET]
git pull origin main
if %errorlevel%==0 (
    echo [32mCombined repo updated successfully![RESET]
) else (
    echo [31mFailed to update combined repo! Check for errors.[RESET]
)
pause

:: Pull updates for each subtree
for %%R in (
    "dyslexia-detection-api git@github.com:edulex/detection-api.git main"
    "backend git@github.com:edulex/backend.git main"
    "landing git@github.com:edulex/landing.git prod" :: Use prod branch
    "app git@github.com:edulex/app.git main"
) do (
    for /f "tokens=1,2,3 delims= " %%A in (%%R) do (
        echo [33mPulling updates for %%A (branch: %%C)...[RESET]
        git subtree pull --prefix=%%A %%B %%C
        if %errorlevel%==0 (
            echo [32m%%A (branch: %%C) updated successfully![RESET]
        ) else (
            echo [31mFailed to update %%A (branch: %%C)! Check for errors.[RESET]
        )
    )
)

pause
echo [34m========================================
echo All repositories updated successfully!
echo ========================================[RESET]
pause
