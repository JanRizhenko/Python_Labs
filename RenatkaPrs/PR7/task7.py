import math

def sine_degree(angle_deg):
    angle_rad = math.radians(angle_deg)
    return math.sin(angle_rad)

angle = float(input("Введіть кут в градусах: "))

result = sine_degree(angle)
result = round(result, 3)

print(f"Синус кута {angle}° дорівнює {result}")
