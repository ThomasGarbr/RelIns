const buttons = document.querySelectorAll('.submitbtn')

buttons.forEach((button) => {
  button.addEventListener('click', (e) => {
    
    const ANIMATION_SPEED = 1000
    
    let x = e.clientX - button.getBoundingClientRect().left
    let y = e.pageY - button.getBoundingClientRect().top
    
    const ripple = document.createElement('div')
    let color = (window.getComputedStyle(button ,null).getPropertyValue('background-color'));
    color = (color.replace(/[^\d,]/g, '').split(','))
    ripple.style.backgroundColor = `rgba(${color[0]},${color[1]},${color[2]},0.${Number(color[3]) + 5})`;
    ripple.style.left = x + 'px'
    ripple.style.top = y + 'px'
    button.appendChild(ripple)
    
    setTimeout(() => {
      ripple.remove()
    }, ANIMATION_SPEED)
  })
})