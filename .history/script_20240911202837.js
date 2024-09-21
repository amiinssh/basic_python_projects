const toggleBtn = document.querySelector(".toggleBtn");
const links = document.querySelector(".links");

toggleBtn.addEventListener("click", () => {
    links.classList.toggle("active");
});
