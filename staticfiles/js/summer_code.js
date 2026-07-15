window.addEventListener("DOMContentLoaded", () => {
  const faqItems = document.querySelectorAll(".faq-item");

  faqItems.forEach((item) => {
    const button = item.querySelector(".faq-question");

    button.addEventListener("click", () => {
      faqItems.forEach((faq) => {
        if (faq !== item) {
          faq.classList.remove("active");
        }
      });

      item.classList.toggle("active");
    });
  });

  // Register Form
  const whatsappNumber = "2348140980792"; // Change this

  const form = document.getElementById("registrationForm");

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const parentName = document.getElementById("parentName").value;
    const phone = document.getElementById("phone").value;
    const email = document.getElementById("email").value;
    const childrenCount = document.getElementById("childrenCount").value;
    const ageGroup = document.getElementById("ageGroup").value;
    const message = document.getElementById("message").value;

    const whatsappMessage = `Hello D'Advantech,

I would like to register for the 2026 Online Summer Code Camp.

Parent/Guardian Name: ${parentName}

Phone Number: ${phone}

Email: ${email || "Not provided"}

Number of Children: ${childrenCount}

Preferred Age Group: ${ageGroup}

Additional Information:
${message || "None"}

Please send me the next steps for registration.`;

    const url = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(
      whatsappMessage,
    )}`;

    window.open(url, "_blank");
  });
});
