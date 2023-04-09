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
    class NoLink(IndexError):
        pass

    def __init__(self) -> None:
        self.tab_based_config = True
        self.reload()

    def open_current(self):
        try:
            inst = self._get_linked_instance()
            b = vim.current.buffer
            file = b.name
            line, col = vim.current.window.cursor
            inst.open_location(file, line, col)
        except Vim_wrapper.NoLink:
            pass

    def reload(self):
        self.instances = VS_wrapper.get_instances()

    def activate(self):
        self._forward_to_linked(VS_wrapper.Instance.activate)

    def set_focus(self):
        self._forward_to_linked(VS_wrapper.Instance.set_focus)

    def start_debugging(self):
        self._forward_to_linked(VS_wrapper.Instance.start_debugging)

    @staticmethod
    def _get_format_str(is_current):
        if is_current:
            return "\t*{}: {}"
        return "\t {}: {}"

    def set_startup_project(self):
        try: 
            inst = self._get_linked_instance()
            current_startup_project = inst.get_startup_project()
            project_list = inst.get_project_list()

            selections_strings = \
             [ Vim_wrapper._get_format_str(p.Name == current_startup_project).format(idx, p)
               for idx, p in enumerate(project_list) ]
            selections_strings.insert(0, "Select Project")
            selected = vim.funcs.inputlist(selections_strings)

            if selected in range(0, len(project_list)):
                inst.set_startup_project(project_list[selected])

        except Vim_wrapper.NoLink:
            pass

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
            format = Vim_wrapper._get_format_str(current is not None and current == key)
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
        raise Vim_wrapper.NoLink

    def _forward_to_linked(self, VS_wrapper_mothod):
        try:
            VS_wrapper_mothod(self._get_linked_instance())
        except Vim_wrapper.NoLink:
            pass

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
