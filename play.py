import os
import sys
import subprocess

def create_venv():
    print("🛠️  Creando entorno virtual...")
    subprocess.run([sys.executable, "-m", "venv", "venv"])
    print("✅ Entorno virtual creado.")

def install_requirements():
    print("📦 Instalando dependencias...")
    pip_executable = os.path.join("venv", "bin", "pip") if os.name != "nt" else os.path.join("venv", "Scripts", "pip.exe")
    subprocess.run([pip_executable, "install", "-r", "requirements.txt"])
    print("✅ Dependencias instaladas.")

def run_game():
    print("🚀 Iniciando el juego...")
    python_exec = os.path.join("venv", "bin", "python") if os.name != "nt" else os.path.join("venv", "Scripts", "python.exe")
    subprocess.run([python_exec, "-m", "src.main"])

def main():
    if not os.path.exists("venv"):
        create_venv()
        install_requirements()

    run_game()

if __name__ == "__main__":
    main()
