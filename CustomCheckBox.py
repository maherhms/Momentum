from flet import *

class CustomCheckBox(UserControl):
    def __init__(self, color, label='', selection_fill='#183588', size=25, stroke_width=2, animation=None, checked=False, font_size=17, pressed=None):
        super().__init__()
        self.selection_fill = selection_fill
        self.color = color
        self.label = label
        self.size = size
        self.stroke_width = stroke_width
        self.animation = animation
        self.checked = checked
        self.font_size = font_size
        self.pressed = pressed
        self.delete_button = self.taskDeleteEdit(icons.DELETE_FOREVER_ROUNDED, 'red500', None)  # Removed self-deletion
        self.delete_button.opacity = 0  # Initially hide the button
        self.edit_button = self.taskDeleteEdit(icons.EDIT_ROUNDED, 'white700', None)
        self.edit_button.opacity = 0

    def _checked(self):
        self.check_box = Container(
            animate=self.animation,
            width=self.size,
            height=self.size,  # Ensure the height is the same as size
            border_radius=(self.size / 2) + 5,
            bgcolor=self.selection_fill,
            content=Icon(icons.CHECK_ROUNDED, size=15),
            alignment=alignment.center  # Center the icon within the container
        )
        return self.check_box

    def _unchecked(self):
        self.check_box = Container(
            animate=self.animation,
            width=self.size,
            height=self.size,
            border_radius=(self.size / 2) + 5,
            bgcolor=None,
            border=border.all(color=self.color, width=self.stroke_width),
            content=Container(),
            alignment=alignment.center  # Center the content within the container
        )
        return self.check_box

    def build(self):
        row_content = Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,  # Space between items in the row
            vertical_alignment=CrossAxisAlignment.CENTER,  # Center items vertically
            controls=[
                Row(
                    alignment=alignment.center,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        self._checked() if self.checked else self._unchecked(),
                        Text(
                            self.label,
                            font_family='poppins',
                            size=self.font_size,
                            weight=FontWeight.W_300
                        ),
                    ]
                ),
                Row(
                    controls=[
                        self.edit_button,
                        self.delete_button
                    ]
                )
            ]
        )

        return Container(
            alignment=alignment.center,
            height=self.size,  # Ensure container height is consistent
            content=row_content,
            on_click=lambda e: self.checked_check(e),
            on_hover=lambda e: self.showIcons(e)  # Handle hover events
        )

    def taskDeleteEdit(self, name, color, on_click_action):
        return IconButton(
            icon=name,
            alignment=alignment.center,
            height=self.size,  # Ensure icon button height is consistent
            icon_size=18,
            icon_color=color,
            opacity=0,  # Start with the button hidden
            animate_opacity=200,
            on_click=on_click_action
        )

    def showIcons(self, e):
        hover = e.data == "true"
        self.delete_button.opacity = 1 if hover else 0
        self.edit_button.opacity = 1 if hover else 0
        self.update()

    def checked_check(self, e):
        self.checked = not self.checked
        self.check_box.border = None if self.checked else border.all(color=self.color, width=self.stroke_width)
        self.check_box.bgcolor = self.selection_fill if self.checked else None
        self.check_box.content = Icon(icons.CHECK_ROUNDED, size=15) if self.checked else Container()
        self.update()

    def is_checked(self):
        return self.checked

    def run(self, *args):
        self.pressed(args)
