if !exists("s:runtim_path_updated")
  echo "Runtime path set"
  let s:runtim_path_updated = ""
  let &runtimepath.=','..getcwd()
endif

map <leader>R :wa <bar> :messages clear <bar> :py3 reload()<CR>
map <leader>b :wa <bar> :messages clear <bar> :py3file test/test.py<CR>

command! VSIBpToggle          :py3 vim_vs_wrap.toggle_breakpoint()
command! VSISetSolution       :py3 vim_vs_wrap.set_solution()
command! VSISetStartupProject :py3 vim_vs_wrap.set_startup_project()
command! VSIOpen              :py3 vim_vs_wrap.open_current()

" call sign_define("VSI_Breakpoint_Enabled", { 🐮
"
"

call sign_define('VSI_BreakpointEnabled',
      \ {"text": "🛑", })

call sign_place(0, 'VSI', 'VSI_BreakpointEnabled', 'test/setup_testing.vim', { 'lnum': 16})
