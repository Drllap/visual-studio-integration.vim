import VS_wrapper
import Vim_wrapper

def reload():
    from importlib import reload
    reload(VS_wrapper)
    reload(Vim_wrapper)

    #  global vim_vs_wrap
    #  vim_vs_wrap = Vim_wrapper.Vim_wrapper()

    #  vim_vs_wrap.set_solution()

reload()

#  if 'vim_vs_wrap' not in globals():
    #  print("creating vim_vs_wrap")
    #  global vim_vs_wrap
    #  vim_vs_wrap = Vim_wrapper.Vim_wrapper()

def fle(a, b, c):
    print("Multiply: ", a*b*c)

#  fle(1, 2, 3)

def forwarder(func, *args):
    func(*args)

#  forwarder(fle, 4, 2, 3)
vim_vs_wrap = Vim_wrapper.Vim_wrapper()
vim_vs_wrap.toggle_breakpoint()
#  vim_vs_wrap.test()
#  vim_vs_wrap.set_startup_project()
#  vim_vs_wrap.open_current()

#  vim_vs_wrapper.set_solution()
#  vim_vs_wrap.activate()
#  vim_vs_wrap.set_focus()
#  w.open_current()
#  print(Vim_wrapper.__dict__)

#  i = VS_wrapper.get_instances()
#  print(type(next(iter(i))))


#  w.set_solution()
#  print(w._get_current_solution())
#  print(vim.__dict__.keys())
#  print(w._get_current_solution())
#  print(vim.vars["vsi_so"])
#  print(vim.vars["vsi_so"])

#  print(help( vim ))
#  vim.current.tabpage.vars["ttt"] = "wtf is going on"
#  print(vim.current.tabpage.vars["ttt"])
#  vim.api.tabpage_del_var(0, "ttt")
#  print(vim.current.tabpage.vars["ttt"])
#  print(help(vim.current.tabpage.vars))
#  vim.current.tabpage.vars.__delitem__("non_existing")
#  print(vim.current.tabpage.vars.get("non_existing", "fle"))
#  print(vim.current.tabpage.vars.nvim_tabpage_del_var(0, "non_existing"))
#  print(vim.api.nvim_tabpage_del_var(0, "non_existing"))
#  print(help(vim))

