import vim
import pynvim
import VS_wrapper

tab_based_config = False
instances = VS_wrapper.get_instances()
#  def __init__(self) -> None:
    #  self.tab_based_config = False

#  def set_use_tab_based_config(tab_based=True):
#      tab_based_config = tab_based

def open_current():
    inst = _get_linked_instance()
    if inst is None:
        return
    b = vim.current.buffer
    file = b.name
    print(file)
    row, line = vim.current.window.cursor
    print("row: {}, line {}".format(row, line))
    inst.open_location(file, line, row)

def reload():
    global instances
    instances = VS_wrapper.get_instances()

def activate():
    inst = _get_linked_instance()
    if inst is None:
        return

def set_solution():
    global instances
    instances = VS_wrapper.get_instances()
    if len(instances) == 0:
        print("No instances detected")
        _set_current_solution(None)
        return
    if len(instances) == 1:
        _set_current_solution(next(iter(instances)))
        print("One instance found and set")
        return

    current = _get_linked_instance_key()

    text = ["Select Solution"]

    select_dict = {}
    counter = 1
    for (key, value) in instances.items():
        if current is not None and current == key:
            format = "\t*{}: {}"
        else:
            format = "\t {}: {}"
        text.append(format.format(counter, value.get_solution_name()))

        select_dict[counter] = key
        counter += 1

    selected_key = vim.funcs.inputlist(text)
    if selected_key in select_dict:
        _set_current_solution(select_dict[selected_key])

def _get_linked_instance_key():
    if vim.current.tabpage.vars.get("vsi_current") is not None:
        return vim.current.tabpage.vars["vsi_current"]

    return vim.vars.get("vsi_current")

def _get_linked_instance():
    key = _get_linked_instance_key()
    if key in instances:
        return instances[key]
    print("Linked instance key isn't in instance dict. Run set_solution to re-initialize")
    return None


def _set_current_solution(value):
    if value is None:
        exists = vim.funcs.exists
        if exists("t:vsi_current"): vim.api.tabpage_del_var(0, "vsi_current")
        if exists("g:vsi_current"): vim.api.del_var("vsi_current")
        return

    if tab_based_config:
        vim.current.tabpage.vars["vsi_current"] = value
    else:
        vim.vars["vsi_current"] = value
