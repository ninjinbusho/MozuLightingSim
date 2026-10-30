# memo: 装置固有デバイスドライバではフェーダーパラメータは通常扱わず、より高位のプライマリデバイスドライバが設定を行う想定になっている。
class light_driver:
    def __init__(self, mode: list, option: dict) -> None:
        self.chm = mode
        self.color = [0, 0, 0, 0]
    def reset(self) -> dict:
        self.color = [0, 0, 0, 0]
        return {
            self.chm[0] +  0 : {"value": 0, "fade": 0.0},
            self.chm[0] +  1 : {"value": 0, "fade": 0.0},
            self.chm[0] +  2 : {"value": 0, "fade": 0.0},
            self.chm[0] +  3 : {"value": 0, "fade": 0.0},
            self.chm[0] +  4 : {"value": 0, "fade": 0.0},
            self.chm[0] +  5 : {"value": 0, "fade": 0.0},
            self.chm[0] +  6 : {"value": 0, "fade": 0.0},
            self.chm[0] +  7 : {"value": 0, "fade": 0.0},
            self.chm[0] +  8 : {"value": 0, "fade": 0.0},
            self.chm[0] +  9 : {"value": 0, "fade": 0.0},
            self.chm[0] + 10 : {"value": 0, "fade": 0.0},
            self.chm[0] + 11 : {"value": 0, "fade": 0.0},
            self.chm[0] + 12 : {"value": 128, "fade": 0.0},# 13ch目(ディマー)を常にMAXの半分（128, 明るすぎるので）にする
        }
    def close(self) -> dict:
        return dict()
    def info(self) -> str:
        return "(C)2023 /\/asTTY\ngeneral 4 x RGB LED driver."
    def apiver(self) -> int:
        return 1
    def displayparam(self) -> list:
        return [
            {
                "category": "color.rgb",
                "type": "int",
                "value": self.color[0],
                "alloc": self.chm[0] + 0
            },
            {
                "category": "color.rgb",
                "type": "int",
                "value": self.color[1],
                "alloc": self.chm[0] + 3
            },
            {
                "category": "color.rgb",
                "type": "int",
                "value": self.color[2],
                "alloc": self.chm[0] + 6
            },
            {
                "category": "color.rgb",
                "type": "int",
                "value": self.color[3],
                "alloc": self.chm[0] + 9
            },
        ]
    def paramlist(self) -> list:
        return ["color1", "color2", "color3", "color4"]
    def set(self, param_name: str, value: int|float, fader: int|float) -> dict:
        if param_name == "color1":
            self.color[0] = value
            return {
                self.chm[0] +  0 : {"value": 128, "fade": fader},#Dimmer半分
                self.chm[0] +  0 : {"value": value // 65536,       "fade": fader},
                self.chm[0] +  1 : {"value": value % 65536 // 256, "fade": fader},
                self.chm[0] +  2 : {"value": value % 256,          "fade": fader}
            }
        elif param_name == "color2":
            self.color[1] = value
            return {
                self.chm[0] +  3 : {"value": value // 65536,       "fade": fader},
                self.chm[0] +  4 : {"value": value % 65536 // 256, "fade": fader},
                self.chm[0] +  5 : {"value": value % 256,          "fade": fader}
            }
        elif param_name == "color3":
            self.color[2] = value
            return {
                self.chm[0] +  6 : {"value": value // 65536,       "fade": fader},
                self.chm[0] +  7 : {"value": value % 65536 // 256, "fade": fader},
                self.chm[0] +  8 : {"value": value % 256,          "fade": fader}
            }
        elif param_name == "color4":
            self.color[3] = value
            return {
                self.chm[0] +  9 : {"value": value // 65536,       "fade": fader},
                self.chm[0] + 10 : {"value": value % 65536 // 256, "fade": fader},
                self.chm[0] + 11 : {"value": value % 256,          "fade": fader}
            }
        else:
            return dict()
    def get(self, param_name: str) -> any:
        if param_name == "color1":
            return self.color[0]
        elif param_name == "color1":
            return self.color[1]
        elif param_name == "color2":
            return self.color[2]
        elif param_name == "color3":
            return self.color[3]
        else:
            return None
