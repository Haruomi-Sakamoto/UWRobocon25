# uwr25_remote/controller.py

class Controller:
    def __init__(self):
        self.status = [0] * 20
        self.cmd_vel = {
            "linear": {"x": 0.0, "y": 0.0, "z": 0.0},
            "angular": {"x": 0.0, "y": 0.0, "z": 0.0}
        }
        self.power = 0.4

        def norm(val):
            return max(min(val / 255.0, 1.0), -1.0)
        self.norm = norm

        def gen_cmd_vel(status):
            self.status = status

            LX = self.norm(status[0]) * self.power
            LY = self.norm(status[1]) * self.power
            RX = self.norm(status[2]) * self.power
            RY = self.norm(status[3]) * self.power
            LB = status[8]
            LT = status[10]

            # Z軸移動
            if LB and not LT:
                linear_z = 1.0 * self.power
            elif LT and not LB:
                linear_z = -1.0 * self.power
            else:
                linear_z = 0.0

            self.cmd_vel = {
                "linear": {
                    "x": RX,
                    "y": RY,
                    "z": linear_z
                },
                "angular": {
                    "x": 0.0,
                    "y": 0.0,
                    "z": LX
                }
            }
            return self.cmd_vel

        self.gen_cmd_vel = gen_cmd_vel
