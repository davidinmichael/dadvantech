window.addEventListener("DOMContentLoaded", () => {
	let menuToggle = document.getElementById("menuToggle");
	let navLinks = document.getElementById("navLinks");

	menuToggle.addEventListener("click", () => {
		console.log("Clicked");
		navLinks.classList.toggle("show");
	});
});