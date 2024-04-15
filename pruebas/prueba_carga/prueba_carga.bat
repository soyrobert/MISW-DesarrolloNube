@echo off
setlocal enabledelayedexpansion

rem Set the token value here
set "token=your_token_value"

for /L %%i in (1,1,2) do (
    set /a "rate=%%i * 100"  REM Increment in steps of 100 requests per second
    ab -n 1000 -c !rate! -p post_data.txt -T "multipart/form-data; boundary=1234567890" -H "Authorization: Bearer !token!" -rk -g prueba_carga.csv http://localhost:8000/api/tasks
)

endlocal
