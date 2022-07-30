from gpiozero import LED # import LED dari gpiozero library

led_1 = LED(20) # menetapkan pin GPIO yang akan kita hubungkan dengan LED

while True:
  led_red.on() # loop untuk terus menyalakan lampu LED