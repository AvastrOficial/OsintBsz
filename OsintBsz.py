import requests
import time
import sys

def tricolor_text(message):
    colors = [
        '\033[91m',  # rojo fuerte
        '\033[93m',  # amarillo
        '\033[92m'   # verde
    ]
    delay = 0.1
    for color in colors:
        sys.stdout.write(f"{color}{message}\033[0m\r")
        sys.stdout.flush()
        time.sleep(delay)

# Tu clave de API proporcionada por Hunter.io
api_key = '66137bf0d4a554cbc322a18d035b87143c6fffad'

def domain_search(domain):
    url = f'https://api.hunter.io/v2/domain-search?domain={domain}&api_key={api_key}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f"Resultados para búsqueda de dominio '{domain}':")
        print(data)
    else:
        print(f"Error en la búsqueda de dominio: {data.get('error')}")

def email_finder(domain, first_name, last_name):
    url = f'https://api.hunter.io/v2/email-finder?domain={domain}&first_name={first_name}&last_name={last_name}&api_key={api_key}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f"Resultados para búsqueda de email con nombre '{first_name} {last_name}' en '{domain}':")
        print(data)
    else:
        print(f"Error en la búsqueda de email: {data.get('error')}")

def verificar_correo_electronico(email):
    url = f'https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        if data['data']['result'] == 'deliverable':
            print("Buscando en otros servicios... ")
            tricolor_text("Cargando... ")

            # Simulación de carga con colores tricolores
            colors = [
                '\033[91m',  # rojo
                '\033[93m',  # amarillo
                '\033[92m',  # verde
            ]
            for i in range(10):
                color = colors[i % len(colors)]
                sys.stdout.write(f"{color}=")
                sys.stdout.flush()
                time.sleep(0.3)

            print(" 100%")
            print("\n")  # Nueva línea para separar la carga del siguiente mensaje

            # Ejemplo de consultas a APIs reales
            social_media_sites = [
                {'name': 'Twitter', 'url': f'https://api.twitter.com/2/users/by/username/{email}'},
                {'name': 'Facebook', 'url': f'https://graph.facebook.com/v13.0/{email}'},
                {'name': 'LinkedIn', 'url': f'https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))&email={email}'},
                {'name': 'Instagram', 'url': f'https://graph.instagram.com/{email}'},
                {'name': 'Snapchat', 'url': f'https://api.snapchat.com/v1/users/{email}'},
                {'name': 'Pinterest', 'url': f'https://api.pinterest.com/v1/users/{email}'},
                {'name': 'Reddit', 'url': f'https://www.reddit.com/user/{email}'},
                {'name': 'TikTok', 'url': f'https://api.tiktok.com/v1/users/{email}'},     
                {'name': 'GitHub', 'url': f'https://api.github.com/users/{email}'},
                {'name': 'Medium', 'url': f'https://api.medium.com/v1/users/{email}'},
                {'name': 'Quora', 'url': f'https://api.quora.com/api/user/{email}'},
                {'name': 'SoundCloud', 'url': f'https://api.soundcloud.com/users/{email}'},
                {'name': 'Spotify', 'url': f'https://api.spotify.com/v1/users/{email}'},
                {'name': 'Vimeo', 'url': f'https://api.vimeo.com/users/{email}'},        
                {'name': 'WeChat', 'url': f'https://api.wechat.com/v1/users/{email}'},
                {'name': 'Skype', 'url': f'https://api.skype.com/v2/users/{email}'},
                {'name': 'Xbox Live', 'url': f'https://xblapi.com/v2/accounts/{email}'},
                {'name': 'Discord', 'url': f'https://discord.com/api/users/{email}'},
                {'name': 'Twitch', 'url': f'https://api.twitch.tv/helix/users?login={email}'}
            ]

            for site in social_media_sites:
                response = requests.get(site['url'])
                if response.status_code == 200:
                    print(f"Resultados de {site['name']} para el correo electrónico {email}:")
                    print(response.json())
                else:
                    print(f"\033[38;5;196mError en la búsqueda de {site['name']}: {response.status_code}. \033[92mCuenta no registrada.\033[0m")
        else:
            print("El correo electrónico no es válido o no es entregable.")
    else:
        print(f"Error al verificar el correo electrónico: {data.get('error')}")

# Función para imprimir el banner del programa
def print_menu_banner():
    banner = """
    \033[38;5;196m
  ___      _       _   ____          
 / _ \ ___(_)_ __ | |_| __ ) ___ ____
| | | / __| | '_ \| __|  _ \/ __|_  /
| |_| \__ \ | | | | |_| |_) \__ \/ / 
 \___/|___/_|_| |_|\__|____/|___/___|

BY @AvaStrOficial / Version : 0.0.1

 ╭────────༺୨ ✧ Elija una opcion ✧ ୧༻────────╮

1. Buscar dominio
2. Buscar email
3. Verificar email
4. Mostrar redes sociales

╰─────────  ʚ✧ OSINTBSZ  CORREO ✧ɞ  ─────────╯
\033[0m
"""
    print(banner)

def mostrar_redes_sociales():
    redes_sociales = """
    \033[38;5;196m
    ╭────────༺୨  ✧ Redes Sociales ✧   ୧༻────────╮
     
    - Telegram: https://t.me/+sOf-gqn6SClmNDcx

    - GitHub: https://github.com/AvastrOficial

    ╰─────────  ʚ✧ OSINTBSZ  CORREO ✧ɞ  ─────────╯
    \033[0m
"""
    print(redes_sociales)

# Ejecución del programa con input de usuario
def main():
    while True:
        print_menu_banner()
        opcion = int(input("Ingrese el número de opción: "))

        if opcion == 1:
            domain = input("Ingrese el dominio a buscar: ")
            domain_search(domain)
        elif opcion == 2:
            domain = input("Ingrese el dominio: ")
            first_name = input("Ingrese el primer nombre: ")
            last_name = input("Ingrese el apellido: ")
            email_finder(domain, first_name, last_name)
        elif opcion == 3:
            email = input("Ingrese el correo electrónico a verificar: ")
            verificar_correo_electronico(email)
        elif opcion == 4:
            mostrar_redes_sociales()
        else:
            print("Opción no válida")

        # Preguntar si el usuario quiere realizar otra acción
        otra_accion = input("¿Desea realizar otra acción? (s/n): ").strip().lower()
        if otra_accion != 's':
            break

if __name__ == "__main__":
    main()
