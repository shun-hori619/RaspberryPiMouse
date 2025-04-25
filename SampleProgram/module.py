# 制御用モジュール
import time
def read_lightsensors():
    """光センサーの値（前右, 右, 左, 前左）を取得"""
    with open("/dev/rtlightsensor0", "r") as f:
        return list(map(int, f.read().split()))
def read_switch(index):
    """スイッチの状態を取得（0: 押されている, 1: 押されていない）"""
    with open(f"/dev/rtswitch{index}", "r") as f:
        return int(f.read().strip())
def set_led(index, state):
    """LEDを点灯（state=True）または消灯（state=False）"""
    with open(f"/dev/rtled{index}", "w") as f:
        f.write("1\n" if state else "0\n")
def beep(freq=440):
    """ブザーを鳴らす（freq=0で停止）"""
    with open("/dev/rtbuzzer0", "w") as f:
        f.write(f"{freq}\n")
def motor_enable(state):
    """モーター制御の有効化/無効化"""
    with open("/dev/rtmotoren0", "w") as f:
        f.write("1\n" if state else "0\n")
def move(left_pwm, right_pwm, duration_ms):
    """モーターをPWM指定で動かす"""
    with open("/dev/rtmotor0", "w") as f:
        f.write(f"{left_pwm} {right_pwm} {duration_ms}\n")









