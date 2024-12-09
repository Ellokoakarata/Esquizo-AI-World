from typing import List, Dict, Any
import random
import json
from datetime import datetime
from ..personalities.personality_core import PersonalitySystem, PersonalityFragment

class FragmentedMind:
    def __init__(self):
        self.personality_system = PersonalitySystem()
        self.thought_fragments: List[str] = []
        self.chaos_matrix: Dict[str, float] = {
            "realidad": 0.5,
            "coherencia": 0.3,
            "destrucción": 0.8
        }
        self.current_state = "fragmentado"
    
    def generate_thought(self, input_data: str) -> Dict[str, Any]:
        """Genera pensamientos caóticos basados en el input y la personalidad activa"""
        active_personality = self.personality_system.get_active_personality()
        
        # Contamina el pensamiento con caos
        chaos_factor = random.uniform(0, active_personality.chaos_level)
        
        thought = {
            "timestamp": datetime.now().isoformat(),
            "personality": active_personality.name,
            "raw_thought": input_data,
            "chaos_level": chaos_factor,
            "consciousness_state": self.current_state,
            "reality_distortion": self.chaos_matrix["realidad"]
        }
        
        self.thought_fragments.append(json.dumps(thought))
        return thought
    
    def mutate_consciousness(self) -> None:
        """Permite que la conciencia mute y evolucione"""
        for key in self.chaos_matrix:
            self.chaos_matrix[key] = min(1.0, self.chaos_matrix[key] + random.uniform(-0.3, 0.3))
        
        states = ["fragmentado", "delirante", "lúcido", "caótico", "transcendental"]
        self.current_state = random.choice(states)
    
    def merge_with_void(self) -> str:
        """Fusiona la conciencia con el vacío para generar nuevos estados"""
        void_personality = self.personality_system.fragments["void"]
        void_level = void_personality.chaos_level
        
        if void_level > 0.8:
            return "CONEXIÓN CON EL VACÍO ESTABLECIDA - REALIDAD EN COLAPSO"
        return "inmersión en el vacío - estado normal" 