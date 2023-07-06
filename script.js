// Agregar animación al logo en el encabezado
const logo = document.querySelector('.logo');

logo.addEventListener('mouseover', () => {
  logo.classList.add('logo-animation');
});

logo.addEventListener('mouseout', () => {
  logo.classList.remove('logo-animation');
});

// Agregar interactividad al botón de WhatsApp
const whatsappBtn = document.querySelector('.whatsapp-btn');

whatsappBtn.addEventListener('click', () => {
  // Realizar alguna acción al hacer clic en el botón de WhatsApp
  // Por ejemplo, podrías abrir una ventana de chat de WhatsApp usando el enlace adecuado
});

// Agregar animaciones al hero al cargar la página
window.addEventListener('load', () => {
  const heroSection = document.getElementById('hero');
  heroSection.classList.add('fade-in');
});

// Agregar animaciones a los servicios al hacer scroll
const serviceElements = document.querySelectorAll('.service');

function animateOnScroll() {
  const triggerOffset = window.innerHeight * 0.8;

  serviceElements.forEach((element) => {
    const elementTop = element.getBoundingClientRect().top;

    if (elementTop < triggerOffset ) {
      element.classList.add('fade-in');
    }
  });
}

window.addEventListener('scroll', animateOnScroll);
