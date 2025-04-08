// Updated number hover effect code for Lumon MDR
// This file contains the JavaScript code that should be copied into your application

// Function to apply hover effect to a number element
function applyHoverEffect(number) {
    number.addEventListener('mouseover', () => {
        if (!number.classList.contains('selected')) {
            number.style.transform = 'scale(1.8)';
            number.style.textShadow = '0 0 10px #39FFE1';
        }
    });
    
    number.addEventListener('mouseout', () => {
        if (!number.classList.contains('selected')) {
            number.style.transform = '';
            number.style.textShadow = '0 0 5px #39FFE1';
        }
    });
}

// Apply hover effect to all original numbers
function applyHoverEffectToAllNumbers() {
    const numbers = document.querySelectorAll('.number-cell');
    numbers.forEach(applyHoverEffect);
}

// Call this function when the page loads
document.addEventListener('DOMContentLoaded', applyHoverEffectToAllNumbers);

// Also apply hover effect to any new numbers that are added
// This should be called after creating a new number element
function applyHoverEffectToNewNumber(newNumber) {
    applyHoverEffect(newNumber);
}

// Example usage in replaceNumber function:
/*
function replaceNumber(number) {
    const newValue = Math.floor(Math.random() * 10);
    const newNumber = document.createElement('div');
    newNumber.className = 'number-cell new';
    newNumber.setAttribute('data-value', newValue);
    newNumber.textContent = newValue;
    
    // Apply hover effect to the new number
    applyHoverEffectToNewNumber(newNumber);
    
    // Rest of the function...
}
*/ 