// DOM yuklanganidan so'ng
document.addEventListener('DOMContentLoaded', function() {
    // Navbar scroll effekti
    const navbar = document.querySelector('nav');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('shadow-xl', 'py-3');
            navbar.classList.remove('py-4');
        } else {
            navbar.classList.remove('shadow-xl', 'py-3');
            navbar.classList.add('py-4');
        }
    });

    // Hover effektlari
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 10px 15px rgba(0, 0, 0, 0.1)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = '';
            this.style.boxShadow = '';
        });
    });

    // Yuklash animatsiyasi
    if (document.querySelector('.loader')) {
        setTimeout(function() {
            document.querySelector('.loader').style.display = 'none';
        }, 1000);
    }

    // Sahifa o'tish animatsiyasi
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Toast xabarlari
function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    toast.className = `fixed bottom-4 right-4 p-4 rounded-lg shadow-lg text-white animate__animated animate__fadeInUp ${
        type === 'success' ? 'bg-green-500' : 'bg-red-500'
    }`;
    toast.textContent = message;
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.classList.remove('animate__fadeInUp');
        toast.classList.add('animate__fadeOutDown');
        setTimeout(() => toast.remove(), 500);
    }, 3000);
}