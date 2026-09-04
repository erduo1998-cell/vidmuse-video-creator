@echo off

if "%~1"=="--version" (
  echo vTEST_ONLY
  exit /b 0
)

if "%~1 %~2"=="profile get" (
  if "%VIDMUSE_TEST_UNAUTH%"=="1" (
    echo TEST_ONLY_AUTH_REQUIRED 1>&2
    exit /b 3
  )
  echo {"id":"TEST_ONLY_PROFILE"}
  exit /b 0
)

if "%~1 %~2"=="plan get" (
  echo {"plan":"TEST_ONLY_PLAN"}
  exit /b 0
)

if "%~1 %~2"=="model list" (
  echo {"data":[{"name":"TEST_ONLY_MODEL"}]}
  exit /b 0
)

echo unsupported test command 1>&2
exit /b 2
