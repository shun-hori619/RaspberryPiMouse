# テスト

import time
import module as mod # type: ignore

# モーターを有効にする
mod.motor_enable(True)

# 直進（左PWM, 右PWM, 動作時間[ミリ秒]）
mod.move(100, 100, 5000)  # 2秒間、左右ともPWM=100で前進

# モーターを無効にする（安全のため）
mod.motor_enable(False)