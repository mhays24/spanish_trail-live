// Select all sections with class "section-left" and "section-right"
const sectionsLeft = document.querySelectorAll('.section-left');
const sectionsRight = document.querySelectorAll('.section-right');

// Create an Intersection Observer
const observer = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    // Check if the element is in the viewport
    if (entry.isIntersecting) {
      if (entry.target.classList.contains('section-left')) {
        entry.target.classList.add('animate-left');
      } else if (entry.target.classList.contains('section-right')) {
        entry.target.classList.add('animate-right');
      }
      // Stop observing the current element after animation starts
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 }); // Trigger when 50% of the section is visible

// Observe each section
sectionsLeft.forEach(section => observer.observe(section));
sectionsRight.forEach(section => observer.observe(section));