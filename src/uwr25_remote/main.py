from gamepad import logicool_controller
from controller import Controller
from communicator import SerialCommunicator

def main():
    gamepad = logicool_controller()
    controller = Controller()
    communicator = SerialCommunicator()
    communicator.open()
    while True:
        try:
            status = gamepad.check_state()
            #print(status)
            cmd_vel = controller.gen_cmd_vel(status)
            #print(cmd_vel)
            data = communicator.communicate(cmd_vel)
            #print(data)
            print(f"\rSent: {data.strip()}    ", end='', flush=True)

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
