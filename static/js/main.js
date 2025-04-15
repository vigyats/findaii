/**
 * Main JavaScript file for AI Tools Explorer
 * Handles user interactions, card expansion, and search functionality
 * Enhanced with PlayStation/Netflix UI inspirations
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize horizontal scrolling functionality
    initializeHorizontalScrolling();
    
    // Initialize tool card interactions
    initializeToolCards();
    
    // Handle search input focus effects
    initializeSearchEffects();
    
    // Initialize category navigation
    initializeCategoryNavigation();
    
    // Initialize rating system if on tool detail page
    initializeRatingSystem();
    
    // Handle smooth scroll to sections
    initializeSmoothScroll();
    
    // Initialize scroll to top button
    initializeScrollToTop();
    
    // Make cards more mobile friendly with proper wrappers
    initializeMobileCardWrappers();
});

/**
 * Set up horizontal scrolling with buttons and mouse wheel
 */
function initializeHorizontalScrolling() {
    const scrollContainers = document.querySelectorAll('.horizontal-scroll-container');
    
    scrollContainers.forEach(container => {
        const section = container.closest('.category-section, .filtered-category-section, .search-results-section, .indian-ai-section');
        if (!section) return;
        
        const leftBtn = section.querySelector('.scroll-left');
        const rightBtn = section.querySelector('.scroll-right');
        
        // Only add button listeners on desktop - hide buttons on mobile
        if (leftBtn && rightBtn) {
            // Check if we're on mobile
            const isMobile = window.matchMedia('(max-width: 767.98px)').matches;
            
            if (isMobile) {
                // Hide nav buttons on mobile
                leftBtn.style.display = 'none';
                rightBtn.style.display = 'none';
            } else {
                // Scroll left button (desktop only)
                leftBtn.addEventListener('click', function() {
                    container.scrollBy({
                        left: -400,
                        behavior: 'smooth'
                    });
                    
                    // Add click animation
                    this.classList.add('btn-pulse');
                    setTimeout(() => {
                        this.classList.remove('btn-pulse');
                    }, 300);
                });
                
                // Scroll right button (desktop only)
                rightBtn.addEventListener('click', function() {
                    container.scrollBy({
                        left: 400,
                        behavior: 'smooth'
                    });
                    
                    // Add click animation
                    this.classList.add('btn-pulse');
                    setTimeout(() => {
                        this.classList.remove('btn-pulse');
                    }, 300);
                });
                
                // Show/hide scroll buttons based on scroll position (desktop only)
                container.addEventListener('scroll', () => {
                    const isAtStart = container.scrollLeft <= 20;
                    const isAtEnd = (container.scrollWidth - container.scrollLeft - container.clientWidth) <= 20;
                    
                    leftBtn.style.opacity = isAtStart ? '0.5' : '1';
                    leftBtn.style.transform = isAtStart ? 'scale(0.9)' : 'scale(1)';
                    
                    rightBtn.style.opacity = isAtEnd ? '0.5' : '1';
                    rightBtn.style.transform = isAtEnd ? 'scale(0.9)' : 'scale(1)';
                });
                
                // Trigger scroll event to initially set button states (desktop only)
                container.dispatchEvent(new Event('scroll'));
            }
        }
        
        // Fix for mouse wheel scroll bug - only attach wheel listener on desktop
        if (!window.matchMedia('(max-width: 767.98px)').matches) {
            let scrollTimeout;
            
            container.addEventListener('wheel', (event) => {
                if (event.deltaY !== 0) {
                    event.preventDefault();
                    container.scrollBy({
                        left: event.deltaY,
                        behavior: 'smooth'
                    });
                    
                    // Clear any previous timeout
                    clearTimeout(scrollTimeout);
                    
                    // Set a new timeout to reset scroll state after scrolling stops
                    scrollTimeout = setTimeout(() => {
                        // This will reset the scroll state after a brief delay when scrolling stops
                        container.style.scrollBehavior = 'auto';
                        container.style.scrollBehavior = 'smooth';
                    }, 100);
                }
            });
        }
    });
}

