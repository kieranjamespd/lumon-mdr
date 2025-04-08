// Updated number animation code for Lumon MDR
// This file contains the JavaScript code that should be copied into your application

// Function to update number animations based on mouse position
function updateNumbersAnimation(mouseX, mouseY) {
    const numbers = document.querySelectorAll('.number-cell');
    const grid = document.querySelector('.number-grid');
    const ACTIVATION_RADIUS = 200;
    
    numbers.forEach(num => {
        if (num.classList.contains('selected')) return;
        
        const rect = num.getBoundingClientRect();
        const numCenterX = rect.left + rect.width / 2;
        const numCenterY = rect.top + rect.height / 2;
        const distance = getDistance(mouseX, mouseY, numCenterX, numCenterY);
        
        if (distance < ACTIVATION_RADIUS) {
            const intensity = Math.pow(1 - (distance / ACTIVATION_RADIUS), 1.5);
            // Only apply the larger scale when dragging (isDragging is true)
            const scale = isDragging ? 1 + (intensity * 2.5) : 1;
            const blur = 5 + (intensity * 30);
            
            // Only apply transform if we're dragging, otherwise let CSS handle it
            if (isDragging) {
                num.style.setProperty('--scale', scale);
                num.style.transform = `scale(${scale})`;
            } else {
                // When not dragging, only apply text shadow
                num.style.textShadow = '0 0 ' + blur + 'px #39FFE1';
            }
            num.classList.add('active');
        } else {
            if (!num.classList.contains('selected')) {
                // Only reset transform if we were dragging
                if (isDragging) {
                    num.style.setProperty('--scale', 1);
                    num.style.transform = 'scale(1)';
                }
                num.style.textShadow = '0 0 5px #39FFE1';
                num.classList.remove('active');
            }
        }
    });

    const gridRect = grid.getBoundingClientRect();
    const gridCenterX = gridRect.left + gridRect.width / 2;
    const gridCenterY = gridRect.top + gridRect.height / 2;
    const distanceToCenter = getDistance(mouseX, mouseY, gridCenterX, gridCenterY);
    const maxDistance = gridRect.width / 2;
    
    if (distanceToCenter < maxDistance) {
        const expansionIntensity = Math.pow(1 - (distanceToCenter / maxDistance), 1.5);
        const gapSize = 8 + (expansionIntensity * 12);
        grid.style.gap = `${gapSize}px`;
    } else {
        grid.style.gap = '8px';
    }
}

// Helper function to calculate distance between two points
function getDistance(x1, y1, x2, y2) {
    return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
}

// CSS to add to your stylesheet
/*
.number-cell:hover {
    transform: scale(1.8);
    text-shadow: 0 0 10px var(--lumon-blue);
}
*/ 