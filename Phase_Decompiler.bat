@echo off
title Cog Invasion Phase File Decompiler

set /p file=What phase file do you want decompiled? 
ppython.exe tools\tool_Multifile.py --filename %file% --mtype decompile

echo Done!
pause >nul
exit
