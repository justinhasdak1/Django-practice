document.addEventListener("DOMContentLoaded", function () {
    // Skills Animation
    const skills = document.querySelectorAll(".skill");
    const skillObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
                const progress = entry.target.querySelector(".progress");
                const width = entry.target.getAttribute("data-skill");
                progress.style.width = `${width}%`;
                skillObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.3 });

    skills.forEach((skill) => skillObserver.observe(skill));

    // Project Cards Animation
    const projectCards = document.querySelectorAll(".project-card");
    const projectObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
                projectObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.3 });

    projectCards.forEach((card) => projectObserver.observe(card));

    // Services Animation
    const services = document.querySelectorAll(".service-card");
    const serviceObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
                serviceObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.3 });

    services.forEach((service) => serviceObserver.observe(service));

    // Contact Section Animation
    const contactSection = document.querySelector(".contact-section");
    const contactTitle = document.querySelector(".contact-section .section-title");
    const contactSubtitle = document.querySelector(".contact-section .section-subtitle");
    const contactForm = document.querySelector(".contact-form-container");

    const contactObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                contactTitle.style.opacity = "1";
                contactTitle.style.transform = "translateY(0)";
                contactSubtitle.style.opacity = "1";
                contactSubtitle.style.transform = "translateY(0)";
                contactForm.style.opacity = "1";
                contactForm.style.transform = "scale(1)";
                contactObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.3 });

    contactObserver.observe(contactSection);

    // Form Submission
    document.getElementById("contactForm").addEventListener("submit", function (e) {
        e.preventDefault();
        alert("Thank you for your message!");
    });
});