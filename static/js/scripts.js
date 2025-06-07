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

	const dropdown = document.querySelector(".dropdown > a");
    const dropdownContent = document.querySelector(".dropdown-content");

    dropdown.addEventListener("click", function (e) {
      e.preventDefault(); // prevent the anchor from jumping
      dropdownContent.classList.toggle("show");
	});
	
	const maxSelections = 2;
	const checkboxes = document.querySelectorAll('#specializeGroupCheckboxes input[type="checkbox"]');
  
	checkboxes.forEach(cb => {
	  cb.addEventListener('change', () => {
		const checked = document.querySelectorAll('#specializeGroupCheckboxes input[type="checkbox"]:checked');
		if (checked.length > maxSelections) {
		  cb.checked = false;
		  alert(`You can only select up to ${maxSelections} groups.`);
		}
	  });
	});

});