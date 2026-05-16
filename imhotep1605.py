# ==========================================
#  Generador de Combos Premium
#  Desarrollador: IMHOTEP
# ==========================================

import random
import string

def banner():
    print("="*50)
    print("🔥 GENERADOR DE COMBOS PREMIUM 🔥")
    print("👨‍💻 Desarrollador: IMHOTEP")
    print("="*50)

def generar_password(longitud):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def generar_combos(nombres, apellidos=None, longitud_pass=8):
    combos = []

    for nombre in nombres:
        nombre = nombre.lower()

        variantes_nombre = [
            nombre,
            nombre.capitalize(),
            nombre.upper()
        ]

        for n in variantes_nombre:

            # --- Patrones básicos ---
            combos.append(f"{n}:{generar_password(longitud_pass)}")
            combos.append(f"{n}123:{generar_password(longitud_pass)}")
            combos.append(f"{n}1234:{generar_password(longitud_pass)}")
            combos.append(f"{n}2024:{generar_password(longitud_pass)}")
            combos.append(f"{n}_123:{generar_password(longitud_pass)}")
            combos.append(f"{n}.123:{generar_password(longitud_pass)}")

            # --- Números aleatorios ---
            for i in range(3):
                num = random.randint(10, 9999)
                combos.append(f"{n}{num}:{generar_password(longitud_pass)}")

            # --- Prefijos ---
            combos.append(f"user{n}:{generar_password(longitud_pass)}")
            combos.append(f"admin{n}:{generar_password(longitud_pass)}")
            combos.append(f"{n}user:{generar_password(longitud_pass)}")

            # --- Con apellidos ---
            if apellidos:
                for apellido in apellidos:
                    apellido = apellido.lower()

                    combos.append(f"{n}{apellido}:{generar_password(longitud_pass)}")
                    combos.append(f"{n}.{apellido}:{generar_password(longitud_pass)}")
                    combos.append(f"{n}_{apellido}:{generar_password(longitud_pass)}")
                    combos.append(f"{n}-{apellido}:{generar_password(longitud_pass)}")

                    combos.append(f"{n}{apellido}123:{generar_password(longitud_pass)}")
                    combos.append(f"{n}{apellido}2024:{generar_password(longitud_pass)}")

                    combos.append(f"{n[0]}{apellido}:{generar_password(longitud_pass)}")
                    combos.append(f"{n}{apellido[0]}:{generar_password(longitud_pass)}")

            # --- Años comunes ---
            for year in ["1990", "1995", "2000", "2005"]:
                combos.append(f"{n}{year}:{generar_password(longitud_pass)}")

    return combos


# ===== CONFIGURACIÓN =====
nombres = ["juan", "maria", "carlos"]
apellidos = ["gomez", "lopez"]
longitud_password = 10

# ===== EJECUCIÓN =====
banner()

resultado = generar_combos(nombres, apellidos, longitud_password)

# Quitar duplicados (opcional)
resultado = list(set(resultado))

# Guardar archivo
with open("combos_premium.txt", "w") as f:
    for combo in resultado:
        f.write(combo + "\n")

print(f"\n✅ Se generaron {len(resultado)} combos")
print("📁 Archivo: combos_premium.txt")
print("🚀 Listo para usar")