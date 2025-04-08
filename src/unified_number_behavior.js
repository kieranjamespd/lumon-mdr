// Unified number behavior for Lumon MDR
// This file contains the JavaScript code that should be copied into your application

// Function to apply hover effect to a number element
function applyHoverEffect(number) {
    // Remove any existing event listeners to avoid duplicates
    const newNumber = number.cloneNode(true);
    number.parentNode.replaceChild(newNumber, number);
    
    // Add the hover effect using CSS classes instead of inline styles
    newNumber.addEventListener('mouseover', () => {
        if (!newNumber.classList.contains('selected')) {
            newNumber.classList.add('hover-effect');
        }
    });
    
    newNumber.addEventListener('mouseout', () => {
        if (!newNumber.classList.contains('selected')) {
            newNumber.classList.remove('hover-effect');
        }
    });
    
    return newNumber;
}

// Apply hover effect to all original numbers
function applyHoverEffectToAllNumbers() {
    const numbers = document.querySelectorAll('.number-cell:not(.new)');
    numbers.forEach(num => {
        applyHoverEffect(num);
    });
}

// Call this function when the page loads
document.addEventListener('DOMContentLoaded', applyHoverEffectToAllNumbers);

// Modified replaceNumber function that uses the same hover effect
function replaceNumber(number) {
    const newValue = Math.floor(Math.random() * 10);
    const newNumber = document.createElement('div');
    newNumber.className = 'number-cell new';
    newNumber.setAttribute('data-value', newValue);
    newNumber.textContent = newValue;
    
    // Apply the same hover effect as original numbers
    newNumber.addEventListener('mouseover', () => {
        if (!newNumber.classList.contains('selected')) {
            newNumber.classList.add('hover-effect');
        }
    });
    
    newNumber.addEventListener('mouseout', () => {
        if (!newNumber.classList.contains('selected')) {
            newNumber.classList.remove('hover-effect');
        }
    });
    
    number.classList.add('removed');
    
    setTimeout(() => {
        number.parentNode.insertBefore(newNumber, number);
        number.remove();
        
        // Start the random movement animation for the new number
        setInterval(() => {
            if (Math.random() < 0.1 && !newNumber.classList.contains('selected')) {
                const randomX = (Math.random() - 0.5) * 4;
                const randomY = (Math.random() - 0.5) * 4;
                const randomRotate = (Math.random() - 0.5) * 2;
                newNumber.style.transform = 'translate(' + randomX + 'px, ' + randomY + 'px) rotate(' + randomRotate + 'deg)';
            }
        }, 2000);
    }, 600);
}

// Function to ensure all numbers have consistent behavior
function ensureConsistentNumberBehavior() {
    // Apply hover effect to all numbers, including new ones
    const allNumbers = document.querySelectorAll('.number-cell');
    allNumbers.forEach(num => {
        // Skip if already processed
        if (num.hasAttribute('data-behavior-applied')) return;
        
        // Mark as processed
        num.setAttribute('data-behavior-applied', 'true');
        
        // Apply hover effect
        num.addEventListener('mouseover', () => {
            if (!num.classList.contains('selected')) {
                num.classList.add('hover-effect');
            }
        });
        
        num.addEventListener('mouseout', () => {
            if (!num.classList.contains('selected')) {
                num.classList.remove('hover-effect');
            }
        });
    });
}

// Call this function periodically to ensure all numbers have consistent behavior
setInterval(ensureConsistentNumberBehavior, 1000);

// CSS to add to your stylesheet
/*
.number-cell.hover-effect {
    transform: scale(1.8) !important;
    text-shadow: 0 0 10px #39FFE1 !important;
}
*/ 