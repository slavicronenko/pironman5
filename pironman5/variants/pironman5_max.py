class Pironman5Max:
    NAME = "Pironman 5 Max"
    ID = "pironman5"
    PRODUCT_VERSION = ""
    PERIPHERALS = [
        'storage',
        "cpu",
        "network",
        "memory",
        "history",
        "log",
        "ws2812",
        "cpu_temperature",
        "gpu_temperature",
        "temperature_unit",
        "oled",
        "clear_history",
        "delete_log_file",
        "pwm_fan_speed",
        "pwm_gpio_fan",
        "vibration_switch",
        "oled_sleep",
    ]
    SYSTEM_DEFAULT_CONFIG = {
        'data_interval': 1,
        "rgb_color": "#0a1aff",
        "rgb_brightness": 50,
        "rgb_style": "breathing",
        "rgb_speed": 50,
        "rgb_enable": True,
        "rgb_led_count": 4,
        "temperature_unit": "C",
        "oled_enable": True,
        "oled_rotation": 0,
        "oled_disk": "total",
        "oled_network_interface": "all",
        'gpio_fan_pin': 6,
        'fan_cooling_level': 0.5,
        'oled_sleep_timeout': 10,
        'vibration_switch_pin': 26,
        'vibration_switch_pull_up': False,
    }
    DT_OVERLAYS = [
        'sunfounder-pironman5.dtbo',
    ]
