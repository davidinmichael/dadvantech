window.addEventListener("DOMContentLoaded", () => {
	let menuToggle = document.getElementById("menuToggle");
	let navLinks = document.getElementById("navLinks");

	// Toggle menu on button click
	menuToggle.addEventListener("click", () => {
	navLinks.classList.toggle("show");
	});

	// Close menu when any nav link is clicked
	document.querySelectorAll(".nav-link").forEach(link => {
	link.addEventListener("click", () => {
		navLinks.classList.remove("show");
	});
	});

	// Close menu when clicking outside the nav
	document.addEventListener("click", (event) => {
	const isClickInsideNav = navLinks.contains(event.target) || menuToggle.contains(event.target);

	if (!isClickInsideNav) {
		navLinks.classList.remove("show");
	}
	});

});