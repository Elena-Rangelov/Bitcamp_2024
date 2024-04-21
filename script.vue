let text1 = document.getElementsByClassName('title-text')[0];
let arrow = document.getElementsByClassName('down-arrow')[0];
let resume = document.getElementsByClassName('resume')[0];

window.addEventListener('scroll', () => {
    let value = window.scrollY;
    text1.style.marginTop = value * 1.5 + 'px';
    arrow.style.marginTop = value * 1.5 + 'px';
    resume.style.marginTop = value * 2.5 + 'px';

});

window.addEventListener('scroll', function() {
    const navbar = document.querySelector('header');
    const section1 = document.querySelector('.parallax');
    const section1Height = section1.offsetHeight; 
  
    const scrollPosition = window.scrollY; 
  
    if (scrollPosition > section1Height) {
      navbar.classList.add('black-background');
    } else {
      navbar.classList.remove('black-background');
    }
  });

