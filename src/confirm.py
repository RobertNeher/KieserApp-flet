from flet import (
    AlertDialog,
    ElevatedButton,
    MainAxisAlignment,
    Text,
    TextButton,
    UserControl,

)

class ConfirmDialog(UserControl):
    def __init__(self):
        super().__init__()

        self.dlg = AlertDialog(
            title=Text("Bitte Löschen bestätigen")
        )

        self.dlg_modal = AlertDialog(
            modal=True,
            title=Text("Bitte bestätige das Löschen"),
            content=Text("Möchten die ausgewählten Trainingsresultate löschen?"),
            actions=[
                TextButton("Ja", on_click=self.close_dlg),
                TextButton("Nein", on_click=self.close_dlg),
            ],
            actions_alignment=MainAxisAlignment.END,
        )

    def open_dlg(self, e):
        self.page.dialog = self.dlg
        self.dlg.open = True
        self.page.update()

    def open_dlg_modal(self, e):
        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()

    def build(self):
        self.page.add(
            ElevatedButton("Open dialog", on_click=self.open_dlg),
            ElevatedButton("Open modal dialog", on_click=self.open_dlg_modal),
        )
