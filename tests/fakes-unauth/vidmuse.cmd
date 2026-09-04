@echo off

if "%~1"=="--version" (
  echo vTEST_ONLY
  exit /b 0
)

if "%~1 %~2"=="profile get" (
  echo TEST_ONLY_AUTH_REQUIRED 1>&2
  exit /b 3
)

echo unsupported test command 1>&2
exit /b 2
