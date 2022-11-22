chcp 65001
:: @File: AutoRemove.bat
:: @Author: Alice(From Chengdu.China)
:: @HomePage: https://github.com/AliceEngineerPro
:: @CreatedTime: 2022/10/31 15:42

@echo off

:: 路径
set DataDir=D:\downloads
:: n天之前
set DaysAgo=30
:: 扩展名, 支持通配符
set Ext=*.*

forfiles /p %DataDir% /s /m %Ext% /d -%DaysAgo% /c "cmd /c if @isdir==TRUE (rmdir /q /s @path) else (del /f @path)"
echo OK
pause
