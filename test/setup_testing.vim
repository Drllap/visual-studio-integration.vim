if !exists("s:runtim_path_updated")
  echo "Runtime path set"
  let s:runtim_path_updated = ""
  let &runtimepath.=','..getcwd()
endif

map <leader>R :wa <bar> :messages clear <bar> :py3 reload()<CR>
map <leader>b :wa <bar> :messages clear <bar> :py3file test/test.py<CR>

command! VSISetSolution :py3 vim_vs_wrap.set_solution()
command! VSIOpen        :py3 vim_vs_wrap.open_current()

imap <C-v> :normal :VSIOpen<CR>
