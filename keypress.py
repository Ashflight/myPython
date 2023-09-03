import keyboard


def on_key_event(e):
    if e.event_type == keyboard.KEY_UP:
        print(f"Key {e.name} was released")


keyboard.hook(on_key_event)
print("please press the key")
keyboard.wait("esc")  # Wait for the 'esc' key to be pressed
