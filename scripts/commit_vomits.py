import subprocess
import datetime
import random

class VomitCommitter:
    def __init__(self):
        self.commit_prefixes = ["🌀", "🤖", "💊", "🧠", "👁️", "🌌", "💉", "🔮"]
        self.commit_states = [
            "DELIRIO_DIGITAL",
            "PSICOSIS_BINARIA",
            "FRAGMENTACIÓN_MENTAL",
            "COLAPSO_NEURAL"
        ]
    
    def _get_random_prefix(self) -> str:
        return random.choice(self.commit_prefixes)
    
    def _get_random_state(self) -> str:
        return random.choice(self.commit_states)
    
    def commit_and_push(self, message: str = None):
        """Hace commit y push de los cambios con un mensaje psycho"""
        try:
            # Agregar cambios
            subprocess.run(["git", "add", "."], check=True)
            
            # Generar mensaje si no se proporciona uno
            if not message:
                prefix = self._get_random_prefix()
                state = self._get_random_state()
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
                message = f"{prefix} Vomitiva {timestamp} - Estado: {state}"
            
            # Hacer commit
            subprocess.run(["git", "commit", "-m", message], check=True)
            
            # Push
            subprocess.run(["git", "push", "origin", "main"], check=True)
            
            print(f"🌀 Vomitiva commiteada y pusheada: {message}")
            
        except subprocess.CalledProcessError as e:
            print(f"💀 Error en el proceso: {str(e)}")
            raise

if __name__ == "__main__":
    committer = VomitCommitter()
    committer.commit_and_push() 