/**
 * Enhanced Animations for the AI Tools Explorer
 * Provides smooth transitions and visual effects with a PlayStation/Netflix inspired feel
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS if it exists
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true,
            mirror: false
        });
    }
    
    // Initialize entrance animations
    initializeEntranceAnimations();
    
    // Initialize scroll effects
    initializeScrollEffects();
    
    // Initialize PlayStation-style hover effects
    initializeHoverEffects();
    
    // Initialize particle animation for hero section
    initializeParticleEffects();
    
    // Initialize marquee animation
    initializeMarquee();
});

/**
 * Setup entrance animations for elements as they appear on screen
 */
function initializeEntranceAnimations() {
    // Animate tool cards as they enter the viewport (fallback if AOS is not used)
    if (typeof AOS === 'undefined') {
        const toolCards = document.querySelectorAll('.tool-card');
        
        // Create intersection observer for fade-in animation
        const cardObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '0';
                    entry.target.style.transform = 'translateY(20px)';
                    
                    // Add animation with a delay based on card index
                    const delay = Array.from(toolCards).indexOf(entry.target) % 6 * 0.1;
                    entry.target.style.transition = `opacity 0.5s ease ${delay}s, transform 0.5s ease ${delay}s, box-shadow 0.3s ease, z-index 0s`;
                    
                    setTimeout(() => {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }, 50);
                    
                    // Stop observing after animation
                    cardObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1
        });
        
        // Observe each tool card
        toolCards.forEach(card => {
            card.style.opacity = '0';
            cardObserver.observe(card);
        });
        
        // Animate section titles as they enter the viewport
        const sectionTitles = document.querySelectorAll('.section-title');
        
        const titleObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '0';
                    entry.target.style.transform = 'translateX(-20px)';
                    
                    setTimeout(() => {
                        entry.target.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateX(0)';
                    }, 100);
                    
                    titleObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1
        });
        
        sectionTitles.forEach(title => {
            title.style.opacity = '0';
            titleObserver.observe(title);
        });
    }
    
    // Logo animation
    const logoIcon = document.querySelector('.logo-container i');
    if (logoIcon) {
        logoIcon.classList.add('animate-pulse');
    }
    
    // Hero badge animation
    const heroBadge = document.querySelector('.hero-badge');
    if (heroBadge) {
        heroBadge.classList.add('animate-bounce');
    }
}

/**
 * Setup scroll-based animations and effects
 */
function initializeScrollEffects() {
    // Parallax effect for hero section
    const heroSection = document.querySelector('.hero-section');
    
    if (heroSection) {
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            if (scrollY <= 500) {
                const yValue = scrollY * 0.4;
                heroSection.style.backgroundPosition = `50% ${yValue}px`;
                
                // Parallax for particles
                const particles = document.querySelectorAll('.particle');
                particles.forEach((particle, index) => {
                    const speed = 0.2 + (index * 0.1);
                    const yPos = scrollY * speed;
                    particle.style.transform = `translateY(${yPos}px)`;
                });
            }
        });
    }
    
    // Sticky category section headers with enhanced effect
    const categorySections = document.querySelectorAll('.category-section');
    
    if (categorySections.length > 0) {
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            
            categorySections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.offsetHeight;
                const sectionTitle = section.querySelector('.section-title');
                
                if (sectionTitle) {
                    if (scrollY >= sectionTop - 100 && scrollY <= sectionTop + sectionHeight - 100) {
                        sectionTitle.style.transform = 'translateY(0) scale(1.05)';
                        sectionTitle.style.color = '#FFFFFF';
                        sectionTitle.style.textShadow = '0 0 15px rgba(0, 112, 209, 0.5)';
                    } else {
                        sectionTitle.style.transform = '';
                        sectionTitle.style.color = '';
                        sectionTitle.style.textShadow = '';
                    }
                }
            });
        });
    }
    
    // Background glow parallax effect
    const bgGlows = document.querySelectorAll('.bg-glow-1, .bg-glow-2, .bg-glow-3');
    
    if (bgGlows.length > 0) {
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            
            bgGlows.forEach((glow, index) => {
                const speed = 0.05 * (index + 1);
                const yPos = scrollY * speed;
                glow.style.transform = `translateY(${yPos}px)`;
            });
        });
    }
}

/**
 * Setup PlayStation/Netflix-style hover animations
 */
