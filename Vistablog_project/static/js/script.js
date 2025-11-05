// Mobile Menu Toggle
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const mobileNav = document.querySelector('.mobile-nav');
const body = document.body;

mobileMenuBtn.addEventListener('click', () => {
    mobileMenuBtn.classList.toggle('active');
    mobileNav.classList.toggle('active');
    body.classList.toggle('no-scroll');
});

// Mobile Dropdown Toggle
const mobileDropdowns = document.querySelectorAll('.mobile-dropdown');

mobileDropdowns.forEach(dropdown => {
    const link = dropdown.querySelector('a');
    
    link.addEventListener('click', (e) => {
        e.preventDefault();
        dropdown.classList.toggle('active');
        
        // Close other dropdowns
        mobileDropdowns.forEach(otherDropdown => {
            if (otherDropdown !== dropdown) {
                otherDropdown.classList.remove('active');
            }
        });
    });
});

// Scroll to Top Button
const scrollToTopBtn = document.querySelector('.scroll-to-top');

window.addEventListener('scroll', () => {
    if (window.pageYOffset > 100) {
        scrollToTopBtn.classList.add('active');
    } else {
        scrollToTopBtn.classList.remove('active');
    }
});

scrollToTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// NEW: Set active navigation link based on current URL
function setActiveNavLink() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.desktop-nav a, .mobile-nav a');
    
    navLinks.forEach(link => {
        // Reset active class
        link.classList.remove('active');
        
        const linkPath = link.getAttribute('href');
        
        // Handle index page separately
        if (currentPath === '/' && linkPath === '/') {
            link.classList.add('active');
            return;
        }
        
        // For other pages, check if the current path contains the link path
        if (currentPath !== '/' && linkPath !== '/' && currentPath.includes(linkPath)) {
            link.classList.add('active');
        }
        
        // Special handling for category pages
        if (currentPath.includes('/category/') && linkPath.includes('/category/')) {
            // Extract slug from paths
            const currentSlug = currentPath.split('/').pop();
            const linkSlug = linkPath.split('/').pop();
            
            if (currentSlug === linkSlug) {
                link.classList.add('active');
            }
        }
    });
}

// Enhanced Pagination System
const POSTS_PER_PAGE = 30;
const MAX_VISIBLE_PAGES = 30;

let currentPage = 1;
let allPosts = [];

// Initialize pagination
function initPagination() {
    allPosts = Array.from(document.querySelectorAll('.post-card'));
    renderPagination();
    showPage(currentPage, false); // Don't scroll on initial load
}

// Show specific page (MODIFIED: Added shouldScroll parameter)
function showPage(page, shouldScroll = false) {
    const totalPages = Math.ceil(allPosts.length / POSTS_PER_PAGE);
    
    // Validate page number
    if (page < 1) page = 1;
    if (page > totalPages && totalPages > 0) page = totalPages;
    
    currentPage = page;
    
    // Hide all posts first
    allPosts.forEach(post => {
        post.style.display = 'none';
    });
    
    // Calculate which posts to show
    const startIndex = (currentPage - 1) * POSTS_PER_PAGE;
    const endIndex = Math.min(startIndex + POSTS_PER_PAGE, allPosts.length);
    
    // Show posts for current page
    for (let i = startIndex; i < endIndex; i++) {
        if (allPosts[i]) {
            allPosts[i].style.display = 'block';
        }
    }
    
    // Update pagination controls
    renderPagination();
    
    // MODIFIED: Scroll to top of posts only if explicitly requested
    if (shouldScroll) {
        const postsSection = document.querySelector('.category-posts') || 
            document.querySelector('.blog-posts');
        if (postsSection) {
            postsSection.scrollIntoView({ behavior: 'smooth' });
        }
    }
}

