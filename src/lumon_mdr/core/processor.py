from typing import List, Dict, Tuple
import numpy as np
from dataclasses import dataclass
from enum import Enum

class NumberCategory(Enum):
    SCARY = "scary"
    HAPPY = "happy"
    SAD = "sad"
    ANGRY = "angry"

@dataclass
class ProcessedNumber:
    value: float
    category: NumberCategory
    confidence: float

class DataProcessor:
    def __init__(self):
        self.processed_count = 0
        self.total_count = 0
        
    def process_numbers(self, numbers: List[float]) -> List[ProcessedNumber]:
        """Process a list of numbers according to Lumon's refinement criteria."""
        self.total_count = len(numbers)
        processed = []
        
        for num in numbers:
            # Implement basic number categorization
            # This is a placeholder algorithm - we'll make it more sophisticated
            if num < 0:
                category = NumberCategory.SCARY
            elif 0 <= num < 50:
                category = NumberCategory.SAD
            elif 50 <= num < 75:
                category = NumberCategory.ANGRY
            else:
                category = NumberCategory.HAPPY
                
            # Calculate confidence (placeholder)
            confidence = np.random.uniform(0.75, 1.0)
            
            processed.append(ProcessedNumber(
                value=num,
                category=category,
                confidence=confidence
            ))
            
            self.processed_count += 1
            
        return processed
    
    def get_progress(self) -> float:
        """Return processing progress as a percentage."""
        if self.total_count == 0:
            return 0.0
        return (self.processed_count / self.total_count) * 100
    
    def parse_input(self, text: str) -> List[float]:
        """Parse comma-separated number input."""
        try:
            numbers = [float(n.strip()) for n in text.split(',') if n.strip()]
            return numbers
        except ValueError:
            raise ValueError("Invalid number format. Please enter comma-separated numbers.") 