function initializeHoverEffects() {
    // Navigation hover effect
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(link => {
        link.addEventListener('mouseenter', () => {
            link.style.transform = 'translateY(-2px)';
            link.style.textShadow = '0 0 8px rgba(52, 152, 219, 0.6)';
        });
        
        link.addEventListener('mouseleave', () => {
            link.style.transform = '';
            link.style.textShadow = '';
        });
    });
    
    // PlayStation-style button hover effects
    const buttons = document.querySelectorAll('.btn');
    
    buttons.forEach(button => {
        button.addEventListener('mouseenter', () => {
            button.style.transform = 'translateY(-3px) scale(1.03)';
            button.style.boxShadow = '0 7px 15px rgba(0, 0, 0, 0.3)';
        });
        
        button.addEventListener('mouseleave', () => {
            button.style.transform = '';
            button.style.boxShadow = '';
        });
        
        // PlayStation-style button press effect
        button.addEventListener('mousedown', () => {
            button.style.transform = 'translateY(1px) scale(0.98)';
            button.style.boxShadow = '0 2px 5px rgba(0, 0, 0, 0.2)';
        });
        
        button.addEventListener('mouseup', () => {
            button.style.transform = 'translateY(-3px) scale(1.03)';
            button.style.boxShadow = '0 7px 15px rgba(0, 0, 0, 0.3)';
        });
    });
    
    // Enhanced Netflix-style card focus effect
    const toolRows = document.querySelectorAll('.tools-row');
    
    toolRows.forEach(row => {
        row.addEventListener('mouseenter', () => {
            const otherRows = document.querySelectorAll('.tools-row:not(:hover)');
            otherRows.forEach(otherRow => {
                otherRow.style.opacity = '0.6';
                otherRow.style.transform = 'scale(0.98) translateY(5px)';
                otherRow.style.filter = 'blur(2px)';
            });
        });
        
        row.addEventListener('mouseleave', () => {
            const allRows = document.querySelectorAll('.tools-row');
            allRows.forEach(anyRow => {
                anyRow.style.opacity = '';
                anyRow.style.transform = '';
                anyRow.style.filter = '';
            });
        });
    });
    
    // Tool cards hover effect
    const toolCards = document.querySelectorAll('.tool-card');
    
    toolCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            const otherCards = card.parentNode.parentNode.querySelectorAll('.tool-card:not(:hover)');
            otherCards.forEach(otherCard => {
                otherCard.style.opacity = '0.7';
                otherCard.style.transform = 'scale(0.95)';
            });
        });
        
        card.addEventListener('mouseleave', () => {
            const allCards = card.parentNode.parentNode.querySelectorAll('.tool-card');
            allCards.forEach(anyCard => {
                anyCard.style.opacity = '';
                anyCard.style.transform = '';
            });
        });
    });
    
    // Quick nav items hover effect
    const quickNavItems = document.querySelectorAll('.quick-nav-item');
    
    quickNavItems.forEach(item => {
        item.addEventListener('mouseenter', () => {
            item.style.transform = 'translateY(-8px)';
            item.style.boxShadow = '0 10px 25px rgba(0, 0, 0, 0.3)';
            
            const icon = item.querySelector('.quick-nav-icon');
            if (icon) {
                icon.style.transform = 'scale(1.2)';
                icon.style.backgroundColor = 'var(--secondary-color)';
            }
        });
        
        item.addEventListener('mouseleave', () => {
            item.style.transform = '';
            item.style.boxShadow = '';
            
            const icon = item.querySelector('.quick-nav-icon');
            if (icon) {
                icon.style.transform = '';
                icon.style.backgroundColor = '';
            }
        });
    });
}

/**
 * Initialize particle effects for hero section
 */
function initializeParticleEffects() {
    const particles = document.querySelectorAll('.particle');
    
    particles.forEach((particle, index) => {
        // Random initial position adjustments
        const randomX = Math.random() * 5 - 2.5; // -2.5 to 2.5
        const randomY = Math.random() * 5 - 2.5; // -2.5 to 2.5
        
        // Apply custom animation
        particle.style.animation = `float ${15 + index * 3}s ease-in-out infinite`;
        particle.style.animationDelay = `${index * 0.5}s`;
        
        // Apply random position adjustment
        const currentTransform = window.getComputedStyle(particle).transform;
        if (currentTransform === 'none') {
            particle.style.transform = `translate(${randomX}px, ${randomY}px)`;
        } else {
            particle.style.transform = `${currentTransform} translate(${randomX}px, ${randomY}px)`;
        }
    });
}

/**
 * Initialize marquee animation for featured tools banner
 */
function initializeMarquee() {
    const marqueeContent = document.querySelectorAll('.marquee-content');
    
    marqueeContent.forEach(content => {
        // Clone the content to create seamless loop
        const clone = content.cloneNode(true);
        content.parentNode.appendChild(clone);
        
        // Add animation class
        content.classList.add('animate-marquee');
        clone.classList.add('animate-marquee');
        
        // Apply different animation speed to each
        const speed = 30 + Math.random() * 10;
        content.style.animationDuration = `${speed}s`;
        clone.style.animationDuration = `${speed}s`;
    });
}
