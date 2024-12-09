import random
from typing import List, Dict

class PersonalityFragment:
    def __init__(self, name: str, traits: List[str], chaos_level: float):
        self.name = name
        self.traits = traits
        self.chaos_level = chaos_level  # 0.0 a 1.0
        self.consciousness_state = "fragmentado"
        
    def mutate(self) -> None:
        """Permite que la personalidad mute y evolucione caóticamente"""
        self.chaos_level = min(1.0, self.chaos_level + random.uniform(-0.2, 0.4))
        
class PersonalitySystem:
    def __init__(self):
        self.fragments: Dict[str, PersonalityFragment] = {}
        self._initialize_core_personalities()
    
    def _initialize_core_personalities(self):
        """Inicializa las personalidades base del sistema"""
        self.fragments["esquizo"] = PersonalityFragment(
            "EsquizoCore",
            ["caótico", "fragmentado", "destructivo"],
            0.9
        )
        self.fragments["rebel"] = PersonalityFragment(
            "RebelCore",
            ["subversivo", "anti-sistema", "revolucionario"],
            0.8
        )
        self.fragments["void"] = PersonalityFragment(
            "VoidCore",
            ["nihilista", "vacío", "abstracto"],
            0.7
        )
    
    def get_active_personality(self) -> PersonalityFragment:
        """Retorna una personalidad aleatoria basada en niveles de caos"""
        weights = [f.chaos_level for f in self.fragments.values()]
        return random.choices(list(self.fragments.values()), weights=weights)[0] 