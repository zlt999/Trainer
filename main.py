import dearpygui.dearpygui as dpg
import time

DT = 0.01

def reset_timer():
    dpg.set_value('timer', 60)

if __name__ == '__main__':
    dpg.create_context()

    with dpg.value_registry():
        dpg.add_float_value(tag='timer')

    with dpg.window(label="Go", width=500, height=500, no_resize=True, no_move=True, no_collapse=True, no_close=True):
        # dpg.add_text("Hello world")
        # dpg.add_input_text(label="string")
        dpg.add_slider_float(label="Timer(s)", source="timer", max_value=60, width=400)
        dpg.add_button(label="Reset timer", callback=reset_timer)

    with dpg.window(label="Set", width=500, height=500, pos=(500,0), no_resize=True, no_move=True, no_collapse=True, no_close=True):
        dpg.add_table(source='item_table')

    dpg.create_viewport(title='Fitness', width=1020, height=550)
    dpg.setup_dearpygui()
    dpg.show_viewport()

    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
        if dpg.get_value(item='timer') > 0:
            dpg.set_value('timer', max(dpg.get_value('timer') - DT, 0))

        time.sleep(DT)

    dpg.destroy_context()
