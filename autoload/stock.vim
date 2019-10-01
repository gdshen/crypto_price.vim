function! HelloWorld()
    echo "Hello World\n"
endfunction
command! -nargs=0 HW call HelloWorld()
