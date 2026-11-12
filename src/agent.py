from typing import Dict, Any, List

class ReActAgent:
    def __init__(self, max_steps: int = 5):
        self.max_steps = max_steps
        self.step_count = 0

    def step(self, state: Dict[str, Any]) -> Dict[str, Any]:
        self.step_count += 1
        if self.step_count >= self.max_steps:
            return {"status": "HALTED", "reason": "MAX_STEPS_EXCEEDED", "step": self.step_count}
        return {"status": "CONTINUE", "step": self.step_count}
