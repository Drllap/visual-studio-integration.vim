import VS_wrapper
import Vim_wrapper

def reload():
    from importlib import reload
    reload(VS_wrapper)
    reload(Vim_wrapper)



#  Vim_wrapper.Vim_wrapper()
#  Vim_wrapper.set_solution()
Vim_wrapper.activate()
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

