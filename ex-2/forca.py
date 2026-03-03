import random

class JogoForca:
    def __init__(self, palavra):
        self.palavra = palavra.upper()
        self._letras_tentadas = []
        self._tentativas = 6

    def mostrar_palavra(self):
        visual = []
        for letra in self.palavra:
            if letra in self._letras_tentadas:
                visual.append(letra)
            else:
                visual.append("_")
        return " ".join(visual)

    def chutar(self, chute):
        chute = chute.strip().upper()
        if not chute or len(chute) != 1:
            print("Por favor, digite apenas uma letra.")
            return

        if chute in self._letras_tentadas:
            print(f"Você já tentou a letra {chute}!")
            return

        self._letras_tentadas.append(chute)

        if chute in self.palavra:
            print(f"Boa! A letra {chute} está na palavra.")
        else:
            self._tentativas -= 1
            print(f"Puxa, a letra {chute} não está na palavra. Tentativas restantes: {self._tentativas}")

    @property
    def venceu(self):
        return "_" not in self.mostrar_palavra()

    @property
    def perdeu(self):
        return self._tentativas <= 0

    def status(self):
        print("\n" + "=" * 30)
        print(f"Palavra: {self.mostrar_palavra()}")
        print(f"Tentativas restantes: {self._tentativas}")
        print(f"Letras já tentadas: {', '.join(self._letras_tentadas)}")
        print("=" * 30)

def jogar():
    print("*" * 30)
    print("BEM-VINDO AO JOGO DA FORCA!")
    print("*" * 30)

    palavras = ["PYTHON", "PROGRAMACAO", "ALURA", "COMPUTADOR", "SOFTWARE", "DESENVOLVEDOR"]
    palavra_secreta = random.choice(palavras)
    
    jogo = JogoForca(palavra_secreta)

    while not jogo.venceu and not jogo.perdeu:
        jogo.status()
        chute = input("Qual letra? ")
        jogo.chutar(chute)

    if jogo.venceu:
        print(f"\nParabéns, você ganhou! 🏆 A palavra era: {jogo.palavra}")
    else:
        print(f"\nGame Over! A palavra era {jogo.palavra}. 💀")

if __name__ == "__main__":
    jogar()

