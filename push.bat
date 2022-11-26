git add .
git commit -m "'"
git push

robocopy .\public ..\mp\ /E
cd ..
cd mp
git add .
git commit -m "'"
git push
cd ..
cd mp_wb_compiler