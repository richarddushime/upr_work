/* Simplified JavaScript for Thinkpro Tech Initiative Website */

// Update time display
function updateTime() {
    const now = new Date();
    const timeElement = document.getElementById('current-time');
    if (timeElement) {
        timeElement.textContent = now.toLocaleTimeString();
    }
}

// Initialize time display
updateTime();
setInterval(updateTime, 1000);

// Form validation
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const name = form.querySelector('#name').value;
            const email = form.querySelector('#email').value;
            const message = form.querySelector('#message').value;
            
            // Basic validation
            if (!name || name.trim().length < 2) {
                alert('Please enter a valid name (at least 2 characters)');
                return;
            }
            
            if (!email || !email.includes('@')) {
                alert('Please enter a valid email address');
                return;
            }
            
            if (!message || message.trim().length < 10) {
                alert('Please enter a message (at least 10 characters)');
                return;
            }
            
            // Success message
            alert('Thank you for your message! We will get back to you soon.');
            form.reset();
        });
    });
});

// Theme toggle
function createThemeToggle() {
    const toggle = document.createElement('button');
    toggle.innerHTML = '🌙';
    toggle.style.cssText = `
        position: fixed;
        top: 20px;
        left: 20px;
        background: rgba(255,255,255,0.2);
        border: none;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        font-size: 1.2rem;
        cursor: pointer;
        z-index: 1000;
    `;
    
    toggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-theme');
        toggle.innerHTML = document.body.classList.contains('dark-theme') ? '☀️' : '🌙';
    });
    
    document.body.appendChild(toggle);
}

// Initialize theme toggle
createThemeToggle();