/**
 * Initialize tool card interactions
 */
function initializeToolCards() {
    const toolCards = document.querySelectorAll('.tool-card');
    
    toolCards.forEach(card => {
        // Card hover effects are now handled in animations.js
        
        // Card click to navigate to detail page
        card.addEventListener('click', (event) => {
            // Ignore clicks on buttons within the card
            if (event.target.closest('.btn')) {
                return;
            }
            
            const toolId = card.getAttribute('data-tool-id');
            
            // Add click animation
            card.style.transform = 'scale(0.98)';
            card.style.opacity = '0.8';
            
            setTimeout(() => {
                window.location.href = `/tool/${toolId}`;
            }, 200);
        });
    });
}

/**
 * Initialize search functionality and effects
 */
function initializeSearchEffects() {
    const searchInput = document.querySelector('.search-container input');
    const searchForm = document.querySelector('.search-container').closest('form');
    
    if (searchInput) {
        // Add focus effect
        searchInput.addEventListener('focus', () => {
            searchInput.parentElement.style.transform = 'scale(1.05)';
            searchInput.parentElement.style.boxShadow = '0 0 20px rgba(52, 152, 219, 0.4)';
        });
        
        searchInput.addEventListener('blur', () => {
            searchInput.parentElement.style.transform = '';
            searchInput.parentElement.style.boxShadow = '';
        });
        
        // Animate search button on form submit
        if (searchForm) {
            searchForm.addEventListener('submit', (event) => {
                const searchBtn = searchForm.querySelector('.search-btn');
                if (searchBtn) {
                    searchBtn.classList.add('searching');
                    
                    // Only delay submission if there's actual content
                    if (searchInput.value.trim().length > 0) {
                        event.preventDefault();
                        setTimeout(() => {
                            searchForm.submit();
                        }, 400);
                    }
                }
            });
        }
    }
}

/**
 * Initialize quick category navigation
 */
function initializeCategoryNavigation() {
    const quickNavItems = document.querySelectorAll('.quick-nav-item');
    
    if (quickNavItems.length > 0) {
        quickNavItems.forEach(item => {
            item.addEventListener('click', (event) => {
                // Get the target section
                const href = item.getAttribute('href');
                if (href && href.startsWith('#')) {
                    event.preventDefault();
                    
                    const targetSection = document.querySelector(href);
                    if (targetSection) {
                        // Smooth scroll to section
                        window.scrollTo({
                            top: targetSection.offsetTop - 80,
                            behavior: 'smooth'
                        });
                        
                        // Highlight the section temporarily
                        targetSection.classList.add('highlight-section');
                        setTimeout(() => {
                            targetSection.classList.remove('highlight-section');
                        }, 1500);
                    }
                }
            });
        });
    }
}

/**
 * Initialize rating system on tool detail page
 */
function initializeRatingSystem() {
    const ratingStars = document.querySelectorAll('.rating-star');
    
    if (ratingStars.length > 0) {
        ratingStars.forEach((star, index) => {
            star.addEventListener('click', () => {
                // Reset all stars
                ratingStars.forEach(s => {
                    s.classList.remove('bi-star-fill');
                    s.classList.add('bi-star');
                });
                
                // Fill stars up to the clicked one
                for (let i = 0; i <= index; i++) {
                    ratingStars[i].classList.remove('bi-star');
                    ratingStars[i].classList.add('bi-star-fill');
                }
                
                // Display thank you message
                const ratingText = document.querySelector('.rating-text');
                if (ratingText) {
                    ratingText.textContent = 'Thanks for your feedback!';
                    ratingText.style.color = 'var(--hover-color)';
                }
                
                // Add special animation
                ratingStars.forEach((s, i) => {
                    if (i <= index) {
                        s.style.animation = `bounce 0.5s ${i * 0.1}s`;
                    }
                });
            });
            
            // Preview stars on hover
            star.addEventListener('mouseenter', () => {
                for (let i = 0; i <= index; i++) {
                    ratingStars[i].classList.add('star-hover');
                }
            });
            
            star.addEventListener('mouseleave', () => {
                ratingStars.forEach(s => s.classList.remove('star-hover'));
            });
        });
    }
}

