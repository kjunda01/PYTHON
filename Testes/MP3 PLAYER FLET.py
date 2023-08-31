import flet as ft
import datetime

url = "https://luan.xyz/files/audio/ambient_c_motion.mp3"
#path = "C:/Users/Kjunda01/OneDrive - MSFT/PROJETOS/Curso em Video Python/Player de Musica/outfoxing.mp3"

def main(page: ft.Page):

    def pause(e):
        audio1.pause()
        audio1.update()

    def volume_down(_):
        audio1.volume -= 0.1
        audio1.update()

    def volume(e):
        knob = float(e.data)
        audio1.volume = 0.0 + knob
        audio1.update()
    
    def volume_mute(e):
        audio1.volume = 0.0
        audio1.update()
    
    def volume_unmute(e):
        audio1.volume = 1.0
        audio1.update()

    def volume_up(_):
        audio1.volume += 0.1
        audio1.update()

    def balance_left(_):
        audio1.balance -= 0.1
        audio1.update()

    def balance_right(_):
        audio1.balance += 0.1
        audio1.update()

    def pick_files(self):
        ft.FilePicker(on_result=self.pick_files_result)


    audio1 = ft.Audio(
        src=url,
        autoplay=False,
        volume=1,
        balance=0,
        on_loaded=lambda _: print("Loaded"),
        on_duration_changed=lambda e: print("Duration changed:", e.data),
        on_position_changed=lambda e: print("Position changed:", e.data),
        on_state_changed=lambda e: print("State changed:", e.data),
        on_seek_complete=lambda _: print("Seek complete"),
    )
    
    page.overlay.append(audio1)

    page.add(
        ft.ElevatedButton("Play", on_click=lambda _: audio1.play()),
        ft.Slider(min=0/100, max=100/100, divisions=10, label="{value}", width=500, on_change=volume),
        ft.ElevatedButton("Pause", on_click= pause),
        ft.ElevatedButton("Resume", on_click=lambda _: audio1.resume()),
        ft.ElevatedButton("Release", on_click=lambda _: audio1.release()),
        ft.ElevatedButton("Seek 2s", on_click=lambda _: audio1.seek(2000)),
        ft.ElevatedButton("Mute", icon=ft.icons.VOLUME_OFF, on_click=volume_mute),
        ft.ElevatedButton("UnMute", icon=ft.icons.VOLUME_UP, on_click=volume_unmute),
        ft.ElevatedButton("Pick Files", icon=ft.icons.FILE_DOWNLOAD, on_click=ft.FilePicker(on_result=pick_files)),
        



        ft.Row(
            [
                ft.ElevatedButton("Volume down", on_click=volume_down),
                ft.ElevatedButton("Volume up", on_click=volume_up),
            ]
        ),
        
        ft.Row(
            [
                ft.ElevatedButton("Balance left", on_click=balance_left),
                ft.ElevatedButton("Balance right", on_click=balance_right),
            ]
       ),
        
        ft.ElevatedButton(
            "Get duration", on_click=lambda _: print("Duration:", audio1.get_duration())
        ),
        
        ft.ElevatedButton(
            "Get current position",
            on_click=lambda _: print("Current position:", audio1.get_duration()),
        ),
    )

ft.app(target=main)