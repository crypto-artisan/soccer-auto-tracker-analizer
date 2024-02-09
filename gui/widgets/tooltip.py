from tkinter import Toplevel
from tkinter.ttk import Widget, Label


class ToolTip:
    def __init__(self, widget: Widget):
        self._widget = widget
        self._tip_window = None

    def showtip(self, text: str):
        if self._tip_window is not None:
            return

        x, y, cx, cy = self._widget.bbox('insert')
        x = x + self._widget.winfo_rootx() + 57
        y = y + cy + self._widget.winfo_rooty() + 27
        self._tip_window = Toplevel(self._widget)
        self._tip_window.wm_overrideredirect(1)
        self._tip_window.wm_geometry('+%d+%d' % (x, y))
        label = Label(
            self._tip_window, text=text, justify='left', relief='solid', borderwidth=1, font=('arial', '8', 'normal')
        )
        label.pack(ipadx=1)

    def hidetip(self):
        if self._tip_window:
            self._tip_window.destroy()
        self._tip_window = None
