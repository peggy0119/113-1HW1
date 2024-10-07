import unittest

def celsius_to_fahrenheit(celsius):  # 將攝氏轉換為華氏
    return (celsius * 9/5) + 32

class TestTemperatureConversion(unittest.TestCase):

    def test_zero_celsius(self):  # 測試 0°C 轉換為 32°F
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_boiling_point(self):  # 測試水的沸點 100°C 轉換為華氏溫度
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_negative_celsius(self):  # 測試負數攝氏溫度
        self.assertEqual(celsius_to_fahrenheit(-40), -40)  # -40°C = -40°F

    def test_positive_celsius(self):  # 測試正數攝氏溫度轉換
        self.assertEqual(celsius_to_fahrenheit(37), 98.6)  # 37°C = 98.6°F

if __name__ == '__main__':
    unittest.main()  # 自動執行所有以 test_ 開頭的測試