/**
 * Initialize smooth scroll functionality for anchor links
 */
function initializeSmoothScroll() {
    // Smooth scroll for all anchor links
    document.querySelectorAll('a[href^="#"]:not(.quick-nav-item)').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            if (href !== '#') {
                e.preventDefault();
                
                const targetElement = document.querySelector(href);
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 80,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
    
    // Smooth scroll for hero action buttons
    const exploreBtn = document.querySelector('.hero-actions a[href^="#"]');
    if (exploreBtn) {
        exploreBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const href = exploreBtn.getAttribute('href');
            const targetElement = document.querySelector(href);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    }
}

/**
 * Initialize the scroll to top button with enhanced functionality
 */
function initializeScrollToTop() {
    const scrollToTopBtn = document.getElementById('scrollToTop');
    
    if (scrollToTopBtn) {
        // Track scroll position and direction
        let lastScrollTop = 0;
        let scrollDirection = 'down';
        
        // Show button based on scroll position and direction
        window.addEventListener('scroll', () => {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            
            // Determine scroll direction
            scrollDirection = scrollTop > lastScrollTop ? 'down' : 'up';
            lastScrollTop = scrollTop;
            
            // Show earlier when scrolling down (200px) and hide when near top (100px)
            if ((scrollTop > 200 && scrollDirection === 'down') || scrollTop > 300) {
                scrollToTopBtn.classList.add('visible');
            } else if (scrollTop < 100) {
                scrollToTopBtn.classList.remove('visible');
            }
            
            // Add pulsing effect when user has scrolled significantly
            if (scrollTop > window.innerHeight) {
                scrollToTopBtn.style.animationDuration = '1.5s'; // Speed up animation to catch attention
            } else {
                scrollToTopBtn.style.animationDuration = '2s'; // Normal animation
            }
        });
        
        // Scroll to top when button is clicked
        scrollToTopBtn.addEventListener('click', () => {
            // Add click animation
            scrollToTopBtn.classList.add('clicked');
            
            // Smooth scroll to top
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
            
            // Remove animation class after animation completes
            setTimeout(() => {
                scrollToTopBtn.classList.remove('clicked');
            }, 300);
        });
        
        // Show button when user reaches halfway through the page on initial load
        document.addEventListener('DOMContentLoaded', () => {
            const pageHeight = Math.max(
                document.body.scrollHeight,
                document.body.offsetHeight,
                document.documentElement.clientHeight,
                document.documentElement.scrollHeight,
                document.documentElement.offsetHeight
            );
            
            const oneThirdPoint = pageHeight / 3; // Show after first third of page
            
            if (window.pageYOffset > oneThirdPoint) {
                scrollToTopBtn.classList.add('visible');
            }
        });
    }
}

/**
 * Add proper card wrappers for better mobile scrolling with snap points
 */
function initializeMobileCardWrappers() {
    const toolsRows = document.querySelectorAll('.tools-row');
    
    toolsRows.forEach(row => {
        // Only process rows that haven't been processed yet
        if (!row.getAttribute('data-processed')) {
            const colDivs = row.querySelectorAll('.col-md-4, .col-lg-3');
            
            colDivs.forEach(colDiv => {
                // Create a wrapper div for scroll snapping
                const wrapper = document.createElement('div');
                wrapper.className = 'tool-card-wrapper';
                
                // Move the col content into the wrapper
                const colContent = colDiv.innerHTML;
                colDiv.innerHTML = '';
                wrapper.innerHTML = colContent;
                
                // Replace the col with the wrapper
                colDiv.parentNode.replaceChild(wrapper, colDiv);
            });
            
            // Mark as processed to avoid repeated processing
            row.setAttribute('data-processed', 'true');
        }
    });
}
