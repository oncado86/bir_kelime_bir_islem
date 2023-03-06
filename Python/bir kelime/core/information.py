from PyQt5.QtWidgets import QMessageBox as message_box


class Information:
    """Programın her yerinde bilgilendirme mesajları vermeye yarar"""

    def __init__(self):
        """Programın her yerinde bilgilendirme mesajları vermeye yarar"""

    def information_message(self, info_message: str) -> None:
        """Bilgilendirme mesajı verir
            
            Args:
                info_message (str): Bilgi metni"""
        message = message_box()
        message.critical(
            None,  # type: ignore
            "Dikkat",
            info_message,
            message_box().StandardButton.Ok
        )
