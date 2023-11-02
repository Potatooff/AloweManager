import dearpygui.dearpygui as dpg

import dearpygui.dearpygui as dpg


class HomeGUI:
    def __init__(self) -> None:
        
        dpg.create_context()
        dpg.create_viewport(title='ALOWE', width=900, height=900)

        with dpg.window(tag="main", no_collapse=True, no_title_bar=True, no_resize=True,
                            no_close=True, no_move=True, width=900, height=900):
        
            dpg.add_spacing(count=5)





    def run(self) -> None:
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("main", True)
        dpg.start_dearpygui()
        dpg.destroy_context()


if __name__ == "__main__":
    HomeGUI().run()