// Render pagination controls
function renderPagination() {
    const paginationContainer = document.querySelector('.pagination');
    if (!paginationContainer) return;
    
    const totalPages = Math.ceil(allPosts.length / POSTS_PER_PAGE);
    
    // Clear existing pagination
    paginationContainer.innerHTML = '';
    
    if (totalPages <= 1) {
        paginationContainer.style.display = 'none';
        return;
    }
    
    paginationContainer.style.display = 'flex';
    
    // Previous button
    const prevLink = document.createElement('a');
    prevLink.href = '#';
    prevLink.className = 'page-link';
    prevLink.innerHTML = '<i class="fas fa-chevron-left"></i> Prev';
    if (currentPage === 1) {
        prevLink.classList.add('disabled');
    } else {
        prevLink.addEventListener('click', (e) => {
            e.preventDefault();
            showPage(currentPage - 1, true); // MODIFIED: Added true parameter
        });
    }
    paginationContainer.appendChild(prevLink);
    
    // Calculate which page numbers to show
    let startPage = Math.max(1, currentPage - Math.floor(MAX_VISIBLE_PAGES / 2));
    let endPage = Math.min(totalPages, startPage + MAX_VISIBLE_PAGES - 1);
    
    // Adjust if we're at the end
    if (endPage - startPage + 1 < MAX_VISIBLE_PAGES) {
        startPage = Math.max(1, endPage - MAX_VISIBLE_PAGES + 1);
    }
    
    // First page + ellipsis if needed
    if (startPage > 1) {
        const firstPageLink = document.createElement('a');
        firstPageLink.href = '#';
        firstPageLink.className = 'page-link';
        firstPageLink.textContent = '1';
        firstPageLink.addEventListener('click', (e) => {
            e.preventDefault();
            showPage(1, true); // MODIFIED: Added true parameter
        });
        paginationContainer.appendChild(firstPageLink);
        
        if (startPage > 2) {
            const ellipsis = document.createElement('span');
            ellipsis.className = 'page-ellipsis';
            ellipsis.textContent = '...';
            paginationContainer.appendChild(ellipsis);
        }
    }
    
    // Page numbers
    for (let i = startPage; i <= endPage; i++) {
        const pageLink = document.createElement('a');
        pageLink.href = '#';
        pageLink.className = 'page-link';
        if (i === currentPage) {
            pageLink.classList.add('active');
        }
        pageLink.textContent = i;
        pageLink.addEventListener('click', (e) => {
            e.preventDefault();
            showPage(i, true); // MODIFIED: Added true parameter
        });
        paginationContainer.appendChild(pageLink);
    }
    
    // Last page + ellipsis if needed
    if (endPage < totalPages) {
        if (endPage < totalPages - 1) {
            const ellipsis = document.createElement('span');
            ellipsis.className = 'page-ellipsis';
            ellipsis.textContent = '...';
            paginationContainer.appendChild(ellipsis);
        }
        
        const lastPageLink = document.createElement('a');
        lastPageLink.href = '#';
        lastPageLink.className = 'page-link';
        lastPageLink.textContent = totalPages;
        lastPageLink.addEventListener('click', (e) => {
            e.preventDefault();
            showPage(totalPages, true); // MODIFIED: Added true parameter
        });
        paginationContainer.appendChild(lastPageLink);
    }
    
    // Next button
    const nextLink = document.createElement('a');
    nextLink.href = '#';
    nextLink.className = 'page-link';
    nextLink.innerHTML = 'Next <i class="fas fa-chevron-right"></i>';
    if (currentPage === totalPages) {
        nextLink.classList.add('disabled');
    } else {
        nextLink.addEventListener('click', (e) => {
            e.preventDefault();
            showPage(currentPage + 1, true); // MODIFIED: Added true parameter
        });
    }
    paginationContainer.appendChild(nextLink);
    
    // Update page info if element exists
    const pageInfo = document.getElementById('page-info');
    if (pageInfo) {
        const startPost = Math.min((currentPage - 1) * POSTS_PER_PAGE + 1, allPosts.length);
        const endPost = Math.min(currentPage * POSTS_PER_PAGE, allPosts.length);
        pageInfo.textContent = `Showing ${startPost}-${endPost} of ${allPosts.length} posts`;
    }
}

// Close mobile menu when clicking outside
document.addEventListener('click', (e) => {
    if (mobileNav.classList.contains('active') && 
        !e.target.closest('.mobile-nav') && 
        !e.target.closest('.mobile-menu-btn')) {
        mobileMenuBtn.classList.remove('active');
        mobileNav.classList.remove('active');
        body.classList.remove('no-scroll');
    }
});

// Close mobile dropdown when clicking outside
document.addEventListener('click', (e) => {
    if (!e.target.closest('.mobile-dropdown')) {
        mobileDropdowns.forEach(dropdown => {
            dropdown.classList.remove('active');
        });
    }
});

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    setActiveNavLink(); // NEW: Set active navigation state
    initPagination();   // Existing pagination initialization
    
    // Add event listeners for any dynamically added posts
    const observer = new MutationObserver(() => {
        const newPosts = Array.from(document.querySelectorAll('.post-card'));
        if (newPosts.length !== allPosts.length) {
            allPosts = newPosts;
            renderPagination();
            showPage(currentPage, false); // Don't scroll on dynamic changes
        }
    });
    
    const postsContainer = document.querySelector('.posts-container');
    if (postsContainer) {
        observer.observe(postsContainer, { childList: true });
    }
    
    console.log('Vistablog initialized with active nav highlighting');
});