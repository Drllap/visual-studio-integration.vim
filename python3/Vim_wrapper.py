import vim
import pynvim
import VS_wrapper

#  tab_based_config = False
#  instances = VS_wrapper.get_instances()
#  def __init__(self) -> None:
    #  self.tab_based_config = False

#  def set_use_tab_based_config(tab_based=True):
#      tab_based_config = tab_based

class Vim_wrapper:
    def __init__(self) -> None:
        self.tab_based_config = True
        self.reload()

    def open_current(self):
        inst = self._get_linked_instance()
        if inst is None:
            return
        b = vim.current.buffer
        file = b.name
        line, col = vim.current.window.cursor
        inst.open_location(file, line, col)

    def reload(self):
        self.instances = VS_wrapper.get_instances()

    def activate(self):
        inst = self._get_linked_instance()
        if inst is None:
            return
        inst.activate()

    def set_focus(self):
        inst = self._get_linked_instance()
        if inst is None:
            return
        inst.set_focus()

    def set_solution(self):
        self.instances = VS_wrapper.get_instances()
        if len(self.instances) == 0:
            print("No instances detected")
            self._set_current_solution(None)
            return
        if len(self.instances) == 1:
            self._set_current_solution(next(iter(self.instances)))
            print("One instance found and set")
            return

        current = self._get_linked_instance_key()

        text = ["Select Solution"]

        select_dict = {}
        counter = 1
        for (key, value) in self.instances.items():
            if current is not None and current == key:
                format = "\t*{}: {}"
            else:
                format = "\t {}: {}"
            text.append(format.format(counter, value.get_solution_name()))

            select_dict[counter] = key
            counter += 1

        selected_key = vim.funcs.inputlist(text)
        if selected_key in select_dict:
            self._set_current_solution(select_dict[selected_key])

    def _get_linked_instance_key(self):
        if vim.current.tabpage.vars.get("vsi_current") is not None:
            return vim.current.tabpage.vars["vsi_current"]

        return vim.vars.get("vsi_current")

    def _get_linked_instance(self):
        key = self._get_linked_instance_key()
        if key in self.instances:
            return self.instances[key]
        print("Linked instance key isn't in instance dict. Run set_solution to re-initialize")
        return None


    def _set_current_solution(self, value):
        if value is None:
            exists = vim.funcs.exists
            if exists("t:vsi_current"): vim.api.tabpage_del_var(0, "vsi_current")
            if exists("g:vsi_current"): vim.api.del_var("vsi_current")
            return

        if self.tab_based_config:
            vim.current.tabpage.vars["vsi_current"] = value
        else:
            vim.vars["vsi_current"] = value
