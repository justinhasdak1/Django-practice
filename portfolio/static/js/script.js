document.addEventListener("DOMContentLoaded", function () {
    const skills = document.querySelectorAll(".skill");
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = 1;
                entry.target.style.transform = "translateY(0)";
                let progress = entry.target.querySelector(".progress");
                let width = entry.target.getAttribute("data-skill");
                progress.style.width = width + "%";
            }
        });
    }, { threshold: 0.3 });

    skills.forEach(skill => observer.observe(skill));
});


document.addEventListener("DOMContentLoaded", function() {
    const projectCards = document.querySelectorAll(".project-card");
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
            }
        });
    }, { threshold: 0.3 });
    
    projectCards.forEach(card => {
        observer.observe(card);
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const services = document.querySelectorAll(".service-card");
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("show");
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.2 });

    services.forEach(service => observer.observe(service));
});


document.addEventListener("DOMContentLoaded", function () {
    const contactSection = document.querySelector(".contact-section");
    const title = document.querySelector(".section-title");
    const subtitle = document.querySelector(".section-subtitle");
    const formContainer = document.querySelector(".contact-form-container");
    
    function revealOnScroll() {
        let sectionTop = contactSection.getBoundingClientRect().top;
        let windowHeight = window.innerHeight;
        if (sectionTop < windowHeight - 100) {
            title.style.opacity = "1";
            title.style.transform = "translateY(0)";
            subtitle.style.opacity = "1";
            subtitle.style.transform = "translateY(0)";
            formContainer.style.opacity = "1";
            formContainer.style.transform = "scale(1)";
        }
    }

    window.addEventListener("scroll", revealOnScroll);
    revealOnScroll();
});


document.addEventListener("DOMContentLoaded", function() {
    const footer = document.querySelector(".footer");
    
    footer.addEventListener("mouseover", () => {
        footer.style.background = "linear-gradient(135deg, #333, #1e1e1e)";
    });

    footer.addEventListener("mouseleave", () => {
        footer.style.background = "linear-gradient(135deg, #1e1e1e, #333)";
    });
});