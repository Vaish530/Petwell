
document.querySelectorAll('nav a').forEach(link => {
  if (link.href === window.location.href) {
      link.style.fontWeight = 'bold';
      link.style.color = 'DarkOliveGreen'; // Highlight active link
  }
});
document.querySelectorAll('nav a').forEach(link => {
  if (link.href === window.location.href) {
      link.style.fontWeight = 'bold';
      link.style.color = 'DarkOliveGreen'; // Highlight active link
  }
});
let slideIndex = 0;
    const slides = document.querySelector('.slides');
    const totalSlides = document.querySelectorAll('.slide').length;

    function showSlide(index) {
      if (index >= totalSlides) {
        slideIndex = 0;
      } else if (index < 0) {
        slideIndex = totalSlides - 1;
      } else {
        slideIndex = index;
      }
      slides.style.transform = 'translateX(' + (-slideIndex * 100) + '%)';
    }

    function nextSlide() {
      showSlide(slideIndex + 1);
    }

    function prevSlide() {
      showSlide(slideIndex - 1);
    }

    function showNumber(phoneNumber) {
      alert("Clinic's Contact Number: " + phoneNumber);
    }

    // Auto-slide every 5 seconds
    setInterval(nextSlide, 5000);
    
        document.getElementById(loginform).addEventListener('submit',function(event){
            event.preventDefault();
            alert("you are logged in");
            window.location.href('index.html');
        });
        function validateForm() {
            var password = document.getElementById("password").value;
            var confirmPassword = document.getElementById("confirm-password").value;
            var error = document.getElementById("error-message");

            if (password !== confirmPassword) {
                error.textContent = "Passwords do not match!";
                return false; // Prevent form submission
            }

           
            return false; // Prevent the default form submission (for demo purposes)
        }
        
  
   
    