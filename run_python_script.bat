@echo off
SETLOCAL

REM 現在のディレクトリを取得
SET CURRENT_DIR=%~dp0

REM ログファイルの名前を設定
SET LOG_FILE=%CURRENT_DIR%logs\%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%_script.log

REM Pythonスクリプトのパスを設定
SET SCRIPT_PATH=%CURRENT_DIR%script.py

REM Pythonインタプリタのパスを設定
SET PYTHON_PATH=C:\path\to\python.exe

REM Pythonスクリプトを実行し、結果をログファイルに出力
"%PYTHON_PATH%" "%SCRIPT_PATH%" > "%LOG_FILE%" 2>&1
SET SCRIPT_EXIT_CODE=%ERRORLEVEL%

REM 戻り値に基づいて適切な戻り値を設定し、ログファイルにメッセージを出力
IF %SCRIPT_EXIT_CODE% EQU 0 (
    echo スクリプトは正常に実行されました。 >> "%LOG_FILE%"
    EXIT /B 0
) ELSE IF %SCRIPT_EXIT_CODE% EQU 4 (
    echo 警告: 詳細はログファイルを確認してください: %LOG_FILE% >> "%LOG_FILE%"
    EXIT /B 4
) ELSE (
    echo エラーが発生しました。詳細はログファイルを確認してください: %LOG_FILE% >> "%LOG_FILE%"
    EXIT /B 8
)

ENDLOCAL
