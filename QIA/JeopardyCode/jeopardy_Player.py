def on_received_number(receivedNumber):
    if receivedNumber == ID:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
radio.on_received_number(on_received_number)

def on_button_pressed_ab():
    radio.send_value("stud1", ID)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

ID = 0
radio.set_group(1)
ID = 8
