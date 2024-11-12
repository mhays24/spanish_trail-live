document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".staff-card");

    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.2}s`;
    });
});
