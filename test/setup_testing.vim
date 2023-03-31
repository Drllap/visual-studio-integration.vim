if !exists("s:runtim_path_updated")
  echo "Runtime paht set"
  let s:runtim_path_updated = ""
  let &runtimepath.=','..getcwd()
endif
map <leader>b :wa <bar> :py3file test/test.py<CR>
map <leader>R :wa <bar> :py3 reload()<CR>
