python3 import Vim_wrapper
python3 vim_vs_wrap = Vim_wrapper.Vim_wrapper()

command! VSIBpToggle          :py3 vim_vs_wrap.toggle_breakpoint()
command! VSISetSolution       :py3 vim_vs_wrap.set_solution()
command! VSISetStartupProject :py3 vim_vs_wrap.set_startup_project()
command! VSIOpen              :py3 vim_vs_wrap.open_current()
