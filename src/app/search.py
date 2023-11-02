import dearpygui.dearpygui as dpg

class SearchGUI:
    def __init__(self) -> None:
        
        dpg.create_context()
        dpg.create_viewport(title='Search Page', width=390, height=100)
        
        with dpg.window(tag="search_page", no_collapse=True, no_title_bar=True, no_resize=True,
                            no_close=True, no_move=True, width=390, height=100): 
             
            dpg.add_spacing(count=3) 
            dpg.add_input_text(tag="query", label="Search")
            dpg.add_spacing(count=2) 
            dpg.add_radio_button(items=["Username", "Website"], horizontal=True, tag="SearchType", default_value="Username")


    def run(self):
            dpg.setup_dearpygui()
            dpg.show_viewport()
            dpg.start_dearpygui()
            dpg.destroy_context()


if __name__ == "__main__":
    SearchGUI().run()