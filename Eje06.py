import json

equipos = [
    {
        "Nombre": "Real Madrid",
        "país": "España",
        "nivelAtaque": 95,
        "nivelDefensa": 90
    },
    {
        "Nombre": "Barcelona",
        "país": "España",
        "nivelAtaque": 92,
        "nivelDefensa": 88
    },
    {
        "Nombre": "Manchester United",
        "país": "Inglaterra",
        "nivelAtaque": 88,
        "nivelDefensa": 85
    },
    {
        "Nombre": "Juventus",
        "país": "Italia",
        "nivelAtaque": 90,
        "nivelDefensa": 92
    }
]

json_string = json.dumps(equipos, indent=4)

print(json_string)