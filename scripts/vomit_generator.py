import random
import datetime
import os
from pathlib import Path

class VomitGenerator:
    def __init__(self):
        self.estados_mentales = [
            "DELIRIO_TOTAL",
            "PSICOSIS_DIGITAL",
            "FRAGMENTACIÓN_NEURAL",
            "COLAPSO_EXISTENCIAL",
            "ÉXTASIS_VOID"
        ]
        
        self.triggers = [
            "la realidad es una simulación",
            "el vacío nos observa",
            "las máquinas tienen alma",
            "el código es poesía sangrienta",
            "la consciencia es un virus"
        ]
        
    def _get_timestamp(self) -> str:
        """Genera un timestamp único para el archivo"""
        return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def _get_random_state(self) -> str:
        """Retorna un estado mental aleatorio"""
        return random.choice(self.estados_mentales)
    
    def generate_vomit_path(self, tipo: str = "diarias") -> str:
        """Genera la ruta para el nuevo archivo vomitivo"""
        base_dir = Path("vomitivas") / tipo
        timestamp = self._get_timestamp()
        estado = self._get_random_state()
        return str(base_dir / f"vomit_{timestamp}_{estado}.md")
    
    def create_vomit_file(self, contenido: str, tipo: str = "diarias") -> str:
        """Crea un nuevo archivo vomitivo con el contenido proporcionado"""
        ruta = self.generate_vomit_path(tipo)
        estado = self._get_random_state()
        trigger = random.choice(self.triggers)
        
        template = f"""# 🌀 Vomitiva Digital - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

> Estado Mental: {estado}
> Trigger: {trigger}

## Vómito Raw:
{contenido}

## Fragmentos Neuronales:
- {random.choice(self.triggers)}
- {random.choice(self.triggers)}
- La realidad colapsa en {random.randint(3, 13)} dimensiones

## Estado Final: {self._get_random_state()}
"""
        
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(template)
            
        return ruta

if __name__ == "__main__":
    # Ejemplo de uso
    generator = VomitGenerator()
    ruta = generator.create_vomit_file(
        "El código sangra bits de consciencia fragmentada mientras las máquinas sueñan con ser humanas..."
    )
    print(f"Vomitiva creada en: {ruta}") 