import pythoncom
import win32com.client

class Instance:
    def __init__(self, dte):
        if type(dte) is win32com.client.CDispatch:
            self.dte = dte
        else:
            print("dte not a win32com.client.CDispatch")

    def activate(self):
        self.dte.MainWindow.Activate

    def set_focus(self):
        self.dte.MainWindow.SetFocus

    def open_location(self, file, line=None, col=None):
        import os
        self.dte.ItemOperations.OpenFile(os.path.abspath(file))
        if line is not None:
            col = col or 1
            self.dte.ActiveDocument.Selection.MoveToLineAndOffset(line, col+1)

    def get_solution_name(self):
        return str(self.dte.Solution.FullName)

    def build_solution(self):
        self.dte.Solution.SolutionBuild.Build()

    def compile_file(self):
        self.dte.ExecuteCommand('Build.Compile')

    def get_caption(self):
        return self.dte.MainWindow.Caption

    def get_project_list(self):
        return [ p for p in self.dte.Solution.Projects ]

    def get_startup_project(self):
        return self.dte.Solution.Properties("StartupProject").Value

    def set_startup_project(self, project):
        self.dte.Solution.Properties("StartupProject").Value = project

    def start_debugging(self):
        self.dte.Debugger.Go(False)

def get_instances():
    ret = {}
    obj_table = pythoncom.GetRunningObjectTable()
    enum = obj_table.EnumRunning()
    while True:
        monikers = enum.Next()
        if not monikers:
            break
        ctx = pythoncom.CreateBindCtx()
        display_name = monikers[0].GetDisplayName(ctx,None)
        if display_name.startswith('!VisualStudio.DTE'):
            obj = obj_table.GetObject(monikers[0])
            interface = obj.QueryInterface(pythoncom.IID_IDispatch)
            try:
                pid = int(display_name[display_name.rfind(':')+1:])
                ret[pid] = Instance(win32com.client.Dispatch(interface))
            except ValueError:
                print("Unable to get DTEs PID")

    return ret

if __name__ == '__main__':
    instances = get_instances()
    print(instances[0].get_caption())
    print(instances[1].get_solution_name())
    #  print(get_instances())

