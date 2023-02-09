var btn = document.getElementById('btn1')
var block = document.getElementById('b1')
for (let index = 2; index < 4; index++) {
    document.getElementById(`b${index}`).style.display = 'none'
}
console.log(btn)
var current = 1
btn.addEventListener('click', change_to_next, false)

function change_to_next(){
    current ++
    console.log(current)
    block.style.display = 'none'
    block =  document.getElementById(`b${current}`)
    console.log(block)
    block.style.display = ''
    btn = document.getElementById(`btn${current}`)
    btn.addEventListener('click', change_to_next, false)
    
    // btn.addEventListener('click', change_to_next, false)
}